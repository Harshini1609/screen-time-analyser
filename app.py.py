import streamlit as st
import matplotlib.pyplot as plt

from src.train_model import train_model
from src.predict import predict

# ✅ Page config
st.set_page_config(
    page_title="Screen Time Predictor",
    page_icon="📱",
    layout="wide"
)

# ✅ DARK THEME CSS
st.markdown("""
<style>
.stApp {
    background: linear-gradient(to right, #141e30, #243b55);
    color: white;
}
.big-font {
    font-size: 35px !important;
    font-weight: bold;
    text-align: center;
    color: #ffffff;
}
p {
    text-align: center;
    color: #d1d1d1;
}
.card {
    padding: 20px;
    border-radius: 15px;
    background: #1e293b;
    box-shadow: 0px 4px 15px rgba(0,0,0,0.4);
    margin-top: 15px;
    color: white;
}
div.stButton > button {
    background-color: #00c9a7;
    color: white;
    border-radius: 10px;
    height: 3em;
    width: 100%;
    font-weight: bold;
}
</style>
""", unsafe_allow_html=True)

# ✅ Sidebar
st.sidebar.title("📌 About Project")
st.sidebar.info(
    "This AI-based system predicts screen time addiction using Machine Learning."
)

# ✅ Header
st.markdown("<div class='big-font'>📱 Smart Screen Time Analyzer</div>", unsafe_allow_html=True)
st.markdown("<p>AI-powered addiction prediction system</p>", unsafe_allow_html=True)
st.markdown("---")

# ✅ Load model
model = train_model()

# ✅ Input Section
col1, col2, col3 = st.columns(3)

with col1:
    screen_time = st.slider("⏱ Screen Time (hours)", 0, 12)

with col2:
    unlocks = st.slider("🔓 Unlock Count", 0, 100)

with col3:
    notifications = st.slider("🔔 Notifications", 0, 200)

# ✅ Prediction
if st.button("🚀 Predict"):
    result = predict(model, screen_time, unlocks, notifications)

    if result == "High":
        st.markdown("<div class='card' style='border-left:5px solid red;'>⚠️ High Addiction - Reduce usage!</div>", unsafe_allow_html=True)
    elif result == "Medium":
        st.markdown("<div class='card' style='border-left:5px solid orange;'>⚡ Medium Addiction - Be careful!</div>", unsafe_allow_html=True)
    else:
        st.markdown("<div class='card' style='border-left:5px solid green;'>✅ Low Addiction - Good job!</div>", unsafe_allow_html=True)

# ✅ Graph Section
st.markdown("---")
st.subheader("📊 Usage Analysis")

if st.button("📊 Show Analysis"):
    values = [screen_time, unlocks, notifications]
    labels = ["Screen Time", "Unlocks", "Notifications"]

    fig, ax = plt.subplots(figsize=(8, 5))  # FIX SIZE

    ax.bar(labels, values, color=["#00c9a7", "#ffb347", "#ff6961"])

    ax.set_title("User Behavior Analysis", color="white", fontsize=14)
    ax.set_xlabel("Category", color="white")
    ax.set_ylabel("Values", color="white")

    ax.tick_params(axis='x', colors='white')
    ax.tick_params(axis='y', colors='white')

    # Add values on bars
    for i, v in enumerate(values):
        ax.text(i, v + 1, str(v), color='white', ha='center')

    fig.patch.set_facecolor('#141e30')
    ax.set_facecolor('#141e30')

    plt.tight_layout()  # FIX CUTTING

    st.pyplot(fig)

# ✅ Footer
st.markdown("---")
st.caption("Made with ❤️ using Streamlit & Machine Learning")