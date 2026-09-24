import streamlit as st
import joblib
import pandas as pd

st.set_page_config(
    page_title="Crop Recommendation AI",
    page_icon="🌱",
    layout="wide"
)

model = joblib.load("crop_recommendation_model.pkl")

st.markdown(
    """
    <style>
        @import url('https://fonts.googleapis.com/css2?family=Poppins:wght@500;600;700&family=Inter:wght@400;500;600&display=swap');

        html, body, [class*="css"] {
            font-family: 'Inter', sans-serif;
        }

        .stApp {
            background: linear-gradient(180deg, #FBFCF9 0%, #F3F7EF 45%, #EDF4E8 100%);
        }

        .block-container {
            max-width: 980px;
            padding-top: 2rem;
        }

        /* ---------- Hero ---------- */
        .hero {
            background: linear-gradient(135deg, #EAF3E4 0%, #DCEBD6 100%);
            padding: 44px 35px;
            border-radius: 24px;
            text-align: center;
            margin-bottom: 30px;
            box-shadow: 0 8px 28px rgba(84, 122, 88, 0.12);
            border: 1px solid rgba(255,255,255,0.6);
        }

        .hero h1 {
            font-family: 'Poppins', sans-serif;
            color: #1F4A28;
            font-size: 40px;
            font-weight: 700;
            margin-bottom: 10px;
            letter-spacing: -0.5px;
        }

        .hero p {
            color: #4E6B54;
            font-size: 16px;
            margin: 0;
        }

        /* ---------- Input card ---------- */
        .input-card {
            background-color: #FFFFFF;
            border-radius: 20px;
            padding: 28px 30px 8px 30px;
            box-shadow: 0 6px 20px rgba(70, 100, 75, 0.08);
            border: 1px solid #E7EFE3;
            margin-bottom: 24px;
        }

        .input-title {
            font-family: 'Poppins', sans-serif;
            color: #1F4A28;
            font-size: 21px;
            font-weight: 600;
            margin-bottom: 20px;
        }

        /* ---------- Number input fields ----------
           These selectors + !important are needed because Streamlit's
           own theme CSS is very specific and will otherwise make
           typed text invisible or default-colored. */
        div[data-testid="stNumberInput"] input {
            background-color: #F8FAF6 !important;
            border: 1.5px solid #D7E4D1 !important;
            border-radius: 10px !important;
            padding: 8px 12px !important;
            color: #23391F !important;
            -webkit-text-fill-color: #23391F !important;
            font-weight: 600 !important;
            font-size: 15px !important;
            caret-color: #23391F !important;
        }

        div[data-testid="stNumberInput"] input::placeholder {
            color: #9AAE9A !important;
            -webkit-text-fill-color: #9AAE9A !important;
        }

        div[data-testid="stNumberInput"] input:focus {
            border-color: #6FA372 !important;
            box-shadow: 0 0 0 3px rgba(111, 163, 114, 0.18) !important;
        }

        div[data-testid="stNumberInput"] button {
            background-color: #F0F5EC !important;
            border-color: #D7E4D1 !important;
        }

        label[data-testid="stWidgetLabel"] p {
            color: #3B5A40 !important;
            font-weight: 600 !important;
            font-size: 14px !important;
        }

        /* ---------- Button ---------- */
        div.stButton > button {
            width: 100%;
            background: linear-gradient(135deg, #6FA372 0%, #4F8A56 100%);
            color: white;
            border: none;
            border-radius: 14px;
            padding: 14px;
            font-size: 17px;
            font-weight: 600;
            font-family: 'Poppins', sans-serif;
            box-shadow: 0 6px 16px rgba(79, 138, 86, 0.3);
            transition: transform 0.15s ease, box-shadow 0.15s ease;
            margin-top: 10px;
            margin-bottom: 24px;
        }

        div.stButton > button:hover {
            background: linear-gradient(135deg, #5F9663 0%, #437849 100%);
            color: white;
            transform: translateY(-1px);
            box-shadow: 0 8px 20px rgba(79, 138, 86, 0.4);
        }

        div.stButton > button:active {
            transform: translateY(0px);
        }

        /* ---------- Result card ---------- */
        .result-card {
            background: linear-gradient(135deg, #E8F3E4 0%, #D9EBD4 100%);
            padding: 30px;
            border-radius: 20px;
            text-align: center;
            margin-top: 6px;
            margin-bottom: 18px;
            border: 1px solid rgba(111, 163, 114, 0.25);
            box-shadow: 0 6px 18px rgba(84, 122, 88, 0.15);
        }

        .result-card p {
            font-family: 'Poppins', sans-serif;
            color: #1F4A28;
            font-size: 34px;
            font-weight: 700;
            margin: 0;
            letter-spacing: -0.5px;
        }

        .result-label {
            color: #4F8A56;
            font-size: 13px;
            font-weight: 700;
            letter-spacing: 1.5px;
            text-transform: uppercase;
            margin-bottom: 6px;
        }

        div[data-testid="stAlert"] {
            border-radius: 14px;
        }

        .footer {
            text-align: center;
            color: #8AA08C;
            font-size: 13px;
            margin-top: 30px;
            padding-top: 18px;
            border-top: 1px solid #E2EBDD;
        }
    </style>
    """,
    unsafe_allow_html=True
)

st.markdown(
    """
    <div class="hero">
        <h1>🌱 Crop Recommendation AI</h1>
        <p>
            Enter your soil and environmental conditions to get
            an AI-based crop recommendation.
        </p>
    </div>
    """,
    unsafe_allow_html=True
)

st.markdown('<div class="input-card">', unsafe_allow_html=True)

st.markdown(
    '<div class="input-title">🌾 Enter Soil &amp; Environmental Conditions</div>',
    unsafe_allow_html=True
)

col1, col2 = st.columns(2)

with col1:
    N = st.number_input(
        "🧪 Nitrogen (N)", min_value=0.0, max_value=200.0,
        value=None, step=1.0, placeholder="e.g. 90"
    )

    P = st.number_input(
        "🧪 Phosphorus (P)", min_value=0.0, max_value=200.0,
        value=None, step=1.0, placeholder="e.g. 42"
    )

    K = st.number_input(
        "🧪 Potassium (K)", min_value=0.0, max_value=200.0,
        value=None, step=1.0, placeholder="e.g. 43"
    )

    temperature = st.number_input(
        "🌡️ Temperature (°C)", min_value=-10.0, max_value=60.0,
        value=None, step=0.1, placeholder="e.g. 25.5"
    )

with col2:
    humidity = st.number_input(
        "💧 Humidity (%)", min_value=0.0, max_value=100.0,
        value=None, step=1.0, placeholder="e.g. 80"
    )

    ph = st.number_input(
        "⚗️ Soil pH", min_value=0.0, max_value=14.0,
        value=None, step=0.1, placeholder="e.g. 6.5"
    )

    rainfall = st.number_input(
        "🌧️ Rainfall (mm)", min_value=0.0, max_value=500.0,
        value=None, step=1.0, placeholder="e.g. 200"
    )

recommend_clicked = st.button("🌱  Recommend Suitable Crop")

st.markdown('</div>', unsafe_allow_html=True)

if recommend_clicked:

    fields = {
        "Nitrogen": N,
        "Phosphorus": P,
        "Potassium": K,
        "Temperature": temperature,
        "Humidity": humidity,
        "Soil pH": ph,
        "Rainfall": rainfall,
    }
    missing = [name for name, value in fields.items() if value is None]

    if missing:
        st.error(f"⚠️ Please fill in: {', '.join(missing)}.")
    else:
        try:
            input_data = pd.DataFrame(
                [[N, P, K, temperature, humidity, ph, rainfall]],
                columns=["N", "P", "K", "temperature", "humidity", "ph", "rainfall"]
            )

            prediction = model.predict(input_data)
            crop = str(prediction[0]).capitalize()

            st.markdown(
                f"""
                <div class="result-card">
                    <div class="result-label">AI Recommendation</div>
                    <p>🌱 {crop}</p>
                </div>
                """,
                unsafe_allow_html=True
            )

            st.info(
                "Recommended based on the soil and environmental "
                "conditions you provided."
            )

        except Exception as e:
            st.error(f"Something went wrong: {e}")

st.markdown(
    """
    <div class="footer">
        🌿 AI-powered crop recommendation system
    </div>
    """,
    unsafe_allow_html=True
)