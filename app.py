import streamlit as st

from widgets.merge_pdfs import render_merge_pdfs_widget

# Set the page configuration
st.set_page_config(
    page_title='Free PDF Merger',  # The title of the page
    page_icon=':page_facing_up:'  # The icon of the page
)

# Set the title of the page
st.title(':blue[Free PDF Merger]')

if 'pdf_merger' not in st.session_state:
    st.session_state['pdf_merger'] = {}
render_merge_pdfs_widget(st.session_state['pdf_merger'])