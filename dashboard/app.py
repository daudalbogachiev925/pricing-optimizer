import os
import requests
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import streamlit as st

API = os.getenv("API_URL", "http://api:8000")
st.set_page_config(page_title="Pricing", layout="wide")
st.title("Pricing Optimizer")

@st.cache_data(ttl=15)
def fetch(path): return requests.get(f"{API}{path}").json()

segment = st.sidebar.selectbox("Сегмент",
                                ["all", "consumer", "smb", "enterprise"])
query = "" if segment == "all" else f"?segment={segment}"

vw = fetch(f"/api/analysis/vw{query}")
st.subheader("van Westendorp")
c1, c2, c3, c4 = st.columns(4)
c1.metric("PMC", f"{vw['pmc']:.0f}" if vw["pmc"] else "—")
c2.metric("IDP", f"{vw['idp']:.0f}" if vw["idp"] else "—")
c3.metric("OPP", f"{vw['opp']:.0f}" if vw["opp"] else "—")
c4.metric("Респондентов", vw["n_respondents"])

if vw["optimal_range"] and vw["optimal_range"] != [0, 0]:
    st.success(f"Оптимальный диапазон: "
               f"{vw['optimal_range'][0]:.0f} — {vw['optimal_range'][1]:.0f}")

gg = fetch("/api/analysis/gg")
if gg["curve"]:
    st.subheader("Gabor-Granger")
    df = pd.DataFrame(gg["curve"])
    fig = px.line(df, x="price", y="revenue", markers=True)
    st.plotly_chart(fig)
    c5, c6 = st.columns(2)
    c5.metric("Оптимальная цена", f"{gg['optimal_price']:.0f}")
    c6.metric("Выручка", f"{gg['revenue']:,.0f}")

st.subheader("Симулятор тарифов")
st.write("Настройте цены и посмотрите на выручку")
default_prices = {"consumer": 19, "smb": 49, "enterprise": 199}
segments = [
    {"segment": "consumer", "price": 19, "conversion": 0.03, "market_size": 200000},
    {"segment": "smb", "price": 49, "conversion": 0.06, "market_size": 30000},
    {"segment": "enterprise", "price": 199, "conversion": 0.10, "market_size": 3000},
]
new_prices = {}
for seg in segments:
    new_prices[seg["segment"]] = st.slider(
        f"{seg['segment']} (текущая {seg['price']})",
        5, 400, seg["price"])

if st.button("Симулировать"):
    r = requests.post(f"{API}/api/analysis/simulate",
                       json=segments, params={"prices": "{}"})
    try:
        st.json(r.json())
    except Exception:
        st.error(r.text)
