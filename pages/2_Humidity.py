import streamlit as st

from services.humidity import classify_humidity

st.title("💧 Humidity Monitoring")

humidity = st.slider("ความชื้น (%)", 0.0, 100.0, 50.0, 0.5)
status = classify_humidity(humidity)

st.metric("ความชื้น", f"{humidity:.1f} %")

{"NORMAL": st.success, "WARNING": st.warning, "CRITICAL": st.error}[status](
    f"สถานะ: {status}"
)
