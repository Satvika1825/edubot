import streamlit as st
import asyncio
from firebase_setup import db
from firebase_auth import auth  # Firebase Auth
from agents.motivation_agent import MotivationAgent
from agents.subject_agent import SubjectAgent
from agents.quiz_agent import QuizAgent
from agents.progress_agent import ProgressAgent
from agents.doubt_solver_agent import DoubtSolverAgent
from agents.orchestra_agent import OrchestraAgent

from input_model import AgentInput
from google_adk_integration import GoogleADKAgent
# Page config
st.set_page_config(
    page_title="EduBot Tutor 🤖📚",
    page_icon="🧠",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ----------- Custom Styles -------------
st.markdown("""
    <style>
        .stButton>button {
            background-color: #e75480;
            color: white;
            font-weight: 600;
            border-radius: 8px;
        }
        .response-box {
            background-color: #fff9db;
            border-left: 8px solid #f9c74f;
            padding: 20px;
            border-radius: 10px;
            margin-top: 20px;
            color: #333;
            font-size: 18px;
            box-shadow: 0 4px 8px rgba(0,0,0,0.1);
        }
        footer {visibility: hidden;}
    </style>
""", unsafe_allow_html=True)

# ----------- Login / Signup -------------
if "user" not in st.session_state:
    st.session_state.user = None

if not st.session_state.user:
    st.title("🔐 EduBot Login / Signup")
    choice = st.radio("Login or Signup?", ["Login", "Signup"])
    email = st.text_input("Email")
    password = st.text_input("Password", type="password")

    if st.button("Submit"):
        try:
            if choice == "Signup":
                user = auth.create_user_with_email_and_password(email, password)
                st.success("✅ Signed up successfully! Please log in.")
            else:
                user = auth.sign_in_with_email_and_password(email, password)
                st.session_state.user = user
                st.success("✅ Logged in successfully!")
                st.rerun()
        except Exception as e:
            st.error("❌ Authentication failed. Try again.")
    st.stop()

# ---------- EduBot Main UI --------------
st.markdown("<h1 style='text-align: center; color: #4CAF50;'>Welcome to EduBot 🧠</h1>", unsafe_allow_html=True)
st.markdown("<h3 style='text-align: center;'>Your Smart AI Study Assistant</h3>", unsafe_allow_html=True)
st.markdown("---")

st.sidebar.header("🎯 Choose Agent & Input")
agent_type = st.sidebar.selectbox(
    "🤖 Select Agent",
    [
        "Motivation Agent",
        "Subject Agent",
        "Quiz Agent",
        "Progress Agent",
        "Doubt Solver Agent",
        "Orchestra Agent"
    ]
)

# 🔽 Dropdown UI for subject/topic (used for SubjectAgent only)
subjects_map = {
    "Math": ["Algebra", "Calculus", "Geometry"],
    "Science": ["Photosynthesis", "Gravity", "Atom"],
    "English": ["Noun", "Verb", "Adjective"],
    "Data Science": ["Machine Learning", "Data Mining", "Data Visualization"],
    "Programming": ["Python", "C", "Java"],
}

if agent_type == "Subject Agent":
    subject = st.sidebar.selectbox("📘 Select Subject", list(subjects_map.keys()))
    topic = st.sidebar.selectbox("📝 Select Topic", subjects_map.get(subject, []))
else:
    subject = st.sidebar.text_input("📘 Subject", "")
    topic = st.sidebar.text_input("📝 Topic", "")

doubt = st.sidebar.text_input("❓ Doubt (if any)", "")

# ---------- Firestore Save -------------
def save_user_input(subject, topic, response):
    db.collection("user_queries").add({
        "email": st.session_state.user['email'],
        "subject": subject,
        "topic": topic,
        "response": response
    })

# ---------- Agent Selector -------------
def load_agent(agent_type):
    if agent_type == "Motivation Agent":
        return MotivationAgent()
    elif agent_type == "Subject Agent":
        return SubjectAgent()
    elif agent_type == "Quiz Agent":
        return QuizAgent()
    elif agent_type == "Progress Agent":
        return ProgressAgent()
    elif agent_type == "Doubt Solver Agent":
        return DoubtSolverAgent()
    elif agent_type == "Orchestra Agent":
        return OrchestraAgent()
    return None

# ---------- Async Handler -------------
async def get_agent_response(agent, input_data):
    responses = []
    async for item in agent.run_async(input_data):
        responses.append(item)
    return responses

# ---------- Run Agent Button ----------
if st.sidebar.button("✨ Run Agent"):
    agent = load_agent(agent_type)
    input_data = AgentInput(subject=subject, topic=topic, doubt=doubt)
    with st.spinner("Thinking... 💭"):
        responses = asyncio.run(get_agent_response(agent, input_data))
    for response in responses:
        message = response.get("formatted_message") or response.get("message", "No message returned.")
        st.markdown(f"<div class='response-box'>💡 <strong>EduBot says:</strong><br><br>{message}</div>", unsafe_allow_html=True)
        save_user_input(subject, topic, message)

# ---------- Logout Button -------------
if st.sidebar.button("🔓 Logout"):
    st.session_state.user = None
    st.rerun()

# ---------- Footer -------------
st.markdown("---")
st.markdown(
    "<p style='text-align: center; font-size: 13px;'>© 2025 EduBot AI. Built with ❤️ using Python & Streamlit.</p>",
    unsafe_allow_html=True
)
