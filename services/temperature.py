def classify_temperature(celsius: float) -> str:
    """
    Classify temperature status.

    NORMAL   : -20 ถึง 30 °C
    WARNING  : มากกว่า 30 ถึง 35 °C
    CRITICAL : มากกว่า 35 ถึง 80 °C
    """

    if not -20 <= celsius <= 80:
        raise ValueError("อุณหภูมิต้องอยู่ระหว่าง -20 ถึง 80 °C")

    if celsius <= 30:
        return "NORMAL"
    elif celsius <= 35:
        return "WARNING"
    else:
        return "CRITICAL"