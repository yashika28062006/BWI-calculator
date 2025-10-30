import streamlit as st
import plotly.graph_objects as go

# ---------------- CONFIG ----------------
st.set_page_config(
    page_title="AI Health Risk Assessment",
    page_icon="🩺",
    layout="centered"
)

# ---------------- CUSTOM STYLING ----------------
st.markdown("""
    <style>
        [data-testid="stAppViewContainer"] {
            background-image: url('https://cdn.pixabay.com/photo/2018/02/21/01/12/medical-3168260_1280.png');
            background-size: cover;
            background-repeat: no-repeat;
            background-attachment: fixed;
            background-position: center;
        }

        [data-testid="stHeader"] {
            background: rgba(0,0,0,0);
        }

        .main {
            background-color: rgba(255, 255, 255, 0.93);
            padding: 2rem 2.5rem;
            border-radius: 20px;
            box-shadow: 0 8px 25px rgba(0,0,0,0.08);
        }

        h1, h2, h3 {
            color: #0077b6;
            font-weight: 700;
        }

        .stButton>button {
            background-color: #0077b6;
            color: white;
            border-radius: 10px;
            height: 3em;
            font-size: 16px;
            font-weight: 600;
            border: none;
            transition: 0.3s;
        }

        .stButton>button:hover {
            background-color: #00b4d8;
            transform: translateY(-2px);
        }

        /* Doctor Recommendation Cards */
        .result-card {
            border-radius: 15px;
            padding: 1.5rem;
            margin-top: 2rem;
            color: #003049;
            box-shadow: 0 6px 18px rgba(0,0,0,0.1);
        }

        .risk-low {
            background: linear-gradient(135deg, #e0f7fa, #b2ebf2);
            border-left: 6px solid #00796b;
        }

        .risk-moderate {
            background: linear-gradient(135deg, #fff8e1, #ffecb3);
            border-left: 6px solid #f9a825;
        }

        .risk-high {
            background: linear-gradient(135deg, #ffebee, #ffcdd2);
            border-left: 6px solid #d32f2f;
        }

        /* Footer */
        .footer {
            text-align: center;
            font-size: 13px;
            color: #6c757d;
            margin-top: 40px;
        }

        .subtitle {
            color: #6c757d;
            font-size: 15px;
            margin-bottom: 25px;
        }
    </style>
""", unsafe_allow_html=True)

# ---------------- FUNCTIONS ----------------
def calculate_bmi(weight, height):
    return round(weight / (height ** 2), 1)

def assess_health_risk(age, bmi, cholesterol, bp, smoker, activity):
    score = 0
    if bmi < 18.5 or bmi > 30:
        score += 2
    elif bmi > 25:
        score += 1
    if cholesterol == "High":
        score += 2
    elif cholesterol == "Borderline":
        score += 1
    if bp == "High":
        score += 2
    elif bp == "Borderline":
        score += 1
    if smoker:
        score += 2
    if activity == "Low":
        score += 2
    elif activity == "Moderate":
        score += 1
    if age > 50:
        score += 1

    if score <= 2:
        return "Low", "🟢 Excellent — you’re in a healthy range. Maintain regular checkups and stay active!"
    elif score <= 5:
        return "Moderate", "🟡 Moderate risk. Watch your diet, increase exercise, and monitor key vitals."
    else:
        return "High", "🔴 Elevated risk. Consider consulting a doctor for a comprehensive health evaluation."

# ---------------- UI ----------------
st.markdown("<h1>🩺 AI Health Risk Assessment</h1>", unsafe_allow_html=True)
st.markdown("<p class='subtitle'>A professional, doctor-themed health assessment dashboard with a soft medical doodle background.</p>", unsafe_allow_html=True)

st.divider()

col1, col2 = st.columns(2)

with col1:
    age = st.number_input("👶 Age (years)", 1, 120, 30)
    gender = st.selectbox("🧬 Gender", ["Male", "Female", "Other"])
    weight = st.number_input("⚖️ Weight (kg)", 20.0, 200.0, 70.0)
    height = st.number_input("📏 Height (m)", 1.0, 2.5, 1.75)

with col2:
    cholesterol = st.selectbox("🩸 Cholesterol", ["Normal", "Borderline", "High"])
    bp = st.selectbox("❤️ Blood Pressure", ["Normal", "Borderline", "High"])
    smoker = st.checkbox("🚬 I smoke regularly")
    activity = st.selectbox("🏃 Activity Level", ["Low", "Moderate", "High"])

st.divider()

if st.button("🔍 Analyze My Health", use_container_width=True):
    bmi = calculate_bmi(weight, height)
    risk, advice = assess_health_risk(age, bmi, cholesterol, bp, smoker, activity)

    st.markdown("## 📋 Patient Health Report")
    st.metric("Body Mass Index (BMI)", bmi)
    st.metric("Overall Risk Level", risk)

    # --- BMI Gauge ---
    fig = go.Figure()
    fig.add_trace(go.Indicator(
        mode="gauge+number",
        value=bmi,
        gauge={
            "axis": {"range": [10, 40]},
            "bar": {"color": "#0077b6"},
            "steps": [
                {"range": [10, 18.5], "color": "#B3E5FC"},
                {"range": [18.5, 24.9], "color": "#C8E6C9"},
                {"range": [25, 29.9], "color": "#FFF59D"},
                {"range": [30, 40], "color": "#FFCDD2"},
            ],
        },
        title={"text": "BMI Gauge"},
    ))
    fig.update_layout(height=300, margin=dict(l=20, r=20, t=40, b=0))
    st.plotly_chart(fig, use_container_width=True)

    # --- Doctor's Advice Card ---
    card_class = "risk-low" if risk == "Low" else "risk-moderate" if risk == "Moderate" else "risk-high"
    st.markdown(f"""
        <div class='result-card {card_class}'>
            <h4>👨‍⚕️ Doctor’s Recommendation</h4>
            <p style="font-size:16px; margin-top:8px;">{advice}</p>
        </div>
    """, unsafe_allow_html=True)

st.markdown("<div class='footer'>© 2025 MediPredict AI | Designed with ❤️ for smarter healthcare</div>", unsafe_allow_html=True)
