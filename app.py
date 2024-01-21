import streamlit as st

from widgets.merge_pdfs import render_merge_pdfs_widget
from widgets.image_to_pdf import render_image_to_pdf_widget
from widgets.pdf_to_image import render_pdf_to_image_widget

# Set the page configuration
st.set_page_config(
    page_title='Free PDFs Tools',  # The title of the page
    page_icon=':page_facing_up:'  # The icon of the page
)

# Set the title of the page
st.title(':blue[Free PDF Tools]')

pdf_merge, image_to_pdf, pdf_to_image = st.tabs(['Merge PDFs', 'Image To PDF', 'PDF To Image'])

with pdf_merge:
    if 'pdf_merger' not in st.session_state:
        st.session_state['pdf_merger'] = {}
    render_merge_pdfs_widget(st.session_state['pdf_merger'])

with image_to_pdf:
    if 'image_to_pdf' not in st.session_state:
        st.session_state['image_to_pdf'] = {}
    render_image_to_pdf_widget(st.session_state['image_to_pdf'])

with pdf_to_image:
    if 'pdf_to_image' not in st.session_state:
        st.session_state['pdf_to_image'] = {}
    render_pdf_to_image_widget(st.session_state['pdf_to_image'])