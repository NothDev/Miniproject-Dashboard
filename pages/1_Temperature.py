import streamlit as st
from services.temperature import classify_temperature
st.title("🌡️ Temperature Monitoring1")
temp = st.slider("อุณอุ หภูมิภู มิ(°C)", -20.0, 80.0, 28.0, 0.5)
status = classify_temperature(temp)
st.metric("อุณอุ หภูมิภู "มิ, f"{temp:.1f} °C")
{"NORMAL": st.success, "WARNING": st.warning, "CRITICAL": st.error}[status](
f"สถานะ: {status}"
)
