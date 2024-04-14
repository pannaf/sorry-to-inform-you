import streamlit as st
from tune2 import InterviewAssistant


def handle_configure_click(job_description, behavioral_requirements):
    assistant = InterviewAssistant()

    with st.spinner("Getting questions for interviewer...."):
        questions = assistant.get_questions(job_description, behavioral_requirements)
        st.write("Generated Questions:", questions)

    # assessment = assistant.assess_call(call_transcript, job_description, behavior_characteristics)

    # print("Generated Questions:", questions)
    # print("Call Assessment:", assessment)
