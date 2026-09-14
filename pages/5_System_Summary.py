import streamlit as st

st.title("📊 System Summary")
import streamlit as st

# 1. Dashboard Modules
st.header("1. Dashboard Modules")

st.markdown("""
- 🌡️ Temperature - ตรวจสอบอุณหภูมิ
- 💧 Humidity - ตรวจสอบความชื้น
- ⚡ Power - คำนวณและตรวจสอบกำลังไฟฟ้า
- 🚨 Safety Alarm - ตรวจสอบสถานะและแจ้งเตือน
- 📊 System Summary - สรุปภาพรวมของระบบ
""")

# 2. Status Criteria
st.header("2. Status Criteria")

st.subheader("🌡️ Temperature")

st.markdown("""
| Temperature | Status |
|---|---|
| ≤ 30°C | NORMAL |
| > 30–35°C | WARNING |
| > 35°C | CRITICAL |
""")

st.subheader("💧 Humidity")

st.markdown("""
| Humidity | Status |
|---|---|
| 40–60% | NORMAL |
| 30–70% แต่ไม่อยู่ใน NORMAL | WARNING |
| <30% หรือ >70% | CRITICAL |
""")

st.subheader("⚡ Power")

st.markdown("""
| Power | Status |
|---|---|
| < 500 W | NORMAL |
| 500–1000 W | WARNING |
| > 1000 W | CRITICAL |
""")

# 3. How to Use
st.header("3. How to Use")

st.markdown("""
1. เลือกโมดูลที่ต้องการจากเมนูด้านซ้าย
2. กรอกค่าที่ต้องการตรวจสอบ
3. ระบบจะแสดงผลการคำนวณ
4. ตรวจสอบสถานะ NORMAL / WARNING / CRITICAL
5. ตรวจสอบหน้า Safety Alarm หากมีการแจ้งเตือน
""")

# 4. Team Members
st.header("4. Team Members")

st.markdown("""
- Person 1 - Temperature
- Person 2 - Humidity
- Person 3 - Power
- Person 4 - Safety Alarm
- Person 5 - System Summary + QA + README
""")

# 5. QA Checklist
st.header("5. QA Checklist")

st.markdown("""
- ตรวจสอบการทำงานของ Temperature
- ตรวจสอบการทำงานของ Humidity
- ตรวจสอบการทำงานของ Power
- ตรวจสอบการทำงานของ Safety Alarm
- ตรวจสอบการทำงานของ Streamlit
- ตรวจสอบการทำงานของ Tests
""")

st.success("System Summary completed")

