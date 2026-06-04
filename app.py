import streamlit as st
from groq import Groq

st.set_page_config(
    page_title="SATHI - SPMVV Doubts Bot",
    page_icon="💜",
    layout="centered"
)

# --- CSS Styling: Glassmorphism + Saturday Font ---
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Poppins:wght@400;500;600;700;800&family=Satisfy&display=swap');

.stApp {
    background: linear-gradient(-45deg, #e1bee7, #f3e5f5, #ede7f6, #d1c4e9);
    background-size: 400% 400%;
    animation: gradientBG 15s ease infinite;
    font-family: 'Poppins', sans-serif;
}

@keyframes gradientBG {
    0% { background-position: 0% 50%; }
    50% { background-position: 100% 50%; }
    100% { background-position: 0% 50%; }
}

.stApp > header {visibility: hidden;}
.block-container { 
    padding-top: 2rem; 
    padding-bottom: 2rem;
    max-width: 700px;
}

.main > div {
    background: rgba(255, 255, 255, 0.25);
    backdrop-filter: blur(10px);
    -webkit-backdrop-filter: blur(10px);
    border-radius: 20px;
    border: 1px solid rgba(255, 255, 255, 0.3);
    padding: 2rem;
    box-shadow: 0 8px 32px 0 rgba(106, 27, 154, 0.15);
}

/* --- Title - SATURDAY FONT STYLE --- */
h1 {
    text-align: center;
    font-family: 'Satisfy', cursive;
    font-size: 5.5rem;
    font-weight: 400;
    background: linear-gradient(90deg, #4A148C, #8E24AA);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    margin-bottom: 0rem;
    line-height: 1;
}
.subtitle {
    text-align: center;
    color: #6A1B9A;
    font-size: 1.1rem;
    font-weight: 500;
    font-family: 'Poppins', sans-serif;
    margin-bottom: 2.5rem;
    opacity: 0.9;
    margin-top: -5px;
}

.stButton>button {
    background: rgba(142, 36, 170, 0.8);
    backdrop-filter: blur(5px);
    color: white;
    border: 1px solid rgba(255, 255, 255, 0.3);
    border-radius: 15px;
    font-weight: 600;
    font-size: 0.95rem;
    font-family: 'Poppins', sans-serif;
    transition: all 0.3s ease;
    height: 3.5em;
    margin-bottom: 12px;
    box-shadow: 0 4px 15px rgba(106, 27, 154, 0.2);
}
.stButton>button:hover {
    background: rgba(106, 27, 154, 0.9);
    transform: translateY(-3px) scale(1.02);
    box-shadow: 0 6px 20px rgba(106, 27, 154, 0.4);
    border: 1px solid rgba(255, 255, 255, 0.5);
}

.stChatMessage {
    background: rgba(255, 255, 255, 0.4);
    backdrop-filter: blur(8px);
    border-radius: 18px;
    padding: 1rem;
    margin-bottom: 1rem;
    border: 1px solid rgba(255, 255, 255, 0.3);
    box-shadow: 0 4px 12px rgba(0, 0, 0, 0.05);
    font-family: 'Poppins', sans-serif;
}
.stChatMessage.user {
    background: rgba(237, 231, 246, 0.6);
}
.stChatMessage.assistant {
    background: rgba(243, 229, 245, 0.6);
}

.stChatInput > div > div > input {
    background: rgba(255, 255, 255, 0.5);
    backdrop-filter: blur(10px);
    border: 2px solid rgba(142, 36, 170, 0.3)!important;
    border-radius: 15px!important;
    padding: 0.8rem!important;
    font-family: 'Poppins', sans-serif;
}
.stChatInput > div > div > input:focus {
    border: 2px solid #8E24AA!important;
    box-shadow: 0 0 0 3px rgba(142, 36, 170, 0.1);
}

hr {
    margin: 2rem 0;
    border: none;
    height: 1px;
    background: linear-gradient(90deg, transparent, rgba(106, 27, 154, 0.3), transparent);
}
</style>
""", unsafe_allow_html=True)

# --- Logo/Header ---
try:
    st.image("logo.png", width=80)
except:
    st.markdown("<h2 style='text-align: center;'>💜</h2>", unsafe_allow_html=True)

# --- Title ---
st.markdown("<h1>SATHI</h1>", unsafe_allow_html=True)
st.markdown('<p class="subtitle">Your SPMVV Guide</p>', unsafe_allow_html=True)

# --- Chat State ---
if "messages" not in st.session_state:
    st.session_state.messages = []
    st.session_state.messages.append({
        "role": "assistant",
        "content": "Hi! I'm SATHI. Ask me about B.Tech cutoffs, hostel 6-share rooms, 6 PM rules, mess food, or placements. I'll tell you pros and cons honestly."
    })

hostel_list = "Gangothri, Godavari, Kinnera, Kalyani, Gowthami, Manjeera, Sravanthi, Swarnamukhi, Krishnaveni, Shabari"

def add_to_chat(user_msg, bot_msg):
    st.session_state.messages.append({"role": "user", "content": user_msg})
    st.session_state.messages.append({"role": "assistant", "content": bot_msg})

# --- Quick Action Buttons ---
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

# --- Quick Doubt Buttons ---
st.write("**Common doubts:**")
col1, col2, col3 = st.columns(3)
prompt = None

if col1.button("Hostel rules?"):
    prompt = "What are the strict hostel rules at SPMVV? Tell me pros and cons"
if col2.button("CSE cutoff?"):
    prompt = "What AP EAPCET rank needed for B.Tech CSE in SPMVV? Is it worth joining?"
if col3.button("Safe for girls?"):
    prompt = "How safe is SPMVV? What restrictions are there for students?"

# --- Chat Input ---
if prompt is None:
    prompt = st.chat_input("Ask SATHI...")

if prompt:
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    with st.chat_message("assistant"):
        with st.spinner("Checking..."):
            try:
                client = Groq(api_key=st.secrets["GROQ_API_KEY"])

                system_prompt = """You are SPMVV Doubts Bot SATHI. Answer questions from students/parents who want to join Sri Padmavati Mahila Visvavidyalayam. Give balanced pros AND cons.

SPMVV FACTS FOR PROSPECTIVE STUDENTS:

1. HOSTELS - Gangothri, Godavari, Kinnera, Kalyani, Gowthami, Manjeera, Sravanthi, Swarnamukhi, Krishnaveni, Shabari
PROS: Very safe with 24/7 security and wardens. Monthly fee system. Inside campus - 5min walk to classes. WiFi available.
CONS: 6-sharing rooms = very crowded, less privacy. STRICT 6:00 PM in-time - must return by 6 PM after outings or get warnings. Mess food is vegetarian only and becomes repetitive/boring after 1-2 months. Daily attendance taken. High security = restricted freedom. Hot water only at fixed times.

2. ADMISSIONS: B.Tech via AP EAPCET. CSE cutoff roughly 40k-60k rank for general, varies yearly. Fees ~50k/year + hostel monthly.
3. PLACEMENTS: TCS, Infosys, Wipro, Cognizant recruit. PRO: Training provided. CON: Avg 3-4.5 LPA, 6+ LPA rare. Need self-preparation.
4. RULES: 75% attendance strict. Dress code in some depts. 6 PM hostel curfew. 15km from Tirupati city.
5. CAMPUS: NAAC A+ grade. PRO: Safe, green, Spoorthy fest, library till 8pm. CON: Small town, no nightlife, only girls.

ANSWER STYLE:
- For doubts, give both sides: "Pro: X. Con: Y"
- Be direct about negatives: 6-share rooms, 6 PM rule, boring mess
- For cutoffs/fees: "Varies yearly. Check spmvv.ac.in or call 0877-2284592 for current data"
- Don't claim to be a student. Just give info.
- Keep answers under 150 words unless detailed info requested.
"""

                chat_completion = client.chat.completions.create(
                    messages=[
                        {"role": "system", "content": system_prompt},
                        *[{"role": m["role"], "content": m["content"]} for m in st.session_state.messages[-6:]]
                    ],
                    model="llama-3.1-8b-instant",
                    temperature=0.6,
                    max_tokens=700,
                )
                response = chat_completion.choices[0].message.content
                st.markdown(response)
                
            except Exception as e:
                response = "Error connecting to AI. For admissions call SPMVV: 0877-2284592 or check spmvv.ac.in"
                st.markdown(response)
    
    st.session_state.messages.append({"role": "assistant", "content": response})
    st.rerun()
