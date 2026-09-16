import streamlit as st

# Page configuration
st.set_page_config(
    page_title="LearnAssist Nigeria",
    page_icon="📚",
    layout="centered"
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

# Question input
question = st.text_area(
    "What would you like to learn?",
    placeholder="Example: Explain quadratic equations to me step by step."
)

# Ask button
if st.button("🤖 Ask LearnAssist"):
    if question.strip():
        st.success("Your question has been received!")
        
        st.info(
            f"Class: {class_level}\n\n"
            f"Subject: {subject}\n\n"
            f"Question: {question}"
        )
        
        st.write("🧠 AI explanation will appear here soon.")
    else:
        st.warning("Please enter a question first.")

st.divider()

st.caption("Built with ❤️ for Nigerian learners.")
