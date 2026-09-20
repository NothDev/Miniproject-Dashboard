import streamlit as st

from services.power import calculate_power, classify_power

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
