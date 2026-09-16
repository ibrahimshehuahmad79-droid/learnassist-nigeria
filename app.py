import streamlit as st
from google import genai

# -----------------------------
# PAGE CONFIGURATION
# -----------------------------
st.set_page_config(
    page_title="LearnAssist Nigeria",
    page_icon="📚",
    layout="centered"
)

# -----------------------------
# GEMINI CLIENT
# -----------------------------
client = genai.Client(
    api_key=st.secrets["GEMINI_API_KEY"]
)

# -----------------------------
# HEADER
# -----------------------------
st.title("📚 LearnAssist Nigeria")
st.subheader("Your AI study partner, built for Nigerian learners.")

st.write(
    "LearnAssist helps secondary-school students understand "
    "Mathematics through simple explanations, worked examples, "
    "practice questions, and personalised feedback."
)

st.divider()

# -----------------------------
# STUDENT SETTINGS
# -----------------------------
st.header("🎓 Start Learning")

class_level = st.selectbox(
    "Select your class",
    ["SS1", "SS2", "SS3"]
)

subject = st.selectbox(
    "Select your subject",
    ["Mathematics"]
)

# -----------------------------
# QUESTION
# -----------------------------
question = st.text_area(
    "What would you like to learn?",
    placeholder="Example: Explain quadratic equations to me step by step."
)

# -----------------------------
# ASK LEARNASSIST
# -----------------------------
if st.button("🤖 Ask LearnAssist"):

    if question.strip():

        prompt = f"""
You are LearnAssist Nigeria, an AI Mathematics tutor
for Nigerian secondary-school students.

Student class: {class_level}
Subject: {subject}

Student question:
{question}

Teach the student clearly and step by step.

Structure your response using these sections:

## 📖 Simple Explanation
Explain the concept using language suitable for the student's class.

## 🧮 Worked Example
Give one example and solve it step by step.

## 📝 Practice Question
Give ONE similar question for the student to solve.

## 💡 Learning Tip
Give one short useful tip.

Do not just provide answers.
Teach the student the method so they can solve similar problems.
"""

        with st.spinner("🧠 LearnAssist is preparing your lesson..."):

            try:
                response = client.models.generate_content(
                    model="gemini-3.8-flash",
                    contents=prompt
                )

                st.session_state["lesson"] = response.text

            except Exception:
                st.error(
                    "Sorry, something went wrong. "
                    "Please check your connection and try again."
                )

    else:
        st.warning("Please enter a question first.")


# -----------------------------
# DISPLAY LESSON
# -----------------------------
if "lesson" in st.session_state:

    st.divider()

    st.header("📚 Your LearnAssist Lesson")

    st.markdown(st.session_state["lesson"])

    # -----------------------------
    # STUDENT ANSWER
    # -----------------------------
    st.divider()

    st.header("✍️ Check My Answer")

    student_answer = st.text_area(
        "Enter your answer to the practice question:",
        placeholder="Type your answer here..."
    )

    if st.button("✅ Check My Answer"):

        if student_answer.strip():

            feedback_prompt = f"""
You are LearnAssist Nigeria, an AI Mathematics tutor.

Student class: {class_level}

Here is the lesson and practice question:

{st.session_state["lesson"]}

The student's answer is:

{student_answer}

Evaluate the student's answer.

Give feedback using these sections:

## 🎯 Result
Say whether the answer appears correct, partially correct, or incorrect.

## ✅ What You Did Well
Mention what the student did correctly.

## 🔎 What Needs Improvement
Explain any mistake clearly.

## 🧠 Correct Method
Show the correct method step by step if necessary.

## 💡 Tip
Give one short tip for improving on this type of question.

Be encouraging and educational.
Do not shame the student.
"""

            with st.spinner("🔍 Checking your answer..."):

                try:
                    feedback = client.models.generate_content(
                        model="gemini-3.8-flash",
                        contents=feedback_prompt
                    )

                    st.success("Feedback ready!")

                    st.markdown(feedback.text)

                except Exception:
                    st.error(
                        "Sorry, I couldn't check the answer right now."
                    )

        else:
            st.warning("Please enter your answer first.")


# -----------------------------
# FOOTER
# -----------------------------
st.divider()

st.caption("Built with ❤️ for Nigerian learners.")
