# 📊 Stock Insight Platform

A full-stack Django-based platform for stock price prediction using historical market data, LSTM models, REST APIs, and a Telegram bot.

---

## 🔧 Features

### 🧠 ML-Based Prediction
- Fetches 10 years of historical stock data using `yfinance`
- Predicts future stock price using a pre-trained LSTM model
- Displays MSE, RMSE, and R² evaluation metrics
- Saves prediction charts (historical & forecasted)

### 👤 User Authentication
- JWT token-based auth using `djangorestframework-simplejwt`
- User registration and login via web form and API

### 🖥️ Frontend Interface
- Tailwind-powered dashboard
- Form to submit stock ticker and view results
- Table of previous predictions with charts

### 🔌 REST API Endpoints
- `POST /api/v1/register/` – Register a user
- `POST /api/v1/token/` – Obtain JWT
- `POST /api/v1/predict/` – Predict a stock price
- `GET /api/v1/predictions/` – View prediction history
- `GET /healthz/` – Health check (no auth)

### 🛠️ Management Commands
- `python manage.py predict --ticker TSLA` – Predict via terminal

### 🤖 Telegram Bot
- `/start` – Connect Telegram
- `/predict TSLA` – Get real-time prediction
- `/latest` – View your latest prediction

---

## 🗂️ Project Structure

