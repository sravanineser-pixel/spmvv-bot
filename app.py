import streamlit as st
from groq import Groq

st.set_page_config(
    page_title="SPMVV Doubts Bot",
    page_icon="🎓",
    layout="centered"
)

st.markdown("""
<style>
.stApp > header {visibility: hidden;}
    h1 {text-align: center; color: #8B0000; margin-bottom: 5px;}
   .subtitle {text-align: center; color: #666; margin-bottom: 25px;}
.stChatMessage {border-radius: 12px;}
</style>
""", unsafe_allow_html=True)

# Simple header
try:
    st.image("logo.png", width=80)
except:
    st.markdown("<h2 style='text-align: center;'>🎓</h2>", unsafe_allow_html=True)

st.markdown("<h1>SPMVV Doubts Bot</h1>", unsafe_allow_html=True)
st.markdown('<p class="subtitle">Ask anything about joining SPMVV - courses, hostels, rules, placements</p>', unsafe_allow_html=True)

if "messages" not in st.session_state:
    st.session_state.messages = []
    st.session_state.messages.append({
        "role": "assistant",
        "content": "Hi! I'm here to clear your doubts about SPMVV. Ask me about B.Tech cutoffs, hostel 6-share rooms, 6 PM rules, mess food, or placements. I'll tell you pros and cons honestly."
    })

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Quick doubt buttons
st.write("**Common doubts:**")
col1, col2, col3 = st.columns(3)
prompt = None

if col1.button("Hostel rules?"):
    prompt = "What are the strict hostel rules at SPMVV? Tell me pros and cons"
if col2.button("CSE cutoff?"):
    prompt = "What AP EAPCET rank needed for B.Tech CSE in SPMVV? Is it worth joining?"
if col3.button("Safe for girls?"):
    prompt = "How safe is SPMVV? What restrictions are there for students?"

if prompt is None:
    prompt = st.chat_input("Ask your SPMVV doubt...")

if prompt:
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    with st.chat_message("assistant"):
        with st.spinner("Checking..."):
            try:
                client = Groq(api_key=st.secrets["GROQ_API_KEY"])

                system_prompt = """You are SPMVV Doubts Bot. Answer questions from students/parents who want to join Sri Padmavati Mahila Visvavidyalayam. Give balanced pros AND cons.

SPMVV FACTS FOR PROSPECTIVE STUDENTS:

1. HOSTELS - Gangothri, Godavari, Kinnera, Kalyani, Gowthami, Manjeera, Sravanthi, Swarnamukhi
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
                response = "Error. For admissions call SPMVV: 0877-2284592"
                st.markdown(response)

    st.session_state.messages.append({"role": "assistant", "content": response})
    st.rerun()