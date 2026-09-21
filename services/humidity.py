# pages/2_Humidity.py

import streamlit as st
from services.humidity import classify_humidity

# ตั้งค่าหน้าเว็บธีม Dark
st.set_page_config(
    page_title="Humidity Monitoring 🐾",
    page_icon="💧",
    layout="centered"
)

# ตกแต่ง CSS Custom สไตล์ Dark Theme + น้องแมว 🐱
st.markdown("""
<style>
    /* Dark Theme Background & Text */
    .main {
        background-color: #121820;
        color: #E2E8F0;
    }
    
    /* กล่องการ์ดสถานะน้องแมว */
    .cat-card {
        background-color: #1A2332;
        border-radius: 16px;
        padding: 20px;
        border: 1px solid #2D3748;
        box-shadow: 0 4px 15px rgba(0, 0, 0, 0.4);
        text-align: center;
        margin-top: 15px;
        margin-bottom: 25px;
    }
    .cat-avatar {
        font-size: 55px;
        line-height: 1.2;
    }
    .cat-status-title {
        font-size: 22px;
        font-weight: bold;
        margin-top: 10px;
    }
    .cat-status-desc {
        font-size: 14px;
        color: #A0AEC0;
        margin-top: 5px;
    }
    
    /* สีของสถานะ */
    .status-normal { color: #10B981; border-left: 5px solid #10B981; }
    .status-warning { color: #F59E0B; border-left: 5px solid #F59E0B; }
    .status-critical { color: #EF4444; border-left: 5px solid #EF4444; }

    /* ตกแต่ง Metric & Badge */
    div[data-testid="stMetricValue"] {
        color: #38BDF8 !important;
        font-size: 40px !important;
    }
</style>
""", unsafe_allow_html=True)

# ส่วนหัวข้อพร้อมลายแมว
st.title("💧 Humidity Monitoring 🐾")
st.caption("ระบบติดตามระดับความชื้นวิศวกรรม (Engineering Monitoring) ฅ^•ﻌ•^ฅ")

st.divider()

# Input Slider
humid = st.slider(
    "🎛️ ปรับจำลองค่าความชื้น (%)",
    min_value=0.0,
    max_value=100.0,
    value=50.0,
    step=0.5
)

# คำนวณสถานะผ่าน Service Logic
status = classify_humidity(humid)

# แสดงผล Metric
col1, col2 = st.columns([1, 1])
with col1:
    st.metric(label="💦 ความชื้นปัจจุบัน", value=f"{humid:.1f} %")
with col2:
    st.metric(label="📊 สถานะระบบ", value=status)

# แมวและข้อความปรับตามสถานะ
cat_data = {
    "NORMAL": {
        "avatar": "😸💬",
        "title": "สถานะปกติ (NORMAL)",
        "desc": "ความชื้นอยู่ในระดับที่เหมาะสมแล้วมนุษย์~ (40% - 60%)",
        "css_class": "status-normal",
        "st_func": st.success
    },
    "WARNING": {
        "avatar": "🙀⚡",
        "title": "เฝ้าระวัง (WARNING)",
        "desc": "ความชื้นเริ่มเบี่ยงเบนจากระดับปกติแล้วนะ! (30%-39% หรือ 61%-70%)",
        "css_class": "status-warning",
        "st_func": st.warning
    },
    "CRITICAL": {
        "avatar": "😾🚨",
        "title": "อันตราย! (CRITICAL)",
        "desc": "ความชื้นอยู่ในระดับอันตรายมาก ตรวจสอบด่วน! (< 30% หรือ > 70%)",
        "css_class": "status-critical",
        "st_func": st.error
    }
}

current_cat = cat_data[status]

# การ์ดน้องแมวรายงานสถานะ
st.markdown(f"""
<div class="cat-card {current_cat['css_class']}">
    <div class="cat-avatar">{current_cat['avatar']}</div>
    <div class="cat-status-title">{current_cat['title']}</div>
    <div class="cat-status-desc">{current_cat['desc']}</div>
</div>
""", unsafe_allow_html=True)

# แสดงกล่องแจ้งเตือนมาตรฐาน Streamlit เพิ่มเติม
current_cat["st_func"](f"**การแจ้งเตือน:** ระบบส่งสถานะ `{status}` สำหรับความชื้น {humid:.1f}%")

# ส่วนคำแนะนำสเปกเกณฑ์
with st.expander("🐾 ดูเกณฑ์การวัดความชื้น (Contract)"):
    st.markdown("""
    - **NORMAL (40% - 60%)**: ระดับความชื้นปกติ
    - **WARNING (30% - 70% ที่ไม่ใช่ Normal)**: เริ่มมีความเสี่ยง
    - **CRITICAL (< 30% หรือ > 70%)**: อันตรายต่อระบบ
    - **Error**: ค่านอกช่วง 0% - 100%
    """)