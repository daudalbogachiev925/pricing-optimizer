# pricing-optimizer
платформа ценообразования. van Westendorp Price Sensitivity Meter, Gabor-Granger, симуляция тарифов с эластичностью, разрез по сегментам. Дашборд для Product Marketing.  Стек: FastAPI, PostgreSQL, NumPy, Streamlit, Docker, GitHub Actions.
# pricing-optimizer

Платформа ценообразования: van Westendorp, Gabor-Granger, симулятор.

## Возможности
- van Westendorp (PMC, IDP, OPP)
- Gabor-Granger (оптимум по выручке)
- Симулятор тарифов с эластичностью
- Разрез по сегментам
- Streamlit-дашборд

## Быстрый старт
cp .env.example .env
docker-compose up --build

API: http://localhost:8000/docs
Dashboard: http://localhost:8501

## Тесты
pytest tests/ -v

## Лицензия
MIT
