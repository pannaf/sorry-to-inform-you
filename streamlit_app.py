import streamlit as st
from functions.functions import handle_configure_click

if "page" not in st.session_state:
    st.session_state.page = "configure_page"

def configure_page():

    if "button_state_disabled" not in st.session_state:
        st.session_state['button_state_disabled'] = True

    if "phone" not in st.session_state:
        st.session_state['phone'] = None

    if "candidate_name" not in st.session_state:
        st.session_state['candidate_name'] = None

    st.markdown("## Submit Job Posting ⚡")
    interview_guide = ""

    job_description = st.text_area("Job description")
    behavioral_requirements = st.text_area("Behavioral Requirements")
    st.divider()
    st.markdown("### Candidate info 💁")
    columns =  st.columns(2)
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
        st.session_state['button_state_disabled'] = False


    if st.button("Submit", disabled=st.session_state.button_state_disabled):
        st.spinner("Submitting job description...")
        handle_configure_click()



    if not interview_guide == "":
        st.write(interview_guide)




def main():

    if st.session_state.page == "configure_page":
        configure_page()





if __name__ == "__main__":
    main()