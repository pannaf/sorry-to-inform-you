import streamlit as st
from functions.functions import handle_configure_click
from retell import Retell

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

    # Input for HR interview content based on job description
    interview_content = st.text_area("Interview Content", value=job_description)
    
    # Add a button for making the API call with LLM
    api_key = "8645408a-d062-47c4-a0ae-97601722639b"
    phone_number = st.text_area("Phone Number")
    if st.button("Make API Call with LLM"):
        with st.spinner("Creating LLM based on job description..."):
            # Initialize Retell client and create an LLM based on the job description
            client = Retell(api_key=api_key)
            llm = client.llm.create(description=job_description)  # Assuming the create method accepts a description parameter
            st.success(f"LLM Created! LLM ID: {llm.llm_id}")
            
            # Generate interview script based on the LLM (this step is assumed and needs actual implementation)
            # For demonstration, we'll just use the interview_content directly
            interview_script = interview_content  # This should ideally be generated based on the LLM
            
            with st.spinner("Making API call..."):
                call = client.call.create(
                    from_number="+14158910214",
                    to_number=phone_number,
                    script=interview_script  # Assuming the Retell API can accept a script parameter
                )
                st.success(f"API Call Successful! Agent ID: {call.agent_id}")

def main():
    if st.session_state.page == "configure_page":
        configure_page()

if __name__ == "__main__":
    main()