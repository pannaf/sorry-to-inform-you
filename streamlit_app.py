import streamlit as st
from functions.functions import handle_configure_click

if "page" not in st.session_state:
    st.session_state.page = "configure_page"

def configure_page():
    st.markdown("## Submit Job Posting ⚡")
    interview_guide = ""

    job_description = st.text_area("Job description")
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