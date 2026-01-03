import streamlit as st
import requests
import time

# ===============================
# CONFIG
# ===============================
API_URL = "https://mentalhealthlabel.onrender.com/predict"
REQUEST_TIMEOUT = 120  # seconds 

# ===============================
# PAGE SETUP
# ===============================
st.set_page_config(
    page_title="Mental Health Text Classifier",
    page_icon="🧠",
    layout="centered"
)

st.title("🧠 Mental Health Text Classification")
st.write(
    "Enter a sentence below and the model will predict the mental health category."
)

st.info(
    "ℹ️ Note: The first request may take **60–120 seconds** because the backend is hosted on Render and may be waking up."
)

# ===============================
# USER INPUT
# ===============================
user_text = st.text_area(
    "Enter text",
    height=150,
    placeholder="I feel very low and tired all the time..."
)

# ===============================
# PREDICTION BUTTON
# ===============================
if st.button("Predict"):
    if not user_text.strip():
        st.warning("Please enter some text before clicking Predict.")
    else:
        payload = {"text": user_text}

        with st.spinner("⏳ Waking up the model and making prediction... Please wait"):
            try:
                start_time = time.time()

                response = requests.post(
                    API_URL,
                    json=payload,
                    timeout=REQUEST_TIMEOUT
                )

                elapsed_time = round(time.time() - start_time, 2)

                if response.status_code == 200:
                    result = response.json()

                    prediction = result.get("prediction", "Unknown")

                    st.success(f"✅ Prediction: **{prediction}**")
                    st.caption(f"⏱ Response time: {elapsed_time} seconds")

                else:
                    st.error(
                        f"❌ API Error ({response.status_code}): {response.text}"
                    )

            except requests.exceptions.Timeout:
                st.error(
                    "⏰ The request timed out. "
                    "The server may still be waking up. Please try again."
                )

            except requests.exceptions.RequestException as e:
                st.error(f"🚫 Failed to connect to the API: {e}")

# ===============================
# FOOTER
# ===============================
st.markdown("---")
st.caption("Powered by FastAPI + Logistic Regression + TF-IDF")
