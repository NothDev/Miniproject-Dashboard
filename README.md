# Engineering Monitoring Dashboard

โปรเจกต์กลุ่ม: จำลองการติดตามสถานะระบบวิศวกรรม (Temperature / Humidity / Power / Safety Alarm)
เครื่องมือ: Python + Streamlit + pytest + Git/GitHub

## รายชื่อสมาชิกในทีม

| คนที่ | ชื่อ-นามสกุล | หน้าที่หลัก |
|---|---|---|
| 1 | (ใส่ชื่อ) | Temperature Monitoring |
| 2 | (ใส่ชื่อ) | Humidity Monitoring |
| 3 | (ใส่ชื่อ) | Power Monitoring |
| 4 | (ใส่ชื่อ) | Safety Alarm |
| 5 | (ใส่ชื่อ) | System Summary + QA + README |

## โครงสร้างโปรเจกต์

```
engineering-dashboard/
├── app.py
├── requirements.txt
├── .gitignore
├── README.md
├── services/        # Logic (ไม่มี streamlit)
├── pages/           # หน้าจอ Streamlit
└── tests/           # Unit test (pytest)
```

## วิธีติดตั้ง (ทำครั้งแรกครั้งเดียวต่อเครื่อง)

1. Clone repository

   ```bash
   git clone <URL_REPO_ของกลุ่ม>
   cd engineering-dashboard
   ```

2. สร้างและเปิดใช้งาน Virtual Environment

   ```bash
   python -m venv .venv
   ```

   Windows PowerShell:
   ```powershell
   .\.venv\Scripts\Activate.ps1
   ```

   macOS / Linux / Git Bash:
   ```bash
   source .venv/bin/activate
   ```

3. ติดตั้งแพ็กเกจที่จำเป็น

   ```bash
   pip install -r requirements.txt
   ```

4. ตรวจสอบว่าติดตั้งสำเร็จ

   ```bash
   streamlit --version
   pytest --version
   ```

## วิธีรันโปรเจกต์

```bash
streamlit run app.py
```

จากนั้นเปิดลิงก์ที่ Streamlit แสดงใน Terminal แล้วเลือกหน้าต่าง ๆ จากเมนูด้านซ้าย

## วิธีรัน Unit Test

```bash
pytest -q
```

- `.` = test ผ่าน
- `F` = test ไม่ผ่าน
- `E` = error ระหว่างเตรียม test

ห้ามลบ test เพื่อให้ผ่าน ให้กลับไปตรวจ Contract ของฟังก์ชันแทน

## Git Workflow (สรุปสั้น ๆ)

1. `git checkout -b feature/<ชื่อโมดูลของคุณ>` — สร้าง branch ของตัวเอง ห้าม push เข้า `main` โดยตรง
2. เขียน logic ใน `services/`, หน้าจอใน `pages/`, test ใน `tests/`
3. รัน `pytest -q` ให้ผ่านก่อน commit ทุกครั้ง
4. `git add <ไฟล์ของคุณ>` แล้ว `git commit -m "..."`
5. `git push -u origin feature/<ชื่อโมดูลของคุณ>`
6. เปิด Pull Request บน GitHub จาก branch ของคุณ → `main`
7. รอเพื่อน Review อย่างน้อย 1 คนก่อน Merge
8. หลัง merge แล้ว อัปเดต branch ตัวเอง: `git checkout main && git pull origin main`

## สถานะโมดูล (อัปเดตตามความคืบหน้าจริง)

- [x] Temperature Monitoring (ตัวอย่างจาก worksheet)
- [x] Humidity Monitoring
- [ ] Power Monitoring
- [ ] Safety Alarm
- [ ] System Summary
