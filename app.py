import streamlit as st
from streamlit_lottie import st_lottie
import requests
import json



# Page config (unchanged)
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

# New better animation
#lottie_healthcare = load_lottieurl("https://assets4.lottiefiles.com/packages/lf20_mn0xjs9i.json")
lottie_healthcare = load_lottieurl("https://assets10.lottiefiles.com/packages/lf20_qp1q7mct.json")



#def load_lottiefile(filepath: str):
 #   with open(filepath, "r") as f:
  #      return json.load(f)
# Load from local instead of URL
#lottie_healthcare = load_lottiefile("lotties/healthcare.json")


# Background + Styling
st.markdown(
    """
    <style>
    .stApp {
        background: linear-gradient(135deg, #808080, #1a1a1a);
        background-attachment: fixed;
        color: #FFD700; /* Default golden font */
    }
    h1 {
        color: #FFD700 !important;
    }
    h2, h3 {
        color: #FFC300 !important;
    }
    .logo {
        position: fixed;
        top: 20px;
        left: 20px;
        width: 120px;
        z-index: 100;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Display logo if you have a file called 'logo.png' in your app folder
st.markdown(
    """
    <img src="hard.png" class="logo">
    """,
    unsafe_allow_html=True
)

# Title and subtitle
st.title("☁️ HARD , NextGen Cloud HIS")
st.subheader("Revolutionizing Healthcare Information Systems for a Smarter Future")

# Display animation
if lottie_healthcare:
    st_lottie(lottie_healthcare, height=300, key="healthcare")
else:
    st.error("⚠️ Animation failed to load. Please check your internet connection.")

# Main description text
st.write("""
Imagine managing healthcare like never before — secure, cloud-native, and always accessible.  
Our NextGen HIS empowers medical professionals to streamline operations, enhance patient care, and embrace the future of healthcare management.
""")

# Premium button
if st.button("Coming Soon !"):
    st.balloons()

# Footer
st.markdown("---")
st.caption("Built to honor a legacy and lead the future of healthcare technology.")
