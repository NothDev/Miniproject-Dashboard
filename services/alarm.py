def generate_alarms(
    temp_status: str,
    humid_status: str,
    power_status: str
) -> list[str]:
    """คืน list ข้อความเตือน; ถ้าปกติทั้งหมดคืน []"""
    # TODO: (คนที่ 4) ตรวจสอบว่าแต่ละสถานะเป็น NORMAL/WARNING/CRITICAL เท่านั้น
    #       ถ้าไม่ใช่ ให้ raise ValueError
    # TODO: เรียงลำดับ Temperature -> Humidity -> Power
    #       และเพิ่มข้อความเตือนตามตารางใน worksheet
    pass
