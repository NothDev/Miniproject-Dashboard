import streamlit as st

from services.alarm import generate_alarms

st.title("🚨 Safety Alarm")

# TODO: (คนที่ 4)
# 1. ให้ผู้ใช้เลือกสถานะ Temperature / Humidity / Power (NORMAL, WARNING, CRITICAL)
#    เช่น ใช้ st.selectbox สามอัน
# 2. เรียก generate_alarms(temp_status, humid_status, power_status)
# 3. แสดงข้อความเตือนแต่ละรายการที่ได้ (ถ้าว่างให้แสดงว่าระบบปกติ)

st.info("หน้านี้ยังไม่เสร็จ - รอคนที่ 4 พัฒนาต่อ")
