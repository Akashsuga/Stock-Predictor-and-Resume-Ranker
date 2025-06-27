
# 📈 LSTM-Based Stock Price Prediction

<p align="center">
    <img src="https://img.shields.io/github/last-commit/pavithraus/Stock%20Price%20Predictor?style=flat-square" alt="Last Commit">
    <img src="https://img.shields.io/github/languages/top/pavithraus/Stock%20Price%20Predictor?color=blue&style=flat-square" alt="Language">
    <img src="https://img.shields.io/github/languages/count/pavithraus/Stock%20Price%20Predictor?style=flat-square" alt="Language Count">
</p>

---

### ⚙️ Built with the tools and technologies:

<p>
    <img src="https://img.shields.io/badge/-Streamlit-000000?style=for-the-badge&logo=streamlit&logoColor=white" alt="Streamlit">
    <img src="https://img.shields.io/badge/-Tensorflow-FF6F00?style=for-the-badge&logo=tensorflow&logoColor=white" alt="Tensorflow">
    <img src="https://img.shields.io/badge/-Keras-D00000?style=for-the-badge&logo=keras&logoColor=white" alt="Keras">
    <img src="https://img.shields.io/badge/-ScikitLearn-F7931E?style=for-the-badge&logo=scikit-learn&logoColor=white" alt="Scikit-Learn">
    <img src="https://img.shields.io/badge/-NumPy-013243?style=for-the-badge&logo=numpy&logoColor=white" alt="NumPy">
    <img src="https://img.shields.io/badge/-Python-3776AB?style=for-the-badge&logo=python&logoColor=white" alt="Python">
    <img src="https://img.shields.io/badge/-Pandas-150458?style=for-the-badge&logo=pandas&logoColor=white" alt="Pandas">
</p>

An interactive stock prediction web app powered by an LSTM (Long Short-Term Memory) neural network. The app uses historical stock data to forecast future closing prices and is built using Streamlit for visualization.

---

## 🧠 Project Overview

- 📈 Predicts stock closing prices using an LSTM model.
- 💾 Trained on Yahoo Finance data for selected companies (e.g., TCS.NS).
- 🧭 Interactive Streamlit dashboard with forecasting options:
  - Forecast the next N business days
  - Forecast for a specific future date
  - Forecast for a custom date range
- 🖼️ Visualizes actual vs predicted prices
- 📤 Upload your own data & export results as CSV

---

## 📁 Folder Structure

### `Stock Price Predictor/`

1. app
   - lstm_app.py # Streamlit dashboard application
   - stock_predictor.py # LSTM training script

2. models
   - lstm_model.keras # Trained LSTM model
   - scaler.npy # Scaler used during training
   - min.npy # Optional normalization min values

3. assets
   - Actual vs Predicted.png # Comparison of actual vs predicted prices
   - Model Evaluation.PNG # Summary of model performance metrics like R², RMSE, and MAE.
   - Training vs Test.png # Line plot comparing predicted vs actual values on training and test datasets
   - Training vs Validation Loss.png # training and validation loss evolve to detect overfitting or underfitting
     
4. recordings/
   -  streamlit_demo.mp4 # Screen recording of the Streamlit app

5. requirements.txt # Required Python packages

6.  README.md # Project documentation
---


---

## 🧾 Requirements

Install required packages from `requirements.txt`:

- `streamlit`
- `numpy`
- `pandas`
- `keras`
- `tensorflow`
- `matplotlib`
- `scikit-learn`
- `yfinance`

> ⚠️ **Note**: Ensure compatibility (e.g., TensorFlow 2.11, Keras 2.11, NumPy < 2.0) for smooth execution.

---

## 🚀 Quick Start

```bash
# Clone the repository
git clone https://github.com/pavithraus/Stock-Price-Predictor.git

# Navigate into the project directory
cd Stock-Price-Predictor

# Install dependencies
pip install -r requirements.txt

# Run the Streamlit app
streamlit run app/lstm_app.py


## 📸 Screenshots & Visuals
- Actual vs Predicted 
- Model Evaluation
-
- Training vs Test
- Training vs Validation Loss 

## 🎥 Streamlit Demo
Watch a demo of the app running locally in

## ✨ Features

- 📦 Pre-trained LSTM model on stock data

- 📂 Option to upload your own CSV

- 🔁 Forecasting Modes:
  - Next N business days
  - Specific future date
  - Custom date range

- 📤 Download predictions as CSV

- 📈 Visual comparison of predictions vs real data

- 📊 Metrics: R² Score, RMSE, MAE

---

## ✅ Conclusion

This project showcases the power of LSTM models in time series forecasting, specifically applied to stock prices. It merges deep learning with an intuitive UI using Streamlit, allowing users to interactively explore, visualize, and generate stock price predictions.

Key concepts include:

- Data preprocessing and scaling

- Sequence modeling with LSTM

- Evaluation using MAE, RMSE, and R²

- Deployment with Streamlit

**🚫 Disclaimer:** This tool is for educational purposes and does not constitute financial advice.

---

## 🌱 Future Improvements

- 📡 Real-time data updates

- 🧠 Sentiment analysis integration

- 🧮 Ensemble forecasting models

- ☁️ Deploy on Streamlit Cloud / Hugging Face Spaces

