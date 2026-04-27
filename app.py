import streamlit as st
from agent.planner import plan
from agent.tools import get_topic_data, get_all_topics
from agent.formatter import format_output

# 🎨 UI Styling
st.markdown("""
    <style>
    body { background-color: #0e1117; }
    .stTextInput>div>div>input {
        background-color: #262730;
        color: white;
        border-radius: 10px;
    }
    .stButton>button {
        border-radius: 10px;
        padding: 10px 20px;
        background-color: #4CAF50;
        color: white;
        font-weight: bold;
    }
    </style>
""", unsafe_allow_html=True)

st.set_page_config(page_title="AI Study Assistant", layout="centered")

# Title
st.markdown("<h1 style='text-align: center;'>🧠 AI Study Assistant Agent</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center;'>Learn smarter with AI-powered notes & quizzes</p>", unsafe_allow_html=True)

# 🧠 Session State
if "topic" not in st.session_state:
    st.session_state.topic = ""
if "data" not in st.session_state:
    st.session_state.data = None

# Input
topic_input = st.text_input("Enter a topic:", value=st.session_state.topic)

# Generate button
if st.button("Generate Study Material"):
    st.session_state.topic = topic_input

    plan_data = plan(topic_input)
    data = get_topic_data(plan_data["topic"])

    if not data:
        st.session_state.data = None
    else:
        st.session_state.data = data

# 🔁 Render output (outside button!)
if st.session_state.topic:

    data = st.session_state.data

    if not data:
        st.error("❌ Topic not found.")
        st.write("Try:", ", ".join(get_all_topics()))
    else:
        st.success("📚 Study Material Generated")

        result = format_output(st.session_state.topic, data)
        st.code(result)

        st.subheader("🧠 Quiz")

        with st.form("quiz_form"):
            score = 0
            answers = []

            for i, q in enumerate(data["questions"]):
                ans = st.text_input(q, key=f"q{i}")
                answers.append(ans)

            submitted = st.form_submit_button("Submit Quiz")

            if submitted:
                for i in range(len(answers)):
                    if answers[i].lower().strip() == data["answers"][i]:
                        score += 1

                st.write(f"🎯 Score: {score}/{len(data['questions'])}")