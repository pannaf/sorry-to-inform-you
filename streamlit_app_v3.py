import os
import streamlit as st
from retell import Retell
from functions.functions import handle_configure_click
from calls import place_call
from tune2 import InterviewAssistant
import re


def initialize_state():
    """Initialize session state variables if they don't exist."""
    state_defaults = {
        "button_state_disabled": True,
        "phone": None,
        "candidate_name": None,
        "call_id": None,
        "call_placed": False,
        "feedback_fetched": False,
    }
    for key, default in state_defaults.items():
        if key not in st.session_state:
            st.session_state[key] = default


def configure_page():
    """Display the job posting configuration page."""
    initialize_state()

    st.markdown("## Submit Job Posting ⚡")
    job_description = st.text_area(
        "Job description",
        key="job_desc",
        value="""Senior Machine Learning Engineer Tune AI 
Bengaluru, Karnataka, India 
We are looking for a highly skilled and experienced ML Engineer to join our team. In this role, you will be responsible for designing, developing, and deploying ML models and algorithms to support our business operations... [trimmed for brevity]""",
    )

    behavioral_requirements = st.text_area("Behavioral Requirements", value="curiosity, mentorship")
    st.divider()
    st.markdown("### Candidate info 💁")

    columns = st.columns(2)
    st.session_state.candidate_name = columns[0].text_input("Candidate name")
    candidate_phone = columns[1].text_input("Phone number", placeholder="5105707879")

    if candidate_phone:
        if len(candidate_phone) == 10 and candidate_phone.isdigit():
            st.session_state.phone = int(candidate_phone)
            st.session_state.button_state_disabled = False
        else:
            st.error("Please enter a 10-digit phone number")

    if st.button("Submit", disabled=st.session_state.button_state_disabled):
        st.spinner("Submitting job description...")
        interview_questions = handle_configure_click(job_description, behavioral_requirements)
        st.session_state.call_id = place_call(f"+1{st.session_state.phone}", interview_questions, job_description=job_description)
        st.session_state.call_placed = bool(st.session_state.call_id)

    # st.button(
    #     "Get feedback",
    #     on_click=fetch_feedback,
    #     args=[job_description, behavioral_requirements],
    #     disabled=not st.session_state.call_placed,
    # )
    # if st.session_state.call_placed:
    #     st.button(
    #         "Get feedback",
    #         on_click=fetch_feedback,
    #         args=[job_description, behavioral_requirements],
    #         disabled=not st.session_state.call_placed,
    #     )
    feedback_button = st.empty()
    feedback_placeholder = st.empty()
    transcript_placeholder = st.empty()

    if st.session_state.call_placed:
        feedback_button.button(
            "Get feedback",
            on_click=lambda: fetch_feedback(job_description, behavioral_requirements, feedback_placeholder, transcript_placeholder),
            help="Click to retrieve the feedback based on the interview call. Ensure the call was completed successfully before clicking.",
        )


def format_transcript(transcript_text):
    # Regular expression to find patterns like "Name:"
    speakers = re.findall(r"\b[A-Z][a-z]*:", transcript_text)
    formatted_text = transcript_text

    # Replace each found speaker with Markdown formatted speaker
    for speaker in set(speakers):  # Use set to avoid duplicating replacements for the same speaker name
        # Add bold and newline for each speaker change
        formatted_text = formatted_text.replace(speaker, f"\n\n**{speaker[:-1]}:** ")

    # Handle the first line not starting with a newline (if applicable)
    if not formatted_text.startswith("\n"):
        formatted_text = "**Start of Transcript:** " + formatted_text

    return formatted_text


def display_transcript(transcript_text, transcript_placeholder):
    formatted_text = format_transcript(transcript_text)
    with transcript_placeholder.expander("View Transcript"):
        st.markdown(formatted_text, unsafe_allow_html=True)


def fetch_feedback(job_description, behavioral_requirements, feedback_placeholder, transcript_placeholder):
    """Fetch and display feedback for the interview call."""
    st.spinner("Fetching feedback...")
    client = Retell(api_key=os.getenv("RETELL_API_KEY"))
    call = client.call.retrieve(st.session_state.call_id)
    transcript = call.transcript
    if transcript is not None:
        display_transcript(transcript, transcript_placeholder)

    assistant = InterviewAssistant()
    assessment = assistant.assess_call(transcript, job_description, behavioral_requirements)
    feedback_placeholder.write(assessment)

    st.session_state.feedback_fetched = True


def main():
    configure_page()
    # Additional pages or logic can be placed here if needed.


if __name__ == "__main__":
    main()
