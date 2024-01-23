import streamlit as st
import uuid

from utils.helpers import merge_files, reset

def render_merge_pdfs_widget(session_page):

    st.header(':blue[Merge PDFs & Images into a Single PDF]')

    # Check if 'uploader_key' is in the session state, if not, add it
    if 'uploader_key' not in session_page:
        session_page['uploader_key'] = uuid.uuid4()

    # File uploader for the PDF files
    session_page['input_file_list'] = st.file_uploader(
        label = 'The files will be merged in the order you upload them', 
        type = ['pdf', 'png', 'jpeg', 'jpg'], 
        accept_multiple_files = True,  
        key = session_page['uploader_key'],
        disabled = ('merged_pdf' in session_page)# Disable the file uploader if 'merged_pdf' is in the session state
    )

    # Button to merge the PDF files
    st.button(
        label = 'Merge!',  
        on_click = merge_files,  
        args = [session_page],  
        use_container_width = True,  
        type ='primary',  
        # Disable the button if 'pdf_list' is empty or 'merged_pdf' is in the session state
        disabled = (len(session_page['input_file_list']) < 2)|('merged_pdf' in session_page)
    )

    # If 'merged_pdf' is in the session state
    if 'merged_pdf' in session_page:
        
        # Button to download the merged PDF
        st.download_button(
            label = ':green[Download merged pdf]',  
            use_container_width = True,  
            data = session_page['merged_pdf'],  
            file_name = f"merged_pdf.pdf",  
            mime = 'application/pdf',  
            on_click = reset,  
            args=[session_page, 'pdf_merger']  
        )

    st.session_state['pdf_merger'] = session_page  # Update the session state