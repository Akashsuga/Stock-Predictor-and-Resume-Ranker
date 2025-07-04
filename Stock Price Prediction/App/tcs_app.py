# -*- coding: utf-8 -*-
"""tcs_app.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1Fl8Gdi0FU_6GcYcq51ZLqmfNM4kN24zJ
"""

import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import yfinance as yf
import datetime
from keras.models import load_model
from sklearn.preprocessing import MinMaxScaler
from sklearn.metrics import r2_score, mean_squared_error, mean_absolute_error
import os

# --- Stylish page config ---
st.set_page_config(page_title="Stock Forecast App", layout="wide")
st.markdown("""
    <style>
        .main {background-color: #0E1117; color: white;}
        h1, h2, h3 {color: #33CCCC;}
        .stButton>button {background-color: red; color: white; font-weight: bold;}
        .css-18e3th9 {background-color: #0E1117;}
    </style>
""", unsafe_allow_html=True)

st.title("📈 LSTM Stock Price Forecast")

# --- Sidebar Options ---
st.sidebar.header("Navigation")
page = st.sidebar.radio("Choose Page", ["Home", "Choose Companies", "Upload CSV", "Prediction Type"])

# --- Load Model ---
model = load_model("lstm_model_v2.h5")

# --- Helper Functions ---
def preprocess_data(data):
    df = data[['Open', 'High', 'Low', 'Close', 'Volume']].dropna()
    scaler = MinMaxScaler()
    scaled = scaler.fit_transform(df)
    return df, scaled, scaler

def create_dataset(data, y_col_index=3, window_size=120):
    x, y = [], []
    for i in range(window_size, len(data)):
        x.append(data[i - window_size:i])
        y.append(data[i, y_col_index])
    return np.array(x), np.array(y)

def inverse_close(pred, scaler):
    zeros = np.zeros((len(pred), 3))
    zeros_tail = np.zeros((len(pred), 1))
    pred_inversed = scaler.inverse_transform(np.concatenate([zeros, pred, zeros_tail], axis=1))[:, 3]
    return pred_inversed

def forecast_next_days(data, scaler, model, n_days=10):
    last_data = data[-120:]
    forecasts = []
    for _ in range(n_days):
        inp = last_data.reshape((1, last_data.shape[0], last_data.shape[1]))
        pred = model.predict(inp)[0]
        forecasts.append(pred)
        next_input = np.append(last_data[1:], [np.concatenate([last_data[-1][:3], pred, last_data[-1][-1:]])], axis=0)
        last_data = next_input
    return inverse_close(np.array(forecasts), scaler)

# --- Company Selection ---
selected_company = "TCS.NS"
if page == "Choose Companies":
    company = st.selectbox("Select Company", ["TCS.NS"])
    selected_company = company
    st.session_state.selected_company = company

# --- Upload CSV ---
data = None
if page == "Upload CSV":
    uploaded = st.file_uploader("Upload CSV", type="csv")
    if uploaded:
        data = pd.read_csv(uploaded)
        st.success("CSV Uploaded Successfully")

# --- Fetch Data ---
if data is None:
    today = datetime.datetime.today().strftime('%Y-%m-%d')
    selected_company = st.session_state.get("selected_company", "TCS.NS")
    data = yf.download(selected_company, start="2010-01-01", end=today)
    # If the dataframe has MultiIndex columns (e.g., ('Close', 'TCS.NS')), flatten it
    if isinstance(data.columns, pd.MultiIndex):
        data.columns = data.columns.get_level_values(0)  # Use just the indicator name


# --- HOME PAGE ---
if page == "Home":
    st.subheader("📊 Raw Data Preview")
    st.dataframe(data.sort_index(ascending=False).head(10), use_container_width=True)


    df, scaled_data, scaler = preprocess_data(data)
    x, y = create_dataset(scaled_data)
    x = x.reshape((x.shape[0], x.shape[1], x.shape[2]))

    y_pred_scaled = model.predict(x)
    y_pred = inverse_close(y_pred_scaled, scaler)
    y_actual = inverse_close(y.reshape(-1, 1), scaler)

    st.subheader("📉 Actual vs Predicted")
    fig1, ax1 = plt.subplots(figsize=(14, 5))
    ax1.plot(y_actual[-700:], label="Actual", color='blue')
    ax1.plot(y_pred[-700:], label="Predicted", color='red')
    ax1.set_title("Actual vs Predicted Closing Price")
    ax1.set_xlabel("Days")
    ax1.set_ylabel("INR")
    ax1.grid(True)
    ax1.legend()
    st.pyplot(fig1)

    r2 = r2_score(y_actual, y_pred)
    rmse = np.sqrt(mean_squared_error(y_actual, y_pred))
    mae = mean_absolute_error(y_actual, y_pred)
    st.markdown(f"**R² Score:** {r2:.4f}  |  **RMSE:** {rmse:.2f}  |  **MAE:** {mae:.2f}")

    st.subheader("📄 Last 10 Predictions")
    pred_df = pd.DataFrame({
        "Date": data.index[-len(y_pred):][-10:].date,
        "Actual": y_actual[-10:],
        "Predicted": y_pred[-10:]
    })
    st.table(pred_df)

# --- PREDICTION TYPE PAGE ---
if page == "Prediction Type":
    df, scaled_data, scaler = preprocess_data(data)
    st.subheader("📅 Select Prediction Type")
    pred_type = st.radio("Prediction Option", ["Next N Days", "Specific Date", "Date Range"])

    if pred_type == "Next N Days":
        n = st.number_input("Enter number of days", min_value=1, max_value=100, value=7)
        if st.button("Predict"):
            forecasted = forecast_next_days(scaled_data, scaler, model, n)
            dates = pd.date_range(start=data.index[-1]+pd.Timedelta(days=1), periods=n, freq='B')
            result = pd.DataFrame({"Date": dates.date, "Predicted Close": forecasted})
            st.dataframe(result)
            csv = result.to_csv(index=False).encode('utf-8')
            st.download_button("Download Predictions", csv, "forecast.csv", "text/csv")

    elif pred_type == "Specific Date":
        date_input = st.date_input("Enter Date")
        st.info("Prediction on a specific date will be based on extrapolation. Make sure the date is after the last date in the dataset.")
        if st.button("Predict"):
            days_gap = (date_input - data.index[-1].date()).days
            if days_gap > 0:
                forecasted = forecast_next_days(scaled_data, scaler, model, days_gap)
                st.success(f"Predicted Close on {date_input.strftime('%Y-%m-%d')} = {forecasted[-1]:.2f} INR")
            else:
                st.error("Date should be in the future.")

    elif pred_type == "Date Range":
        start_date = st.date_input("Start Date")
        end_date = st.date_input("End Date")
        if start_date and end_date and end_date > start_date:
            if st.button("Predict"):
                days_gap = (start_date - data.index[-1].date()).days
                range_days = (end_date - start_date).days + 1
                if days_gap >= 0:
                    forecasted = forecast_next_days(scaled_data, scaler, model, days_gap + range_days)
                    forecasted = forecasted[days_gap:]
                    dates = pd.date_range(start=start_date, periods=range_days, freq='B')
                    result = pd.DataFrame({"Date": dates.date, "Predicted Close": forecasted})
                    st.dataframe(result)
                    csv = result.to_csv(index=False).encode('utf-8')
                    st.download_button("Download Predictions", csv, "forecast.csv", "text/csv")
                else:
                    st.error("Start date must be after the last date in the dataset.")
        else:
            st.warning("Select valid start and end dates")
