import streamlit as st
from datetime import datetime
import base64
import random

# ===================== PAGE CONFIG =====================
st.set_page_config(
    page_title="Will You Be My Valentine? 💖",
    page_icon="💖",
    layout="centered"
)

# ===================== HELPERS =====================
def img_to_base64(path):
    with open(path, "rb") as f:
        return base64.b64encode(f.read()).decode()

# ===================== ASSETS =====================
bg_base64 = img_to_base64("assets/bg.jpg")
img1 = img_to_base64("assets/pic10.jpeg")
img2 = img_to_base64("assets/pic11.png")
img3 = img_to_base64("assets/pic9.jpeg")

# ===================== CSS =====================
st.markdown(f"""
<style>
@import url('https://fonts.googleapis.com/css2?family=Pacifico&family=Poppins:wght@400;600&display=swap');

html, body {{
    margin: 0;
    padding: 0;
    font-family: 'Poppins', sans-serif;
}}

.stApp {{
    background: url("data:image/jpg;base64,{bg_base64}") no-repeat center center fixed;
    background-size: cover;
}}

.main {{
    max-width: 420px;
    margin: auto;
    padding-top: 40px;
    text-align: center;
    color: white;
}}

.title {{
    font-family: 'Pacifico', cursive;
    font-size: 36px;
    text-shadow: 2px 2px 10px #ff4d6d;
}}

.subtitle {{
    font-size: 15px;
    margin-bottom: 16px;
}}

.love-message {{
    font-family: 'Pacifico', cursive;
    font-size: 22px;
    margin: 18px 0;
    color: #ffe6ee;
    text-shadow: 2px 2px 8px #ff4d6d;
    text-align: center;
}}

.countdown {{
    font-family: 'Pacifico', cursive;
    font-size: 22px;
    margin: 18px auto;
    color: #5b1b2d;
    background: rgba(255,255,255,0.65);
    padding: 8px 18px;
    border-radius: 30px;
    width: fit-content;
    box-shadow: 0 6px 16px rgba(0,0,0,0.2);
}}

.footer {{
    font-size: 14px;
    margin-top: 16px;
    text-align: center;
}}

/* ---------- IMAGE GRID ---------- */
.photo-grid {{
    display: flex;
    gap: 16px;
    margin-top: 20px;
}}

.photo-box {{
    flex: 1;
    height: 260px;
    border-radius: 18px;
    overflow: hidden;
    background: white;
    box-shadow: 0 10px 25px rgba(0,0,0,0.25);
}}

.photo-box img {{
    width: 100%;
    height: 100%;
    object-fit: cover;
}}

/* ---------- BUTTONS ---------- */
div[data-testid="column"] {{
    display: flex;
}}

div.stButton > button {{
    width: 100%;
    height: 64px;
    border-radius: 40px;
    font-size: 18px;
    font-weight: 600;
    border: 2px solid rgba(255,255,255,0.7);
    color: white;
    background: linear-gradient(135deg, #ff4d6d, #ff8fa3);
    box-shadow: 0 10px 25px rgba(255,77,109,0.6);
    transition: all 0.25s ease;
}}

div.stButton > button:hover {{
    transform: scale(1.05);
    box-shadow: 0 14px 32px rgba(255,77,109,0.85);
}}

.ofcourse div.stButton > button {{
    background: linear-gradient(135deg, #ff6fb1, #ffc2dd);
}}

/* ---------- CENTER TOAST ---------- */
.center-toast {{
    position: fixed;
    top: 50%;
    left: 50%;
    transform: translate(-50%, -50%);
    background: rgba(255,255,255,0.9);
    color: #ff4d6d;
    padding: 18px 28px;
    border-radius: 30px;
    font-size: 22px;
    font-family: 'Pacifico', cursive;
    box-shadow: 0 12px 30px rgba(0,0,0,0.25);
    z-index: 9999;
    animation: fadeOut 2.8s forwards;
}}

@keyframes fadeOut {{
    0% {{ opacity: 0; }}
    15% {{ opacity: 1; }}
    85% {{ opacity: 1; }}
    100% {{ opacity: 0; }}
}}

/* ---------- FLOATING HEARTS ---------- */
.floating-heart {{
    position: fixed;
    bottom: -30px;
    font-size: 22px;
    animation: floatUp 6s linear infinite;
    opacity: 0.85;
}}

@keyframes floatUp {{
    from {{ transform: translateY(0); opacity: 1; }}
    to {{ transform: translateY(-120vh); opacity: 0; }}
}}

/* ================= MOBILE RESPONSIVE ================= */
@media (max-width: 600px) {{

    .main {{
        max-width: 95%;
        padding-top: 24px;
    }}

    .title {{
        font-size: 30px;
    }}

    .love-message {{
        font-size: 20px;
    }}

    .photo-grid {{
        flex-direction: column;
    }}

    .photo-box {{
        height: 220px;
    }}

    div.stButton > button {{
        height: 58px;
        font-size: 17px;
    }}

    .countdown {{
        font-size: 20px;
        padding: 6px 14px;
    }}

    .floating-heart {{
        font-size: 16px;
    }}
}}
</style>
""", unsafe_allow_html=True)

# ===================== HEADER =====================
st.markdown("""
<div class="main">
    <div class="title">Will You Be My Valentine? 💖</div>
    <div class="subtitle">Forever & Always</div>
</div>
""", unsafe_allow_html=True)

# ===================== IMAGES =====================
st.markdown(f"""
<div class="photo-grid">
    <div class="photo-box"><img src="data:image/jpeg;base64,{img1}"></div>
    <div class="photo-box"><img src="data:image/png;base64,{img2}"></div>
    <div class="photo-box"><img src="data:image/jpeg;base64,{img3}"></div>
</div>
""", unsafe_allow_html=True)

# ===================== MESSAGE =====================
st.markdown("""
<div class="love-message">
Tara roop ni poonam no pagal aeklo...! 💕
</div>
""", unsafe_allow_html=True)

# ===================== COUNTDOWN =====================
valentine = datetime(datetime.now().year, 2, 14)
if datetime.now() > valentine:
    valentine = datetime(datetime.now().year + 1, 2, 14)

days_left = (valentine - datetime.now()).days
st.markdown(
    f"<div class='countdown'>⏳ {days_left} days until Valentine’s Day 💘</div>",
    unsafe_allow_html=True
)

# ===================== STATE =====================
if "choice" not in st.session_state:
    st.session_state.choice = None

# ===================== BUTTONS =====================
b1, b2 = st.columns(2)

with b1:
    if st.button("YES 💍", use_container_width=True):
        st.balloons()
        st.session_state.choice = "yes"

with b2:
    st.markdown('<div class="ofcourse">', unsafe_allow_html=True)
    if st.button("OF COURSE 💖", use_container_width=True):
        st.markdown('<div class="center-toast">I love you ❤️</div>', unsafe_allow_html=True)
        st.session_state.choice = "ofcourse"

# ===================== LOVE EFFECT =====================
if st.session_state.choice:
    for i in range(22):
        st.markdown(
            f"<div class='floating-heart' style='left:{random.randint(0,100)}%; animation-delay:{i*0.18}s;'>❤️</div>",
            unsafe_allow_html=True
        )

# ===================== LOVE LETTER =====================
with st.expander("💌 Open my love letter"):
    st.markdown("""
    <div style="
        font-family: 'Pacifico', cursive;
        font-size: 22px;
        color: #fff1f5;
        text-align: center;
        line-height: 1.6;
        text-shadow: 2px 2px 10px rgba(255, 77, 109, 0.85);
    ">
        प्रेम, क्रोध, फ़िक्र, शिक़ायत, आदर, सम्मान, संसार —  
        <span style="
            color: #ffd6e8;
            font-size: 26px;
            font-weight: bold;
        ">
            “तुम”
        </span>
        <br><br>
        <span style="
            font-size: 18px;
            color: #ffe6ee;
        ">
            Forever yours ❤️
        </span>
    </div>
    """, unsafe_allow_html=True)

st.markdown(
    "<div class='footer'>Happy Valentine’s Day, my love 🌹</div>",
    unsafe_allow_html=True
)
