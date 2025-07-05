# 📈 Stock Insight Platform

This is a Django-based stock prediction web app that lets users:

- 🔒 Register, login, and logout securely
- 🧠 Enter stock tickers (e.g., AAPL, TSLA) and predict prices
- 📊 View charts for historical and predicted prices
- 🗃️ See their prediction history

---

## 🚀 Technologies Used

- Django & Django REST Framework
- yfinance (for stock data)
- scikit-learn (for basic prediction)
- matplotlib (for charts)
- SQLite (default DB)
- Tailwind CSS (for UI)

---

## 🛠️ Running Locally

```bash
git clone https://github.com/Sreeja061/stock_insight_platform.git
cd stock_insight_platform
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
