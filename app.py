import streamlit as st
from google import genai

# Page configuration
st.set_page_config(
    page_title="LearnAssist Nigeria",
    page_icon="📚",
    layout="centered"
)

# Gemini client
client = genai.Client(
    api_key=st.secrets["GEMINI_API_KEY"]
)

# Header
st.title("📚 LearnAssist Nigeria")
st.subheader("Your AI study partner, built for Nigerian learners.")

st.write(
    "LearnAssist helps secondary-school students understand "
    "Mathematics through simple explanations, worked examples, "
    "and practice questions."
)

st.divider()

# Student information
st.header("🎓 Start Learning")

class_level = st.selectbox(
    "Select your class",
    ["SS1", "SS2", "SS3"]
)

subject = st.selectbox(
    "Select your subject",
    ["Mathematics"]
)

question = st.text_area(
    "What would you like to learn?",
    placeholder="Example: Explain quadratic equations to me step by step."
)

# Ask AI
if st.button("🤖 Ask LearnAssist"):

    if question.strip():

        prompt = f"""
You are LearnAssist Nigeria, an AI Mathematics tutor
for Nigerian secondary-school students.

Student class: {class_level}
Subject: {subject}

Student question:
{question}

Teach the student in a clear and friendly way.

Your response must contain:

1. 📖 Simple Explanation
Explain the idea in language suitable for the student's class.

2. 🧮 Worked Example
Give one example and solve it step by step.

3. 📝 Practice Question
Give the student one similar question to try.

4. 💡 Learning Tip
Give one short tip to help the student remember the concept.

Do not simply give the final answer.
Teach the student so they understand the method.
"""

        with st.spinner("🧠 LearnAssist is thinking..."):

            try:
                response = client.models.generate_content(
                    model="gemini-3.8-flash",
                    contents=prompt
                )

                st.success("Here is your lesson!")

                st.markdown(response.text)

            except Exception as e:
                st.error(
                    "Sorry, something went wrong. "
                    "Please try again."
                )

    else:
        st.warning("Please enter a question first.")

st.divider()

st.caption("Built with ❤️ for Nigerian learners.")
