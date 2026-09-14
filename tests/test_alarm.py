import pytest

from services.alarm import generate_alarms

# TODO: (คนที่ 4) เขียน Test อย่างน้อย 5 กรณีตาม worksheet
# 1. ทุกโมดูลเป็น NORMAL -> ต้องได้ []
# 2. มี 1 โมดูลเป็น WARNING
# 3. มี WARNING และ CRITICAL พร้อมกัน
# 4. ทุกโมดูลเป็น CRITICAL
# 5. มี Input ที่ไม่ใช่ NORMAL/WARNING/CRITICAL -> ต้องเกิด ValueError


def test_all_normal_todo():
    pass


def test_one_warning_todo():
    pass


def test_warning_and_critical_todo():
    pass


def test_all_critical_todo():
    pass


def test_invalid_status_todo():
    pass
