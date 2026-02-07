import streamlit as st
from datetime import date
import time
import base64
import random

# ================= PAGE CONFIG =================
st.set_page_config(page_title="Love_Terminal.exe", layout="wide")

# ================= CONSTANTS =================
PASSWORD = "AjjuuOnly"
USER_1 = "Shweta"
USER_2 = "Ajjuu"

DAYS = [
    ("🌹 Rose Day", date(2026, 2, 7), "Ajjuu 🌹\n\nTu mazhya ayushyatla sabse sundar rose aahe ❤️\nTujhya sobat pratyek divas khup special vatto 💞 HAPPY ROSE DAY PILLAAAA"),
    ("💍 Propose Day", date(2026, 2, 8), "Ajjuu 💍\n\nTu ho YES bolshil ka?\nMazya life cha forever partner banashil ka? ❤️"),
    ("🍫 Chocolate Day", date(2026, 2, 9), "Ajjuu 🍫\n\nTu chocolate sarkha sweet aahe 💖\nEkda taste ghetla ki sodavat nahi 😄HAPPY CHOCOLATE DAY CHOCOO"),
    ("🧸 Teddy Day", date(2026, 2, 10), "Ajjuu 🧸\n\nTeddy nahi pan tu majha comfort aahe 🤗 HAPPY TEDDY DAY "),
    ("🤞 Promise Day", date(2026, 2, 11), "Ajjuu 🤞\n\nPromise — good days, bad days,\nSaglya divsat tujhya sobat ❤️"),
    ("🤗 Hug Day", date(2026, 2, 12), "Ajjuu 🤗\n\nEk tight hug…\nSagla stress nighun jail ❤️"),
    ("💋 Kiss Day", date(2026, 2, 13), "Ajjuu 💋\n\nEk nahi… hazaar kisses pending aahet 😘"),
    ("❤️ Valentine’s Day", date(2026, 2, 14), "Ajjuu ❤️\n\nTu majha Valentine aahe.\nAaj, उद्या ani forever 💞 HAPPY VALENTINE DAY")
]

# ================= STYLE =================
st.markdown("""
<style>
body {
    background: radial-gradient(circle at top, #1a001f, #000);
    color: white;
}

.card {
    padding: 18px;
    border-radius: 15px;
    text-align: center;
    font-size: 18px;
    margin: 10px;
}

.locked {
    background: #2a2a2a;
    color: #777;
}

.popup {
    background: black;
    padding: 30px;
    border-radius: 18px;
    font-family: monospace;
    font-size: 18px;
    color: #00ff9c;
    box-shadow: 0 0 30px #ff4d6d;
    text-align: center;
}

.heart {
    position: fixed;
    animation: floatUp 8s linear infinite;
}

@keyframes floatUp {
    0% {transform: translateY(100vh) scale(0.5); opacity:0;}
    10% {opacity:1;}
    100% {transform: translateY(-10vh) scale(1.4); opacity:0;}
}
</style>
""", unsafe_allow_html=True)

# ================= FLOATING HEARTS =================
hearts = ""
for _ in range(15):
    hearts += f"""
    <div class="heart" style="
        left:{random.randint(0,100)}%;
        animation-delay:{random.uniform(0,5)}s;
        font-size:{random.randint(18,30)}px;
        color:#ff4d6d;">❤️</div>
    """
st.markdown(hearts, unsafe_allow_html=True)

# ================= AUDIO =================
def autoplay_audio(file):
    with open(file, "rb") as f:
        data = f.read()
    b64 = base64.b64encode(data).decode()
    st.markdown(f"""
    <audio autoplay loop>
        <source src="data:audio/mp3;base64,{b64}" type="audio/mp3">
    </audio>
    """, unsafe_allow_html=True)

# ================= SESSION =================
if "auth" not in st.session_state:
    st.session_state.auth = False
if "popup_msg" not in st.session_state:
    st.session_state.popup_msg = None
if "typed_done" not in st.session_state:
    st.session_state.typed_done = False

# ================= PASSWORD =================
if not st.session_state.auth:
    st.title("🔐 Love_Terminal.exe")
    pwd = st.text_input("Enter password", type="password")
    if st.button("Unlock ❤️"):
        if pwd == PASSWORD:
            st.session_state.auth = True
            st.rerun()
        else:
            st.error("Wrong password 😜")
    st.stop()

# ================= PLAY MUSIC =================
autoplay_audio("romantic.mp3")

# ================= HEADER =================
st.markdown(f"### 💻 Love_Terminal.exe  \n**User:** {USER_1} ❤️ {USER_2}")

# ================= GRID =================
today = date.today()
cols = st.columns(4)

for i, (name, unlock, msg) in enumerate(DAYS):
    with cols[i % 4]:
        if today >= unlock:
            if st.button(name):
                st.session_state.popup_msg = msg
                st.session_state.typed_done = False
        else:
            st.markdown(f"<div class='card locked'>{name}<br>🔒 Locked</div>", unsafe_allow_html=True)

# ================= POPUP =================
if st.session_state.popup_msg:
    st.markdown("---")
    st.markdown("<div class='popup'>", unsafe_allow_html=True)

    placeholder = st.empty()
    text = ""

    if not st.session_state.typed_done:
        for ch in st.session_state.popup_msg:
            text += ch
            placeholder.markdown(f"`{text}`")
            time.sleep(0.04)
        st.session_state.typed_done = True
    else:
        st.markdown(f"`{st.session_state.popup_msg}`")

    if st.button("❌ Close"):
        st.session_state.popup_msg = None
        st.session_state.typed_done = False
        st.rerun()

    st.markdown("</div>", unsafe_allow_html=True)
