import streamlit as st

PAGES = {
    "Page 1": page_one,
    "Page 2": page_two
}

def main():
    st.sidebar.title('Navigation')
    selection = st.sidebar.radio("Go to", list(PAGES.keys()))
    page = PAGES[selection]
    page()

if __name__ == "__main__":
    main()