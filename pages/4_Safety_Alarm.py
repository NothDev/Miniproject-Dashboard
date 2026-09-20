import streamlit as st

from services.alarm import generate_alarms

st.title("Safety Alarm")

module_statuses = {
	"Temperature": st.session_state.get("temperature_status"),
	"Humidity": st.session_state.get("humidity_status"),
	"Power": st.session_state.get("power_status"),
}
missing_modules = [name for name, status in module_statuses.items() if status is None]

if missing_modules:
	st.warning(
		"กรุณาเปิดหน้า "
		+ ", ".join(missing_modules)
		+ " เพื่อให้ระบบคำนวณสถานะก่อน"
	)
	st.stop()

alarms = generate_alarms(
	module_statuses["Temperature"],
	module_statuses["Humidity"],
	module_statuses["Power"],
)

st.subheader("สถานะความปลอดภัย")
for name, status in module_statuses.items():
	st.write(f"{name}: {status}")

if not alarms:
	st.success("ระบบปกติ ไม่พบสัญญาณเตือน")
else:
	for alarm in alarms:
		if alarm.startswith("CRITICAL"):
			st.error(alarm)
		else:
			st.warning(alarm)
