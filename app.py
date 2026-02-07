import streamlit as st
from datetime import date
import time
import random

# ================= PAGE CONFIG =================
st.set_page_config(page_title="Love_Terminal.exe", layout="wide")

# ================= CONSTANTS =================
PASSWORD = "AjjuuOnly"
USER_1 = "Shweta"
USER_2 = "Ajjuu"

DAYS = [
    ("🌹 Rose Day", date(2026, 2, 7), "Ajjuu 🌹\n\nAjju, tu majha favourite rose aahe 🌹Red nahi, pink nahi… \n\ntu mera dil-rose hai ❤️\n\nTu Jab bhi muskuraata hai na, meri duniya aur bhi khil jaati hai 💕❤️\n\nHAPPY ROSE DAY PILLAAAA"),
    ("💍 Propose Day", date(2026, 2, 8), "Ajjuu 💍\n\nTu ho YES bolshil ka?\nwords thode kam pad jaate hain jab tujhe explain karna hota hai 🫶\n\nBut simple sa propose hai \n\n—Will you be my forever person?\n\nAaj, kal aur hamesha 💍❤️"),
    ("🍫 Chocolate Day", date(2026, 2, 9), "Ajjuu 🍫\n\nchocolates sweet hoti hain 🍫\n\nPar tu unse bhi zyada sweet hai 😌\n\nEk bite chocolate ka aur ek smile teri — dono mujhe happy kar dete hain 💕\n\nHappy Chocolate Day ❤️"),
    ("🧸 Teddy Day", date(2026, 2, 10), "Ajjuu 🧸\n\nteddy soft hota hai 🧸\n\nPar tera hug usse bhi zyada warm hai 🤍\n\nAgar tu teddy hota na, main tujhe kabhi shelf pe nahi rakhti…\n\nSeedha dil ke paas 🫶🤗\n\nHappy Teddy Day ❤️"),
    ("🤞 Promise Day", date(2026, 2, 11), "Ajjuu 🤞\n\npromise karti hoon 💍\n\nTere saath hasungi, roothungi, sambhaalungi aur samjhungi 💖\n\nLife thodi messy ho sakti hai,\n\nPar mera saath hamesha tera rahega 🤞"),
    ("🤗 Hug Day", date(2026, 2, 12), "Ajjuu 🤗\n\nek hug tera 🤗\n\nSaari tension, saari thakaan gayab kar deta hai 💞\n\nKabhi words na mile na, bas mujhe tightly hug kar lena…\n\nMain samajh jaungi ❤️\n\nHappy Hug Day ❤️"),
    ("💋 Kiss Day", date(2026, 2, 13), "Ajjuu 💋\n\nkiss sirf lips pe nahi hoti 💋\n\nKabhi forehead pe care wali,\n\nKabhi aankhon pe trust wali,\n\nAur kabhi smile pe pyaar wali 😘\n\nSab teri hi hain 🤍\n\nHappy Kiss Day Babyyy❤️"),
    ("❤️ Valentine’s Day", date(2026, 2, 14), "Ajjuu ❤️\n\ntu mera Valentine hi nahi…\n\nTu meri habit, meri safe place, meri favorite feeling hai ❤️\n\nAaj bhi, kal bhi, aur har Valentine ke din\n\nIt will always be you 💕🌍\n\nHappy Valentine’s Day Jivv❤️")
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
for _ in range(15):
    st.markdown(
        f"<div class='heart' style='left:{random.randint(0,100)}%;"
        f"animation-delay:{random.uniform(0,5)}s;"
        f"font-size:{random.randint(18,30)}px;'>❤️</div>",
        unsafe_allow_html=True
    )

# ================= SESSION =================
if "auth" not in st.session_state:
    st.session_state.auth = False
if "active_msg" not in st.session_state:
    st.session_state.active_msg = None

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

# ================= HEADER =================
st.markdown(f"### 💻 Love_Terminal.exe  \n**User:** {USER_1} ❤️ {USER_2}")

# ================= MUSIC (MOBILE SAFE) =================
st.markdown("### 🎵 Background Music")
st.audio("romantic.mp3")

# ================= GRID =================
today = date.today()
cols = st.columns(4)

for i, (name, unlock, msg) in enumerate(DAYS):
    with cols[i % 4]:
        if today >= unlock:
            if st.button(name):
                st.session_state.active_msg = msg
        else:
            st.markdown(f"<div class='card locked'>{name}<br>🔒 Locked</div>", unsafe_allow_html=True)

# ================= REAL POPUP (STREAMLIT DIALOG) =================
if st.session_state.active_msg:
    with st.dialog("💌 For Ajjuu"):
        typed = ""
        placeholder = st.empty()
        for ch in st.session_state.active_msg:
            typed += ch
            placeholder.markdown(f"`{typed}`")
            time.sleep(0.04)

        if st.button("❤️ Close"):
            st.session_state.active_msg = None
            st.rerun()
