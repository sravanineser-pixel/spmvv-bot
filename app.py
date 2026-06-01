import streamlit as st
from groq import Groq

 

st.set_page_config(
    page_title="SATHI - SPMVV Doubts Bot",
    page_icon="💜",
    layout="centered"
)

# --- CSS Styling ---
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Poppins:wght@400;500;600;700&display=swap');

.stApp {
    background: linear-gradient(135deg, #f3e5f5, #ede7f6);
    font-family: 'Poppins', sans-serif;
}
.stApp > header {visibility: hidden;}
.block-container { padding-top: 2rem; padding-bottom: 2rem; }

/* Title */
h1 {
    text-align: center;
    font-size: 3.5rem;
    font-weight: 700;
    color: #4A148C;
    margin-bottom: 0.5rem;
}
.subtitle {
    text-align: center;
    color: #6A1B9A;
    font-size: 1.2rem;
    margin-bottom: 2rem;
}

/* Buttons */
.stButton>button {
    background: linear-gradient(90deg, #8E24AA, #AB47BC);
    color: white;
    border-radius: 12px;
    font-weight: 600;
    transition: 0.3s;
    height: 3.5em;
    margin-bottom: 12px;
}
.stButton>button:hover {
    background: linear-gradient(90deg, #6A1B9A, #8E24AA);
    transform: scale(1.05);
    box-shadow: 0 4px 8px rgba(142, 36, 170, 0.3);
}

/* Chat */
.stChatMessage.user {
    background-color: #EDE7F6;
    border-radius: 12px;
    padding: 10px;
}
.stChatMessage.assistant {
    background-color: #F3E5F5;
    border-radius: 12px;
    padding: 10px;
}
.stChatInput > div > div > input {
    border: 2px solid #E0E0E0!important;
    border-radius: 12px!important;
}
</style>
""", unsafe_allow_html=True)

# --- Title ---
st.markdown("<h1>SATHI</h1>", unsafe_allow_html=True)
st.markdown('<p class="subtitle">Your SPMVV Guide</p>', unsafe_allow_html=True)

# --- Chat State ---
if "messages" not in st.session_state:
    st.session_state.messages = []

hostel_list = "Gangothri, Godavari, Kinnera, Kalyani, Gowthami, Manjeera, Sravanthi, Swarnamukhi, Krishnaveni, Shabari"

def add_to_chat(user_msg, bot_msg):
    st.session_state.messages.append({"role": "user", "content": user_msg})
    st.session_state.messages.append({"role": "assistant", "content": bot_msg})

# --- Buttons ---
col1, col2 = st.columns(2)
with col1:
    if st.button("🏠 Hostel Names"):
        add_to_chat("Show hostel names", f"SPMVV hostels: **{hostel_list}**")
        st.rerun()
    if st.button("💰 Hostel Fees"):
        add_to_chat("Hostel fees?", "Hostel fee is **₹4,000 per month (~₹48,000 yearly)** including mess.")
        st.rerun()
    if st.button("🎓 B.Tech Branches"):
        add_to_chat("B.Tech branches?", "Branches: **CSE, ECE, MECH, EEE**. Admission via AP EAPCET.")
        st.rerun()

with col2:
    if st.button("📚 All Courses"):
        add_to_chat("List all courses", "**UG**: B.Tech, B.Sc Nursing, B.Pharm, BBA, LLB\n\n**PG**: M.Tech, MBA, MCA, M.Sc, M.Pharm\n\n**PhD** available")
        st.rerun()
    if st.button("🎉 Fests Info"):
        add_to_chat("Tell me about fests", "SPMVV fests: *Padmavati Utsav*, *Techno Spark*, Hostel Day, Dept Fests.")
        st.rerun()
    if st.button("🏛️ About SPMVV"):
        add_to_chat("About SPMVV", """**Sri Padmavati Mahila Visvavidyalayam (SPMVV)**

- Established: 1983 by Sri N.T. Rama Rao
- Type: State Women's University | NAAC A+ Grade
- Location: Tirupati, Andhra Pradesh
- Campus: 138 acres | Students: ~5,000
- VC: Prof. V. Uma
- NIRF 2025: Ranked 60th in Pharmacy

**Highlights:**
- Only women’s university in AP offering Engineering + Sciences + Arts
- Admissions via AP EAPCET, AP ICET, AP PGCET, AP LAWCET""")
        st.rerun()

st.divider()

# --- Chat Display ---
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# --- Chat Input ---
if prompt := st.chat_input("Ask SATHI..."):
    st.session_state.messages.append({"role": "user", "content": prompt})
    prompt_lower = prompt.lower().strip()
    response = ""

    # Greetings
    if prompt_lower in ["hi","hello","hey","hi sathi","hello sathi"]:
        response = "Hello! I'm SATHI, your SPMVV guide. Ask me about **admissions, hostels, courses, placements, or fests**."

    # Admission Process
    elif "admission" in prompt_lower or "apply" in prompt_lower or "join" in prompt_lower:
        response = """**Admission Process at SPMVV:**

- **B.Tech**: AP EAPCET → Counseling → Fee Payment → Admission
- **MBA/MCA**: AP ICET → Counseling → Admission
- **M.Tech/M.Pharm/M.Sc**: AP PGCET → Counseling → Admission
- **Law (LLB/LLM)**: AP LAWCET → Counseling → Admission
- **Nursing/Pharmacy**: AP EAPCET → Counseling → Admission

**Steps:**
1. Register for entrance exam
2. Appear & secure rank
3. Attend counseling
4. Submit documents + pay fees
5. Hostel allotment if needed

📞 Contact: 0877-2284592 | 🌐 spmvv.ac.in"""

    # Eligibility
    elif "eligibility" in prompt_lower:
        response = """**Eligibility Criteria:**
- B.Tech: 10+2 with MPC + AP EAPCET
- MBA/MCA: Graduation + AP ICET
- M.Sc/M.Tech/M.Pharm: Graduation in relevant field + AP PGCET
- Law: Graduation + AP LAWCET
- Nursing/Pharmacy: 10+2 BiPC + AP EAPCET"""

    # Placements
    elif "placement" in prompt_lower or "jobs" in prompt_lower:
        response = """**Placements at SPMVV:**
- Recruiters: Infosys, TCS, Wipro, Cognizant
- Avg Package: ₹4–6 LPA
- Highest Package (2025): ₹12 LPA
- Career Guidance Cell provides training & internships"""

    # Hostel Info
    elif "hostel" in prompt_lower:
        if "name" in prompt_lower:
            response = f"Hostels: **{hostel_list}**"
        elif "fee" in prompt_lower:
            response = "Hostel fee: **₹4,000 per month (~₹48,000 yearly)** including mess."
        else:
            response = "SPMVV hostels provide safe accommodation with Wi‑Fi, mess, and study spaces."

    # Fests
    elif "fest" in prompt_lower or "event" in prompt_lower:
        response = "SPMVV hosts *Padmavati Utsav*, *Techno Spark*, Hostel Day, and Dept Fests every year."

    # Contact
    elif "contact" in prompt_lower or "phone" in prompt_lower:
        response = """**SPMVV Contact Info:**
📞 0877-2284592
📍 Padmavati Nagar, Tirupati, AP - 517502
🌐 spmvv.ac.in
📧 registrar@spmvv.ac.in"""

    else:
        response = "I'm SATHI — ask me about **admissions, hostels, courses, placements, or fests**."

    st.session_state.messages.append({"role": "assistant", "content": response})
    st.rerun()
