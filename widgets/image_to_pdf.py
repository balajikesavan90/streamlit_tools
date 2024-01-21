import streamlit as st
import uuid

from utils.helpers import convert_images_to_pdf, reset

def render_image_to_pdf_widget(session_page):
    
    st.header(':blue[Convert Images To PDF]')

    # Check if 'uploader_key' is in the session state, if not, add it
    if 'uploader_key' not in session_page:
        session_page['uploader_key'] = uuid.uuid4()

    # File uploader for the PDF files
    session_page['image_list'] = st.file_uploader(
        label = 'The files will be merged in the order you upload them',  # Label of the file uploader
        type = ['png', 'jpg', 'jpeg'],  # Only accept images
        accept_multiple_files = True,  # Accept multiple files
        key = session_page['uploader_key'],  # Unique key for the file uploader
        disabled = ('output_pdf' in session_page)  # Disable the file uploader if 'merged_pdf' is in the session state
    )

    # Button to merge the PDF files
    st.button(
        label = 'Convert!',  # Label of the button
        on_click = convert_images_to_pdf,  # Function to call when the button is clicked
        args = [session_page],  # Arguments to pass to the function
        use_container_width = True,  # Use the full width of the container
        type ='primary',  # Type of the button
        # Disable the button if 'pdf_list' is empty or 'merged_pdf' is in the session state
        disabled = (session_page['image_list'] == [])|('output_pdf' in session_page)
    )

    if 'output_pdf' in session_page:
        st.download_button(
            label = ':green[Download PDF]',  # Label of the button
            use_container_width = True,  # Use the full width of the container
            data = session_page['output_pdf'],  # Data to download
            file_name = f"output_pdf.pdf",  # Filename of the downloaded file
            mime = 'application/pdf',  # MIME type of the downloaded file
            on_click = reset,  # Function to call when the button is clicked,
            args=[session_page, 'image_to_pdf']  # Arguments to pass to the function
        )
    
    st.session_state['image_to_pdf'] = session_page  # Update the session state