def calculate_power(voltage: float, current: float) -> float:
    """P = V x I; V > 0, I >= 0; ผิดเงื่อนไข -> ValueError"""
    if voltage <= 0:
        raise ValueError("แรงดันไฟฟ้าต้องมากกว่า 0 V")
    if current < 0:
        raise ValueError("กระแสไฟฟ้าต้องไม่น้อยกว่า 0 A")
    return voltage * current


def classify_power(power_watt: float) -> str:
    """คืน NORMAL|WARNING|CRITICAL"""
    if power_watt < 500:
        return "NORMAL"
    if power_watt <= 1000:
        return "WARNING"
    return "CRITICAL"
