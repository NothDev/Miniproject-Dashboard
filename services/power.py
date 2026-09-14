def calculate_power(voltage: float, current: float) -> float:
    """P = V x I; V > 0, I >= 0; ผิดเงื่อนไข -> ValueError"""
    # TODO: (คนที่ 3) ตรวจสอบเงื่อนไข voltage และ current
    # TODO: คำนวณและคืนค่ากำลังไฟฟ้า
    pass


def classify_power(power_watt: float) -> str:
    """คืน NORMAL|WARNING|CRITICAL"""
    # TODO: (คนที่ 3) เขียนเงื่อนไขจำแนกสถานะตามเกณฑ์
    # < 500 W = NORMAL, 500-1000 W = WARNING, > 1000 W = CRITICAL
    pass
