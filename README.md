# 🧠 Mental Health Text Classification – Streamlit App

This repository contains the **Streamlit frontend application** for the Mental Health Text Classification project.  
The app allows users to enter text and receive a predicted mental health category using a **deployed FastAPI backend**.

---

## 🔗 Live Backend API

The Streamlit app consumes predictions from the following REST API:

https://mentalhealthlabel.onrender.com/predict


> ⚠️ Note: Since the backend is hosted on **Render (free tier)**, the **first request may take 20–40 seconds** due to cold start.  
A loading message is shown in the UI to avoid user confusion.

---

## 🎯 Supported Mental Health Labels

The model predicts one of the following categories:

- Normal
- Anxiety
- Depression
- Suicidal

---

## 🖥️ Streamlit App Features

- Simple and clean UI
- Real-time prediction using REST API
- Handles backend cold-start delay gracefully
- Lightweight frontend (no ML model stored here)
- Production-ready architecture

---

## 📁 Project Structure

mental-health-streamlit-app/
│
├── app.py # Streamlit application
├── requirements.txt # Dependencies
└── README.md

---

## ⚙️ Installation & Local Run

### 1️⃣ Clone the repository
```bash
git clone <your-streamlit-repo-url>
cd mental-health-streamlit-app
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
streamlit run app.py
```

---

### 📦 Dependencies
- streamlit
- requests

---

### 🧪 Example Input
*I feel very anxious and overthink everything lately.*

### Output
Prediction: Anxiety

---

## 👨‍💻 Author
### Subir Kumar Behera
Aspiring Data Analyst | **Machine Learning** Enthusiast
