import streamlit as st
import PyPDF2
from io import BytesIO
import uuid

# Set the page configuration
st.set_page_config(
    page_title='Merge PDFs',  # The title of the page
    page_icon=':page_facing_up:'  # The icon of the page
)

# Set the title of the page
st.title(':blue[Free PDF Merger]')

# Check if 'uploader_key' is in the session state, if not, add it
if 'uploader_key' not in st.session_state:
    st.session_state.uploader_key = uuid.uuid4()

# File uploader for the PDF files
st.session_state.pdf_list = st.file_uploader(
    label = 'The files will be merged in the order you upload them',  # Label of the file uploader
    type = ['pdf'],  # Only accept PDF files
    accept_multiple_files = True,  # Accept multiple files
    key = st.session_state.uploader_key,  # Unique key for the file uploader
    disabled = ('merged_pdf' in st.session_state)  # Disable the file uploader if 'merged_pdf' is in the session state
)

def merge_pdfs(pdf_list):
    """
    Function to merge the uploaded PDF files.

    Parameters:
    pdf_list (list): List of uploaded PDF files.
    """
    with st.spinner('Merging pdfs...'):
        pdf_writer = PyPDF2.PdfWriter()  # Create a PdfWriter object

        # Loop through the PDF files
        for pdf in pdf_list:
            pdf_reader = PyPDF2.PdfReader(pdf)  # Create a PdfReader object
            # Loop through the pages in the PDF file
            for page in range(len(pdf_reader.pages)):
                pdf_writer.add_page(pdf_reader.pages[page])  # Add the page to the PdfWriter object

        merged_pdf = BytesIO()
        pdf_writer.write(merged_pdf)  # Write the pages to the BytesIO object
        merged_pdf.seek(0)  # Go to the start of the BytesIO object

    st.session_state.merged_pdf = merged_pdf  # Add the merged PDF to the session state

def reset():
    """
    Function to reset the session state.
    """
    # Remove 'merged_pdf', 'pdf_list', and 'filename' from the session state
    st.session_state.pop('merged_pdf', None)
    st.session_state.pop('pdf_list', None)
    st.session_state.pop('filename', None)
    # Reset the 'uploader_key'
    st.session_state.uploader_key = uuid.uuid4()

# Button to merge the PDF files
st.button(
    label = 'Merge!',  # Label of the button
    on_click = merge_pdfs,  # Function to call when the button is clicked
    args = (st.session_state.pdf_list,),  # Arguments to pass to the function
    use_container_width = True,  # Use the full width of the container
    type ='primary',  # Type of the button
    # Disable the button if 'pdf_list' is empty or 'merged_pdf' is in the session state
    disabled = (st.session_state.pdf_list == [])|('merged_pdf' in st.session_state)
)

# If 'merged_pdf' is in the session state
if 'merged_pdf' in st.session_state:
    
    # Check if 'filename' is in the session state, if not, add it
    if 'filename' not in st.session_state:
        st.session_state.filename = 'merged_pdf'

    # Text input for the filename of the merged PDF
    st.session_state.filename = st.text_input(
        label = 'What do you want to name your merged pdf?',  # Label of the text input
        value = st.session_state.filename,  # Default value of the text input
        max_chars = 100  # Maximum number of characters
        )

    # Button to download the merged PDF
    st.download_button(
        label = ':green[Download merged pdf]',  # Label of the button
        use_container_width = True,  # Use the full width of the container
        data = st.session_state.merged_pdf,  # Data to download
        file_name = f"{st.session_state.filename}.pdf",  # Filename of the downloaded file
        mime = 'application/pdf',  # MIME type of the downloaded file
        on_click = reset  # Function to call when the button is clicked
    )