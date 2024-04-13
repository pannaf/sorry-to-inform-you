import streamlit as st

from functions.functions import handle_configure_click

from pages.configure import show_page as configure_page
from pages.results import show_page as results_page

PAGES = {
    "configure_page": configure_page,
    "results_page": results_page
}

def main():
    st.markdown("## Submit Job Posting ⚡")
    interview_guide = ""

    job_description = st.text_area("Job description")
    if st.button("Submit"):
        st.spinner("Submitting job description...")
        handle_configure_click()

    if not interview_guide == "":
        st.write(interview_guide)



if __name__ == "__main__":
    main()