
# 📈 LSTM-Based Stock Price Prediction

A robust and interactive web application designed to forecast future stock closing prices using an LSTM (Long Short-Term Memory) neural network, built on historical market data. Developed with Streamlit, it provides an intuitive interface for data exploration and predictive visualization.


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

1. App
   - tcs_app.py # Streamlit dashboard application
   - tcs_lstm.py # LSTM training script

2. Models
   - lstm_model_v2.h5 # Trained LSTM model
   - scaler_v2.npy # Scaler used during training
   - min_v2.npy # Optional normalization min values

3. Assets
   - Actual vs Predicted.png # Comparison of actual vs predicted prices
   - Model Valuation.PNG # Summary of model performance metrics like R², RMSE, and MAE.
   - Training vs Test.png # Line plot comparing predicted vs actual values on training and test datasets
   - Training vs Loss Validation.png # training and validation loss evolve to detect overfitting or underfitting

4. Outputs
   - forecast.csv # Sample output
     
5. Recordings/
   -  streamlit_demo.mp4 # Screen recording of the Streamlit app

6. Requirements.txt # Required Python packages

7.  README.md # Project documentation

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
git clone https://github.com/Akashsuga/Stock-Price-Predictor.git

# Navigate into the project directory
cd Stock-Price-Predictor

# Install dependencies
pip install -r requirements.txt

# Run the Streamlit app
streamlit run app/lstm_app.py


```

---

## 📸 Screenshots & Visuals
- Actual vs Predicted ![Actual vs Predicted](https://github.com/user-attachments/assets/f6bd8c2d-5a24-4d31-972e-66aaca14c76c)

- Model Valuation
- ![Model Valuation](https://github.com/user-attachments/assets/8217fa89-c307-4499-8cab-95b5a2e2590b)

- Training vs Test ![Train Vs Test](https://github.com/user-attachments/assets/591fabeb-a692-41e6-b846-27b3c6c95ada)

  
- Training vs Validation Loss ![Training vs Loss Validation](https://github.com/user-attachments/assets/422fcab1-72d3-478c-9e16-50ffe14e812e)


---

## 🎥 Streamlit Demo
Watch a demo of the app running locally in


https://github.com/user-attachments/assets/d082bf34-13aa-4c62-985e-e834d709dc8c


---

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

