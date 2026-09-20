import streamlit as st

from services.power import calculate_power, classify_power

st.title("⚡ Power Monitoring")

# TODO: (คนที่ 3)
# 1. เพิ่ม Slider สำหรับแรงดันไฟฟ้า (voltage)
# 2. เพิ่ม Slider สำหรับกระแสไฟฟ้า (current)
# 3. เรียก calculate_power(voltage, current) แล้วแสดงค่าด้วย st.metric
# 4. เรียก classify_power(power) แล้วแสดงสถานะด้วย st.success / st.warning / st.error
# 5. หลังได้ status ให้ส่งต่อด้วย st.session_state["power_status"] = status
#    เพื่อให้หน้า 4 อ่านสถานะ Power ไปสร้าง Safety Alarm

st.info("หน้านี้ยังไม่เสร็จ - รอคนที่ 3 พัฒนาต่อ")
