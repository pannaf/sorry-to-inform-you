from retell import Retell
import os
import streamlit as st
from functions.functions import handle_configure_click
from calls import place_call
from tune2 import InterviewAssistant


if "page" not in st.session_state:
    st.session_state.page = "configure_page"


def configure_page():
    if "button_state_disabled" not in st.session_state:
        st.session_state["button_state_disabled"] = True

    if "transcript_button" not in st.session_state:
        st.session_state["transcript_button"] = True

    if "phone" not in st.session_state:
        st.session_state["phone"] = None

    if "candidate_name" not in st.session_state:
        st.session_state["candidate_name"] = None

    if "call_id" not in st.session_state:
        st.session_state["call_id"] = None

    st.markdown("## Submit Job Posting ⚡")
    interview_guide = ""

    job_description = st.text_area(
        "Job description",
        value="""Senior Machine Learning Engineer Tune AI 
    Bengaluru, Karnataka, India 
    We are looking for a highly skilled and experienced ML Engineer to join our team. In this role, you will be responsible for designing, developing, and deploying ML models and algorithms to support our business operations. You will work closely with data scientists, software engineers, and other cross-functional teams to develop, test, and deploy ML models in production.

    Key Responsibilities:
    - Design, develop, and deploy ML models and algorithms to support business operations
    - Work with data scientists, software engineers, and other cross-functional teams to develop, test, and deploy ML models in production
    - Monitor and optimize ML model performance in production
    - Collaborate with data engineers to design and implement data pipelines and infrastructure for ML model training and deployment
    - Conduct research and experimentation to develop new ML algorithms and techniques
    - Test ML technologies and best practices, and share knowledge with the team""",
    )

    behavioral_requirements = st.text_area("Behavioral Requirements", value="curiosty, mentorship")
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
        st.session_state.call_id = place_call(f"+1{st.session_state.phone}", interview_questions)

    if st.session_state.call_id is not None:
        st.session_state.transcript_button = False

    if st.button("Get feedback", disabled=st.session_state.transcript_button):
        client = Retell(api_key=os.getenv("RETELL_API_KEY"))
        call = client.call.retrieve(st.session_state.call_id)
        print(call.agent_id)

        transcript = call.transcript
        print(transcript)
        st.write(transcript)

        assistant = InterviewAssistant()
        assessment = assistant.assess_call(transcript, job_description, behavioral_requirements)

        st.write(assessment)

        st.session_state.page = "results_page"

    if not interview_guide == "":
        st.write(interview_guide)


# feedback = {
#     "feedback": "The candidate struggled to provide concrete examples of successful upselling and handling difficult customer situations. They also admitted to having difficulty staying organized and engaging with customers proactively. The candidate demonstrated a lack of initiative in collaborative tasks and could benefit from improving their patience and understanding with customers.",
#     "recommendation": False,
#     "reason": "The candidate's lack of experience and skills in upselling, customer interaction, and teamwork are concerning for a retail position. They displayed limited enthusiasm for the job and a relatively low job fit score, indicating a potential mismatch for the role.",
#     "top relevant skills": ["Politeness", "Availability"],
#     "potential skill gaps": ["Upselling", "Customer Service", "Organization", "Teamwork", "Patience"],
#     "enthusiasm": 2,
#     "job fit": 2,
#     "communication": 3,
# }
#
#
# def results_page():
#     st.divider()
#     st.markdown("## Interview Results ⚡")
#     st.write("### Feedback")
#     st.write(feedback["feedback"])
#     st.write("### Recommendation")
#     st.write(feedback["recommendation"])
#     st.write("### Reason")
#     st.write(feedback["reason"])
#     st.write("### Top Relevant Skills")
#     st.write(feedback["top relevant skills"])
#     st.write("### Potential Skill Gaps")
#     st.write(feedback["potential skill gaps"])


def main():
    if st.session_state.page == "configure_page":
        configure_page()
    # if st.session_state.page == "results_page":
    #     results_page()


if __name__ == "__main__":
    main()
