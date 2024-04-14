import streamlit as st
from functions.functions import handle_configure_click


if "page" not in st.session_state:
    st.session_state.page = "configure_page"


def configure_page():
    if "button_state_disabled" not in st.session_state:
        st.session_state["button_state_disabled"] = True

    if "phone" not in st.session_state:
        st.session_state["phone"] = None

    if "candidate_name" not in st.session_state:
        st.session_state["candidate_name"] = None

    st.markdown("## Submit Job Posting ⚡")
    interview_guide = ""

    job_description = st.text_area("Job description")
    behavioral_requirements = st.text_area("Behavioral Requirements")
    st.divider()
    st.markdown("### Candidate info 💁")
    columns = st.columns(2)
    st.session_state.candidate_name = columns[0].text_input("Candidate name")
    candidate_phone = columns[1].text_input("Phone number", placeholder=5105707879)
    if candidate_phone:
        if len(candidate_phone) != 10:
            st.error("Please enter a 10-digit phone number")
        else:
            try:
                st.session_state.phone = int(candidate_phone)
            except ValueError:
                st.error("Please enter a valid phone number")

    if st.session_state.phone and st.session_state.candidate_name:
        st.session_state["button_state_disabled"] = False

    if st.button("Submit", disabled=st.session_state.button_state_disabled):
        st.spinner("Submitting job description...")
        interview_questions = handle_configure_click(job_description, behavioral_requirements)
        st.session_state.page = "results_page"

    if not interview_guide == "":
        st.write(interview_guide)


feedback = {
    "feedback": "The candidate struggled to provide concrete examples of successful upselling and handling difficult customer situations. They also admitted to having difficulty staying organized and engaging with customers proactively. The candidate demonstrated a lack of initiative in collaborative tasks and could benefit from improving their patience and understanding with customers.",
    "recommendation": False,
    "reason": "The candidate's lack of experience and skills in upselling, customer interaction, and teamwork are concerning for a retail position. They displayed limited enthusiasm for the job and a relatively low job fit score, indicating a potential mismatch for the role.",
    "top relevant skills": ["Politeness", "Availability"],
    "potential skill gaps": ["Upselling", "Customer Service", "Organization", "Teamwork", "Patience"],
    "enthusiasm": 2,
    "job fit": 2,
    "communication": 3,
}


def results_page():
    st.divider()
    st.markdown("## Interview Results ⚡")
    st.write("### Feedback")
    st.write(feedback["feedback"])
    st.write("### Recommendation")
    st.write(feedback["recommendation"])
    st.write("### Reason")
    st.write(feedback["reason"])
    st.write("### Top Relevant Skills")
    st.write(feedback["top relevant skills"])
    st.write("### Potential Skill Gaps")
    st.write(feedback["potential skill gaps"])


def main():
    if st.session_state.page == "configure_page":
        configure_page()
    if st.session_state.page == "results_page":
        results_page()


if __name__ == "__main__":
    main()
