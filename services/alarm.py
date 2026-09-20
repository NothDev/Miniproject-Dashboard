def generate_alarms(
    temp_status: str,
    humid_status: str,
    power_status: str
) -> list[str]:
    """คืน list ข้อความเตือน; ถ้าปกติทั้งหมดคืน []"""
    valid_statuses = {"NORMAL", "WARNING", "CRITICAL"}
    statuses = {
        "Temperature": temp_status,
        "Humidity": humid_status,
        "Power": power_status,
    }

    invalid_statuses = {
        name: status
        for name, status in statuses.items()
        if status not in valid_statuses
    }
    if invalid_statuses:
        raise ValueError("สถานะต้องเป็น NORMAL, WARNING หรือ CRITICAL เท่านั้น")

    alarms = []
    for name, status in statuses.items():
        if status == "WARNING":
            alarms.append(f"WARNING: {name} status requires attention")
        elif status == "CRITICAL":
            alarms.append(f"CRITICAL: {name} status requires immediate action")

    return alarms
