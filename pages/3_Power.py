import streamlit as st

from services.power import calculate_power, classify_power

st.set_page_config(page_title="Power Monitoring", page_icon="⚡", layout="centered")

# --- Custom CSS สำหรับความสวยงาม ---
st.markdown("""
<style>
    /* พื้นหลังและฟอนต์โดยรวม */
    .main {
        background: linear-gradient(135deg, #0f172a 0%, #1e293b 100%);
    }
    
    /* หัวข้อ */
    h1 {
        background: linear-gradient(90deg, #38bdf8, #a78bfa);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        font-weight: 800;
        text-align: center;
        padding-bottom: 0.5rem;
    }

    /* กล่อง slider */
    div[data-testid="stSlider"] {
        background: rgba(255, 255, 255, 0.04);
        padding: 1.2rem 1.5rem;
        border-radius: 16px;
        margin-bottom: 1rem;
        border: 1px solid rgba(148, 163, 184, 0.15);
    }

    /* label ของ slider */
    div[data-testid="stSlider"] label p {
        font-size: 1.05rem;
        font-weight: 600;
        color: #e2e8f0 !important;
    }

    /* แถบ track ของ slider */
    div[data-testid="stSlider"] div[data-baseweb="slider"] > div > div {
        background: linear-gradient(90deg, #38bdf8, #a78bfa) !important;
    }

    /* หัวจับ (thumb) ของ slider */
    div[data-baseweb="slider"] div[role="slider"] {
        background-color: #ffffff !important;
        border: 3px solid #38bdf8 !important;
        box-shadow: 0 0 12px rgba(56, 189, 248, 0.6);
    }

    /* ตัวเลขค่า slider */
    div[data-testid="stThumbValue"] {
        background: #38bdf8 !important;
        color: #0f172a !important;
        font-weight: 700;
        border-radius: 8px;
    }

    /* st.metric card */
    div[data-testid="stMetric"] {
        background: rgba(255, 255, 255, 0.05);
        padding: 1.2rem;
        border-radius: 16px;
        border: 1px solid rgba(148, 163, 184, 0.15);
        text-align: center;
    }
    div[data-testid="stMetricValue"] {
        color: #38bdf8;
        font-size: 2.2rem !important;
        font-weight: 800;
    }
    div[data-testid="stMetricLabel"] {
        color: #94a3b8;
    }

    /* กล่องสถานะ (success/warning/error) */
    div[data-testid="stAlert"] {
        border-radius: 14px;
        font-weight: 600;
        font-size: 1.05rem;
    }
</style>
""", unsafe_allow_html=True)

st.title("⚡ Power Monitoring")

voltage = st.slider("แรงดันไฟฟ้า (V)", 1.0, 240.0, 220.0, 1.0)
current = st.slider("กระแสไฟฟ้า (A)", 0.0, 10.0, 2.0, 0.1)

power = calculate_power(voltage, current)
status = classify_power(power)
st.session_state["power_status"] = status

st.metric("กำลังไฟฟ้า", f"{power:.1f} W")

{"NORMAL": st.success, "WARNING": st.warning, "CRITICAL": st.error}[status](
    f"สถานะ: {status}"
)
)
