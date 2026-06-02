
import streamlit as st
import joblib
import sys

sys.path.append("src")

from resolution_engine import get_resolution
from severity_engine import get_severity
from src.banking_faq import FAQS
from src.pdf_generator import generate_pdf

# ----------------------------------
# PAGE CONFIG
# ----------------------------------

st.set_page_config(
    page_title="FinGuard AI",
    page_icon="🏦",
    layout="wide"
)

# ----------------------------------
# LOAD MODEL
# ----------------------------------

model = joblib.load("complaint_model.pkl")
vectorizer = joblib.load("vectorizer.pkl")

# ----------------------------------
# HEADER
# ----------------------------------

st.title("🏦 FinGuard AI")
st.subheader(
    "Smart Banking Assistant & Complaint Resolution Platform"
)

# ----------------------------------
# CLEAR CHAT
# ----------------------------------

if st.button("🗑 Clear Chat"):
    st.session_state.messages = []
    st.rerun()

# ----------------------------------
# CHAT HISTORY
# ----------------------------------

if "messages" not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:

    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# ----------------------------------
# CHAT INPUT
# ----------------------------------

prompt = st.chat_input(
    "Ask a banking question or describe a complaint..."
)

if prompt:

    st.session_state.messages.append(
        {
            "role": "user",
            "content": prompt
        }
    )

    with st.chat_message("user"):
        st.markdown(prompt)

    query = prompt.lower()

    faq_answer = None

    question_words = [
        "what is",
        "what are",
        "define",
        "explain",
        "meaning of",
        "tell me about",
        "how does",
        "how do",
        "can you explain"
    ]

    complaint_words = [
        "charged",
        "rejected",
        "denied",
        "failed",
        "problem",
        "issue",
        "fraud",
        "stolen",
        "unauthorized",
        "harassment",
        "delay",
        "delayed",
        "dispute",
        "blocked",
        "threat",
        "threatening",
        "application",
        "declined",
        "not working"
    ]

    is_question = any(
        phrase in query
        for phrase in question_words
    )

    is_complaint = any(
        word in query
        for word in complaint_words
    )

    # ----------------------------------
    # FAQ MODE
    # ----------------------------------

    if is_question and not is_complaint:

        for keyword, answer in FAQS.items():

            if keyword in query:

                faq_answer = answer
                break

    if faq_answer:

        response = f"""
### 📚 Banking Information

{faq_answer}
"""

        with st.chat_message("assistant"):
            st.markdown(response)

        st.session_state.messages.append(
            {
                "role": "assistant",
                "content": response
            }
        )

    else:

        complaint_vector = vectorizer.transform(
            [prompt]
        )

        probabilities = model.predict_proba(
            complaint_vector
        )[0]

        classes = model.classes_

        top_indices = probabilities.argsort()[-3:][::-1]

        top_predictions = [
            (
                classes[i],
                probabilities[i] * 100
            )
            for i in top_indices
        ]

        prediction = top_predictions[0][0]
        confidence = top_predictions[0][1]

        severity = get_severity(prompt)

        resolution = get_resolution(
            prediction
        )

        pdf_path = generate_pdf(
            prediction,
            confidence,
            severity,
            resolution
        )

        response = f"""
### 📌 Complaint Analysis

**Predicted Category:** {prediction}

**Confidence Score:** {confidence:.2f}%

**Severity Level:** {severity}

### 🏆 Top 3 Predictions

1. {top_predictions[0][0]} ({top_predictions[0][1]:.2f}%)

2. {top_predictions[1][0]} ({top_predictions[1][1]:.2f}%)

3. {top_predictions[2][0]} ({top_predictions[2][1]:.2f}%)

### ✅ Recommended Resolution

{resolution}
"""

        with st.chat_message("assistant"):

            st.markdown(response)

            with open(pdf_path, "rb") as file:

                st.download_button(
                    label="📄 Download Complaint Report",
                    data=file,
                    file_name="FinGuard_Report.pdf",
                    mime="application/pdf"
                )

        st.session_state.messages.append(
            {
                "role": "assistant",
                "content": response
            }
        )

