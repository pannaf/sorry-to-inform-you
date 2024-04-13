import streamlit as st
from functions.functions import handle_configure_click

if "page" not in st.session_state:
    st.session_state.page = "configure_page"

def configure_page():
    st.markdown("## Submit Job Posting ⚡")
    interview_guide = ""

    job_description = st.text_area("Job description")
    st.divider()
    st.markdown("### Candidate info 💁")
    columns =  st.columns(2)
    candidate_name = columns[0].text_input("Candidate name")
    candidate_phone = columns[1].text_input("Phone number", placeholder=5105707879)
    if candidate_phone:
        if len(candidate_phone) != 10:
            st.error("Please enter a 10-digit phone number")
        else:
            try:
                candidate_phone = int(candidate_phone)
            except ValueError:
                st.error("Please enter a valid phone number")


    if st.button("Submit"):
        st.spinner("Submitting job description...")
        handle_configure_click()



    if not interview_guide == "":
        st.write(interview_guide)




def main():

    if st.session_state.page == "configure_page":
        configure_page()




if __name__ == "__main__":
    main()