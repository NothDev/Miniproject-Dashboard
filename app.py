import streamlit as st

st.set_page_config(page_title="Engineering Monitoring Dashboard", page_icon="🛠️")

st.title("🛠️ Engineering Monitoring Dashboard")

st.markdown(
    """
    ยินดีต้อนรับสู่ **Engineering Monitoring Dashboard**

    ใช้เมนูด้านซ้ายเพื่อเปิดหน้าติดตามแต่ละโมดูล:
    - 🌡️ Temperature Monitoring
    - 💧 Humidity Monitoring
    - ⚡ Power Monitoring
    - 🚨 Safety Alarm
    - 📊 System Summary
    """
)

st.subheader("รายชื่อสมาชิกในกลุ่ม")
st.markdown(
    """
    | คนที่ | ชื่อ-นามสกุล | หน้าที่หลัก |
    |---|---|---|
    | 1 | นางสาว ดุจดาว ลุงพงษ์| Temperature Monitoring |
    | 2 | นายศักดิ์สกุล อนุภาพ | Humidity Monitoring |
    | 3 | นาย อนันตพงษ์ จันทะวัง | Power Monitoring |
    | 4 | นายวิชิต แสนนวล | Safety Alarm |
    | 5 | นาย ธีระกดิ์ สืบตา  | System Summary + QA + README |
    """
)
