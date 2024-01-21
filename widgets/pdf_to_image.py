import streamlit as st
import uuid

from utils.helpers import convert_pdf_to_image, reset

def render_pdf_to_image_widget(session_page):
    
    st.header(':blue[Convert PDF To Image]')

    # Check if 'uploader_key' is in the session state, if not, add it
    if 'uploader_key' not in session_page:
        session_page['uploader_key'] = uuid.uuid4()

    # File uploader for the PDF files
    session_page['pdf'] = st.file_uploader(
        label = 'The PDFs will be merged in the order you upload them',  # Label of the file uploader
        type = ['pdf'],  # Only accept PDFs
        accept_multiple_files = False,  # Do not accept multiple files
        key = session_page['uploader_key'],  # Unique key for the file uploader
        disabled = ('output_images' in session_page)  # Disable the file uploader if 'merged_pdf' is in the session state
    )

    # Button to merge the PDF files
    st.button(
        label = 'Convert!',  # Label of the button
        on_click = convert_pdf_to_image,  # Function to call when the button is clicked
        args = [session_page],  # Arguments to pass to the function
        use_container_width = True,  # Use the full width of the container
        type ='primary',  # Type of the button
        key='convert_pdf_to_image',  # Unique key for the button
        # Disable the button if 'pdf_list' is empty or 'merged_pdf' is in the session state
        disabled = (session_page['pdf'] == None)|('output_images' in session_page)
    )

    if 'output_images' in session_page:
        st.download_button(
            label = ':green[Download Images]',  # Label of the button
            use_container_width = True,  # Use the full width of the container
            data = session_page['output_images'],  # Data to download
            file_name = f"output_images.zip",  # Filename of the downloaded file
            mime = 'application/zip',  # MIME type of the downloaded file
            on_click = reset,  # Function to call when the button is clicked,
            args=[session_page, 'pdf_to_image']  # Arguments to pass to the function
        )
    
    st.session_state['pdf_to_image'] = session_page  # Update the session state

    st.sidebar.write(st.session_state)