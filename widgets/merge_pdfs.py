import streamlit as st
import uuid

from utils.helpers import merge_pdfs, reset

def render_merge_pdfs_widget(session_page):

    st.header(':blue[Merge PDFs]')

    # Check if 'uploader_key' is in the session state, if not, add it
    if 'uploader_key' not in session_page:
        session_page['uploader_key'] = uuid.uuid4()

    # File uploader for the PDF files
    session_page['pdf_list'] = st.file_uploader(
        label = 'The files will be merged in the order you upload them',  # Label of the file uploader
        type = ['pdf'],  # Only accept PDF files
        accept_multiple_files = True,  # Accept multiple files
        key = session_page['uploader_key'],  # Unique key for the file uploader
        disabled = ('merged_pdf' in session_page)  # Disable the file uploader if 'merged_pdf' is in the session state
    )

    # Button to merge the PDF files
    st.button(
        label = 'Merge!',  # Label of the button
        on_click = merge_pdfs,  # Function to call when the button is clicked
        args = [session_page],  # Arguments to pass to the function
        use_container_width = True,  # Use the full width of the container
        type ='primary',  # Type of the button
        # Disable the button if 'pdf_list' is empty or 'merged_pdf' is in the session state
        disabled = (len(session_page['pdf_list']) < 2)|('merged_pdf' in session_page)
    )

    # If 'merged_pdf' is in the session state
    if 'merged_pdf' in session_page:
        
        # Button to download the merged PDF
        st.download_button(
            label = ':green[Download merged pdf]',  # Label of the button
            use_container_width = True,  # Use the full width of the container
            data = session_page['merged_pdf'],  # Data to download
            file_name = f"merged_pdf.pdf",  # Filename of the downloaded file
            mime = 'application/pdf',  # MIME type of the downloaded file
            on_click = reset,  # Function to call when the button is clicked,
            args=[session_page, 'pdf_merger']  # Arguments to pass to the function
        )

    st.session_state['pdf_merger'] = session_page  # Update the session state