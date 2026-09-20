import streamlit as st
import streamlit.components.v1 as components

from services.temperature import classify_temperature


# ============================================================
# PAGE CONFIG
# ============================================================

st.set_page_config(
    page_title="Temperature Monitoring",
    page_icon="🌡️",
    layout="wide",
)


# ============================================================
# SESSION STATE
# ============================================================

if "temperature_history" not in st.session_state:
    st.session_state.temperature_history = [28.0]


# ============================================================
# PAGE STYLE
# ============================================================

st.markdown(
    """
    <style>
    .stApp {
        background:
            radial-gradient(circle at 10% 0%, rgba(37, 99, 235, .14), transparent 30%),
            linear-gradient(135deg, #030712 0%, #071426 55%, #050b16 100%);
        color: #f8fafc;
    }

    .block-container {
        max-width: 1180px;
        padding-top: 1.4rem;
        padding-bottom: 3rem;
    }

    h1, h2, h3 {
        color: #f8fafc !important;
    }

    h1 {
        font-size: 2.1rem !important;
        margin-bottom: .15rem !important;
    }

    [data-testid="stCaptionContainer"] {
        color: #79a7ef !important;
    }

    div[data-testid="stVerticalBlockBorderWrapper"] {
        background:
            linear-gradient(
                145deg,
                rgba(10, 31, 61, .96),
                rgba(7, 20, 42, .98)
            );
        border: 1px solid #24477e !important;
        border-radius: 20px !important;
        box-shadow: 0 12px 32px rgba(0, 0, 0, .18);
    }

    div[data-testid="stSlider"] label p {
        color: #dbeafe !important;
        font-weight: 700 !important;
    }

    div[data-testid="stMetric"] {
        background: rgba(14, 38, 75, .65);
        border: 1px solid #28528f;
        padding: 15px 18px;
        border-radius: 16px;
    }

    div[data-testid="stMetricLabel"] {
        color: #93c5fd !important;
    }

    div[data-testid="stMetricValue"] {
        color: #8db7ff !important;
        font-size: 1.75rem !important;
        font-weight: 800 !important;
    }

    .stButton > button {
        border-radius: 12px;
        border: 1px solid #315b9b;
        background: #0b2549;
        color: #bfdbfe;
    }

    .stButton > button:hover {
        border-color: #60a5fa;
        color: #ffffff;
    }
    </style>
    """,
    unsafe_allow_html=True,
)


# ============================================================
# HEADER
# ============================================================

st.title("🌡️ Temperature Monitoring")
st.caption("Real-time temperature monitoring & system status")


# ============================================================
# REQUIRED SLIDER: -20 TO 80 °C
# ============================================================

with st.container(border=True):
    temp = st.slider(
        "🎚️ ปรับอุณหภูมิ (°C)",
        min_value=-20.0,
        max_value=80.0,
        value=28.0,
        step=0.5,
    )


# ============================================================
# REQUIRED SERVICE FUNCTION
# ============================================================

status = classify_temperature(temp)
st.session_state["temperature_status"] = status


# ============================================================
# HISTORY — SAVE REAL SLIDER CHANGES
# ============================================================

if st.session_state.temperature_history[-1] != temp:
    st.session_state.temperature_history.append(temp)

# Keep only the latest 30 values.
st.session_state.temperature_history = (
    st.session_state.temperature_history[-30:]
)


# ============================================================
# TRUE THERMOMETER SCALE
#
# -20 °C =   0%
#   0 °C =  20%
#  30 °C =  50%
#  60 °C =  80%
#  80 °C = 100%
#
# The bulb is NOT part of this scale.
# ============================================================

MIN_TEMP = -20.0
MAX_TEMP = 80.0

fill_percent = (
    (temp - MIN_TEMP)
    / (MAX_TEMP - MIN_TEMP)
) * 100.0

fill_percent = max(0.0, min(100.0, fill_percent))


# ============================================================
# STATUS COLORS
# ============================================================

if status == "NORMAL":
    thermo_color = "#38bdf8"
    thermo_dark = "#2563eb"
    glow = "rgba(56, 189, 248, .62)"

    status_color = "#34d399"
    status_bg = "rgba(6, 78, 59, .75)"
    status_border = "#10b981"
    status_icon = "✓"

elif status == "WARNING":
    thermo_color = "#fbbf24"
    thermo_dark = "#f97316"
    glow = "rgba(251, 191, 36, .65)"

    status_color = "#fbbf24"
    status_bg = "rgba(120, 75, 5, .75)"
    status_border = "#d99b00"
    status_icon = "!"

else:
    thermo_color = "#fb4f6d"
    thermo_dark = "#dc2626"
    glow = "rgba(251, 79, 109, .68)"

    status_color = "#fb7185"
    status_bg = "rgba(110, 25, 45, .75)"
    status_border = "#fb4f6d"
    status_icon = "▲"


# ============================================================
# MAIN LAYOUT
# ============================================================

left, right = st.columns([0.38, 0.62], gap="medium")


# ============================================================
# THERMOMETER
#
# Important:
# .scale-track is the ONLY 0–100% coordinate system.
# The bulb and connector are outside the scale.
# ============================================================

with left:
    with st.container(border=True):

        thermometer_html = f"""
        <!DOCTYPE html>
        <html>
        <head>
        <meta charset="UTF-8">

        <style>
        * {{
            box-sizing: border-box;
        }}

        html,
        body {{
            margin: 0;
            padding: 0;
            width: 100%;
            background: transparent;
            overflow: hidden;
            font-family: Inter, Arial, sans-serif;
        }}

        .wrapper {{
            width: 100%;
            height: 530px;
            display: flex;
            flex-direction: column;
            align-items: center;
            justify-content: flex-start;
            padding-top: 18px;
            color: #f8fafc;
        }}

        .title {{
            margin-bottom: 22px;
            color: #8db7ff;
            font-size: 13px;
            font-weight: 800;
            letter-spacing: 2px;
        }}

        /*
        --------------------------------------------------------
        THERMOMETER ASSEMBLY
        --------------------------------------------------------
        */

        .thermometer-area {{
            position: relative;
            width: 130px;
            height: 330px;
            display: flex;
            justify-content: center;
        }}

        /*
        The visible tube.
        */

        .tube {{
            position: absolute;
            top: 0;
            left: 50%;
            transform: translateX(-50%);

            width: 72px;
            height: 270px;

            border: 7px solid #bfdbfe;
            border-radius: 40px 40px 24px 24px;

            background:
                linear-gradient(
                    90deg,
                    #061426 0%,
                    #0b223d 45%,
                    #0e2948 50%,
                    #0b223d 55%,
                    #061426 100%
                );

            box-shadow:
                inset 0 0 20px rgba(96, 165, 250, .15),
                0 0 22px {glow};

            overflow: hidden;
        }}

        /*
        --------------------------------------------------------
        TRUE SCALE TRACK

        This track alone represents:
        bottom = -20 °C = 0%
        top    =  80 °C = 100%

        The bulb is completely outside this range.
        --------------------------------------------------------
        */

        .scale-track {{
            position: absolute;

            left: 50%;
            bottom: 0;

            transform: translateX(-50%);

            width: 36px;
            height: 100%;
        }}

        /*
        Liquid height is a direct percentage of the scale track.
        No px conversion, no extra bottom offset and no bulb
        height are involved.
        */

        .liquid {{
            position: absolute;

            left: 0;
            bottom: 0;

            width: 100%;
            height: {fill_percent:.3f}%;

            background:
                linear-gradient(
                    to top,
                    {thermo_dark},
                    {thermo_color}
                );

            border-radius: 20px 20px 0 0;

            box-shadow: 0 0 20px {glow};

            transition:
                height .22s ease,
                background .22s ease,
                box-shadow .22s ease;
        }}

        .liquid::after {{
            content: "";

            position: absolute;
            top: 6px;
            left: 5px;

            width: 7px;
            height: calc(100% - 12px);

            border-radius: 10px;

            background:
                linear-gradient(
                    to bottom,
                    rgba(255,255,255,.34),
                    rgba(255,255,255,.03)
                );
        }}

        /*
        Connector is visual only.
        It is NOT part of the temperature scale.
        */

        .connector {{
            position: absolute;

            left: 50%;
            top: 246px;

            transform: translateX(-50%);

            width: 36px;
            height: 48px;

            background:
                linear-gradient(
                    to bottom,
                    {thermo_color},
                    {thermo_dark}
                );

            box-shadow: 0 0 18px {glow};
        }}

        /*
        Bulb is outside the scale.
        */

        .bulb {{
            position: absolute;

            left: 50%;
            top: 242px;

            transform: translateX(-50%);

            width: 88px;
            height: 88px;

            border-radius: 50%;

            border: 7px solid #bfdbfe;

            background: {thermo_color};

            box-shadow:
                0 0 26px {glow},
                inset 0 0 18px rgba(255,255,255,.15);

            transition:
                background .22s ease,
                box-shadow .22s ease;
        }}

        .bulb::after {{
            content: "";

            position: absolute;

            top: 13px;
            left: 17px;

            width: 16px;
            height: 27px;

            border-radius: 50%;

            background: rgba(255,255,255,.18);

            transform: rotate(25deg);
        }}

        /*
        --------------------------------------------------------
        VALUE + STATUS
        --------------------------------------------------------
        */

        .value {{
            margin-top: 5px;

            color: {thermo_color};

            font-size: 42px;
            line-height: 1;

            font-weight: 900;
            letter-spacing: -1px;

            text-shadow: 0 0 18px {glow};
        }}

        .status-pill {{
            margin-top: 15px;

            padding: 8px 20px;

            border-radius: 999px;

            color: {status_color};
            background: {status_bg};

            border: 1px solid {status_border};

            font-size: 13px;
            font-weight: 900;
            letter-spacing: .4px;
        }}

        /*
        --------------------------------------------------------
        SCALE LABELS
        --------------------------------------------------------
        */

        .scale-row {{
            width: 78%;

            margin-top: 21px;

            display: flex;
            justify-content: space-between;
            align-items: center;

            color: #93c5fd;

            font-size: 12px;
        }}

        .scale-center {{
            opacity: .65;
        }}

        .scale-position {{
            margin-top: 7px;

            color: #5878a5;

            font-size: 10px;
            letter-spacing: .4px;
        }}
        </style>

        </head>

        <body>

        <div class="wrapper">

            <div class="title">
                CURRENT TEMPERATURE
            </div>

            <div class="thermometer-area">

                <div class="tube">

                    <div class="scale-track">

                        <div class="liquid"></div>

                    </div>

                </div>

                <div class="connector"></div>

                <div class="bulb"></div>

            </div>

            <div class="value">
                {temp:.1f} °C
            </div>

            <div class="status-pill">
                {status_icon} {status}
            </div>

            <div class="scale-row">
                <span>-20 °C</span>
                <span class="scale-center">30 °C</span>
                <span>80 °C</span>
            </div>

            <div class="scale-position">
                Scale position: {fill_percent:.1f}%
            </div>

        </div>

        </body>
        </html>
        """

        components.html(
            thermometer_html,
            height=540,
            scrolling=False,
        )


# ============================================================
# RIGHT SIDE
# ============================================================

with right:

    st.caption("LIVE MONITORING")

    metric_left, metric_right = st.columns(2)

    with metric_left:
        # Requirement: st.metric
        st.metric(
            "🌡️ อุณหภูมิปัจจุบัน",
            f"{temp:.1f} °C",
        )

    with metric_right:
        st.metric(
            "💡 สถานะปัจจุบัน",
            status,
        )


    # ========================================================
    # Requirement:
    # st.success / st.warning / st.error
    # ========================================================

    if status == "NORMAL":

        st.success(
            "🌱 สถานะ: NORMAL — "
            "อุณหภูมิอยู่ในช่วงปกติ"
        )

    elif status == "WARNING":

        st.warning(
            "⚠️ สถานะ: WARNING — "
            "อุณหภูมิเริ่มสูง ควรตรวจสอบ"
        )

    else:

        st.error(
            "🔥 สถานะ: CRITICAL — "
            "อุณหภูมิสูงเกินกำหนด"
        )


    # ========================================================
    # STATUS RANGE
    # ========================================================

    with st.container(border=True):

        st.subheader("Temperature Status Range")

        normal_col, warning_col, critical_col = st.columns(3)

        with normal_col:
            st.success(
                "✓ NORMAL\n\n"
                "-20 – 30 °C"
            )

        with warning_col:
            st.warning(
                "! WARNING\n\n"
                ">30 – 35 °C"
            )

        with critical_col:
            st.error(
                "▲ CRITICAL\n\n"
                ">35 – 80 °C"
            )


    # ========================================================
    # TEMPERATURE HISTORY
    # ========================================================

    with st.container(border=True):

        title_col, button_col = st.columns(
            [0.72, 0.28]
        )

        with title_col:
            st.subheader("Temperature History")
            st.caption(
                "Values recorded from the temperature slider"
            )

        with button_col:

            if st.button(
                "Clear History",
                use_container_width=True,
            ):

                st.session_state.temperature_history = [temp]
                st.rerun()


        history = st.session_state.temperature_history

        # Real history tied to slider changes.
        st.line_chart(
            history,
            height=220,
            use_container_width=True,
        )

        min_col, current_col, max_col = st.columns(3)

        with min_col:
            st.metric(
                "Minimum",
                f"{min(history):.1f} °C",
            )

        with current_col:
            st.metric(
                "Current",
                f"{temp:.1f} °C",
            )

        with max_col:
            st.metric(
                "Maximum",
                f"{max(history):.1f} °C",
            )
