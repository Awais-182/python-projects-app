import streamlit as st

# 1. Page Configuration
st.set_page_config(
    page_title="Chronos: Time Converter",
    page_icon="⏳",
    layout="centered"
)

# Custom Styling for Cyberpunk/Dark UI
st.markdown("""
    <style>
    .main {
        background-color: #0e1117;
    }
    .metric-card {
        background-color: #1e222d;
        border-radius: 10px;
        padding: 15px;
        text-align: center;
        border: 1px solid #313745;
        box-shadow: 0 4px 6px rgba(0, 0, 0, 0.3);
    }
    .metric-value {
        font-size: 28px;
        font-weight: bold;
        color: #00e5ff;
    }
    .metric-label {
        font-size: 14px;
        color: #a0aab8;
        text-transform: uppercase;
    }
    </style>
""", unsafe_allow_html=True)

# Header Section
st.title("⏳ Chronos Manipulation Engine")
st.caption("v6.5 — Pure Python `divmod()` Time Conversion & Visualizer")

st.divider()

# 2. Disclaimer Notice
st.warning(
    "⚠️ **Calculation Logic Notice:** This system calculates time using a standardized "
    "**30-day average per month** and a **365-day year model** to maintain mathematical consistency "
    "and prevent arithmetic drift."
)

st.write("")

# 3. Input Section
total_seconds = st.number_input(
    "Enter Total Seconds to Manipulate:",
    min_value=0,
    value=35000000,
    step=1000,
    help="Type any positive integer of seconds."
)

# 4. Core divmod() Hierarchical Logic
minutes, seconds = divmod(total_seconds, 60)
hours, minutes = divmod(minutes, 60)
days, hours = divmod(hours, 24)
months, days = divmod(days, 30)
weeks, days = divmod(days, 7)
years, months = divmod(months, 12)

st.write("")

# 5. Conditional Rendering
if total_seconds > 0:
    st.subheader("📊 Breakdown Cards")

    # Styled Metric Cards Layout
    col1, col2, col3, col4 = st.columns(4)
    with col1:
        st.markdown(f'<div class="metric-card"><div class="metric-value">{years}</div><div class="metric-label">Years</div></div>', unsafe_allow_html=True)
    with col2:
        st.markdown(f'<div class="metric-card"><div class="metric-value">{months}</div><div class="metric-label">Months</div></div>', unsafe_allow_html=True)
    with col3:
        st.markdown(f'<div class="metric-card"><div class="metric-value">{weeks}</div><div class="metric-label">Weeks</div></div>', unsafe_allow_html=True)
    with col4:
        st.markdown(f'<div class="metric-card"><div class="metric-value">{days}</div><div class="metric-label">Days</div></div>', unsafe_allow_html=True)

    st.write("")
    col5, col6, col7 = st.columns(3)
    with col5:
        st.markdown(f'<div class="metric-card"><div class="metric-value">{hours}</div><div class="metric-label">Hours</div></div>', unsafe_allow_html=True)
    with col6:
        st.markdown(f'<div class="metric-card"><div class="metric-value">{minutes}</div><div class="metric-label">Minutes</div></div>', unsafe_allow_html=True)
    with col7:
        st.markdown(f'<div class="metric-card"><div class="metric-value">{seconds}</div><div class="metric-label">Seconds</div></div>', unsafe_allow_html=True)

    st.divider()

    # Advanced Visualizations
    st.subheader("🌐 Visual Analytics")

    # Visualization A: Human Lifespan Comparison
    LIFESPAN_SECONDS = 2_500_000_000
    percentage_of_life = min((total_seconds / LIFESPAN_SECONDS), 1.0)

    st.write("##### 🧬 Human Lifespan Scale")
    st.caption(f"Your input ({total_seconds:,} sec) represents roughly **{percentage_of_life * 100:.3f}%** of an average human lifespan (2.5 Billion seconds).")
    st.progress(percentage_of_life)

    st.write("")

    # Visualization B: Month Cycle Progress
    month_progress = days / 30.0
    st.write("##### 📅 Current Month Progress")
    st.caption(f"The remaining **{days} days** complete **{month_progress * 100:.1f}%** of a 30-day cycle.")
    st.progress(month_progress)

    st.write("")

    # Visualization C: Component Breakdown Chart
    st.write("##### 📈 Component Distribution Matrix")
    st.caption("Visualizing the relative weight of each time unit extracted from your input:")

    time_data = {
        "Years": years,
        "Months": months,
        "Weeks": weeks,
        "Days": days,
        "Hours": hours,
        "Minutes": minutes,
        "Seconds": seconds
    }

    st.bar_chart(time_data)

else:
    st.info("Enter a value greater than 0 to view the time manipulation breakdown.")