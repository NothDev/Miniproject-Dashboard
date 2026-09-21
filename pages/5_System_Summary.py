import streamlit as st

# ---------------------------------------------------------
# Page Configuration
# ---------------------------------------------------------
st.set_page_config(
    page_title="System Summary",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom Styling (CSS Injection)
st.markdown("""
<style>
    .status-normal { background-color: #d4edda; color: #155724; padding: 4px 8px; border-radius: 4px; font-weight: bold; }
    .status-warning { background-color: #fff3cd; color: #856404; padding: 4px 8px; border-radius: 4px; font-weight: bold; }
    .status-critical { background-color: #f8d7da; color: #721c24; padding: 4px 8px; border-radius: 4px; font-weight: bold; }
    .module-card {
        padding: 15px;
        border-radius: 10px;
        border: 1px solid #e0e0e0;
        background-color: #f9f9f9;
        margin-bottom: 10px;
    }
</style>
""", unsafe_allow_html=True)

# ---------------------------------------------------------
# Header & Overview
# ---------------------------------------------------------
st.title("📊 System Summary & Documentation")
st.caption("ระบบสรุปภาพรวม เกณฑ์การทำงาน และคู่มือการใช้งานระบบ")
st.divider()

# ---------------------------------------------------------
# Main Tabs Navigation
# ---------------------------------------------------------
tab1, tab2, tab3, tab4 = st.tabs([
    "🧩 Dashboard Modules", 
    "🎯 Status Criteria", 
    "📖 How to Use", 
    "👥 Team & QA"
])

# ---------------------------------------------------------
# TAB 1: Dashboard Modules
# ---------------------------------------------------------
with tab1:
    st.subheader("Dashboard Modules")
    st.write("โมดูลการทำงานหลักของระบบ")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        <div class="module-card">
            <h4>🌡️ Temperature</h4>
            <p>ตรวจสอบและติดตามค่าอุณหภูมิของระบบ</p>
        </div>
        <div class="module-card">
            <h4>💧 Humidity</h4>
            <p>ตรวจสอบและติดตามระดับความชื้นสัมพัทธ์</p>
        </div>
        <div class="module-card">
            <h4>⚡ Power</h4>
            <p>คำนวณและตรวจสอบปริมาณการใช้กำลังไฟฟ้า</p>
        </div>
        """, unsafe_allow_html=True)
        
    with col2:
        st.markdown("""
        <div class="module-card">
            <h4>🚨 Safety Alarm</h4>
            <p>ตรวจสอบสถานะความปลอดภัยและการแจ้งเตือนฉุกเฉิน</p>
        </div>
        <div class="module-card">
            <h4>📊 System Summary</h4>
            <p>สรุปภาพรวม รายงานผล และเกณฑ์การควบคุมทั้งหมด</p>
        </div>
        """, unsafe_allow_html=True)

# ---------------------------------------------------------
# TAB 2: Status Criteria
# ---------------------------------------------------------
with tab2:
    st.subheader("เกณฑ์การประเมินสถานะ (Status Criteria)")
    
    col_t, col_h, col_p = st.columns(3)
    
    with col_t:
        with st.container(border=True):
            st.markdown("### 🌡️ Temperature")
            st.markdown("""
            | เงื่อนไข | สถานะ |
            |---|---|
            | ≤ 30°C | <span class="status-normal">NORMAL</span> |
            | > 30–35°C | <span class="status-warning">WARNING</span> |
            | > 35°C | <span class="status-critical">CRITICAL</span> |
            """, unsafe_allow_html=True)
            
    with col_h:
        with st.container(border=True):
            st.markdown("### 💧 Humidity")
            st.markdown("""
            | เงื่อนไข | สถานะ |
            |---|---|
            | 40–60% | <span class="status-normal">NORMAL</span> |
            | 30–70% (ไม่อยู่ใน Normal) | <span class="status-warning">WARNING</span> |
            | <30% หรือ >70% | <span class="status-critical">CRITICAL</span> |
            """, unsafe_allow_html=True)
            
    with col_p:
        with st.container(border=True):
            st.markdown("### ⚡ Power")
            st.markdown("""
            | เงื่อนไข | สถานะ |
            |---|---|
            | < 500 W | <span class="status-normal">NORMAL</span> |
            | 500–1000 W | <span class="status-warning">WARNING</span> |
            | > 1000 W | <span class="status-critical">CRITICAL</span> |
            """, unsafe_allow_html=True)

# ---------------------------------------------------------
# TAB 3: How to Use
# ---------------------------------------------------------
with tab3:
    st.subheader("ขั้นตอนการใช้งานระบบ")
    
    steps = [
        ("1️⃣ เลือกโมดูล", "เลือกโมดูลที่ต้องการจากเมนูด้านซ้าย (Sidebar)"),
        ("2️⃣ ป้อนข้อมูล", "กรอกค่าที่ต้องการตรวจสอบลงในช่องป้อนข้อมูล"),
        ("3️⃣ คำนวณผลลัพธ์", "ระบบจะประมวลผลและแสดงค่าการคำนวณอัตโนมัติ"),
        ("4️⃣ ตรวจสอบสถานะ", "สังเกตระดับสถานะ (NORMAL / WARNING / CRITICAL)"),
        ("5️⃣ ตรวจสอบความปลอดภัย", "หากพบสถานะผิดปกติ ให้ตรวจสอบหน้า Safety Alarm ทันที")
    ]
    
    for title, desc in steps:
        with st.container(border=True):
            st.markdown(f"**{title}**")
            st.write(desc)

# ---------------------------------------------------------
# TAB 4: Team & QA
# ---------------------------------------------------------
with tab4:
    col_team, col_qa = st.columns(2)
    
    with col_team:
        with st.container(border=True):
            st.subheader("👥 Team Members")
            st.markdown("""
            - **Person 1:** Temperature Module
            - **Person 2:** Humidity Module
            - **Person 3:** Power Module
            - **Person 4:** Safety Alarm Module
            - **Person 5:** System Summary + QA + README
            """)
            
    with col_qa:
        with st.container(border=True):
            st.subheader("✅ QA Checklist")
            st.checkbox("ตรวจสอบการทำงานของ Temperature", value=True)
            st.checkbox("ตรวจสอบการทำงานของ Humidity", value=True)
            st.checkbox("ตรวจสอบการทำงานของ Power", value=True)
            st.checkbox("ตรวจสอบการทำงานของ Safety Alarm", value=True)
            st.checkbox("ตรวจสอบการทำงานของ Streamlit UI", value=True)
            st.checkbox("ตรวจสอบการทำงานของ Test Cases", value=True)

st.divider()
st.success("System Summary completed successfully.")