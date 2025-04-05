import streamlit as st
from streamlit_lottie import st_lottie
import requests

# Page config (corrected)
st.set_page_config(
    page_title="NextGen Cloud HIS",
    page_icon="☁️",
    layout="centered",
    initial_sidebar_state="collapsed"
)

# Load a lottie animation
def load_lottieurl(url: str):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

# Example Lottie animation (cloud technology theme)
lottie_cloud = load_lottieurl("https://assets10.lottiefiles.com/packages/lf20_qp1q7mct.json")

# Background styling (this is where background color is set)
st.markdown(
    """
    <style>
    .stApp {
        background: linear-gradient(135deg, #c3ecff, #e0f7ff);
        background-attachment: fixed;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Title and description
st.title("☁️ NextGen Cloud HIS")
st.subheader("Revolutionizing Healthcare Information Systems")

# Display animation
if lottie_cloud:
    st_lottie(lottie_cloud, height=300, key="cloud")
else:
    st.error("⚠️ Animation failed to load. Please check your internet connection.")

# Main text
st.write("""
Imagine managing healthcare like never before — secure, accessible, and cloud-native.  
Our NextGen HIS empowers medical professionals to streamline operations, enhance patient care, and embrace true digital transformation.
""")

# Fancy button
if st.button("🚀 Learn More Soon"):
    st.balloons()

# Footer
st.markdown("---")
st.caption("Built with ❤️ to honor a legacy and lead the future of healthcare technology.")
