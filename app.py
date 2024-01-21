import streamlit as st

from widgets.merge_pdfs import render_merge_pdfs_widget

# Set the page configuration
st.set_page_config(
    page_title='Free PDFs Tools',  # The title of the page
    page_icon=':page_facing_up:'  # The icon of the page
)

# Set the title of the page
st.title(':blue[Free PDF Tools]')

pdf_merge, feature2, feature3 = st.tabs(['Merge PDFs', 'Feature 2', 'Feature 3'])

with pdf_merge:
    if 'pdf_merger' not in st.session_state:
        st.session_state['pdf_merger'] = {}
    render_merge_pdfs_widget(st.session_state['pdf_merger'])