import streamlit as st
import PyPDF2
from io import BytesIO
import img2pdf

def merge_files(session_page):
    """
    This function merges multiple files into a single PDF file. It supports both PDF and image files.
    For image files, it first converts them into PDF format before merging.

    Args:
        session_page (dict): A dictionary containing the session data. It should have a key 'input_file_list' 
                             which is a list of files to be merged. The merged PDF is stored in the 'merged_pdf' key.

    Returns:
        None. The 'session_page' dictionary is updated in-place with the merged PDF.
    """
    # Display a spinner on the UI while the files are being merged
    with st.spinner('Merging files...'):
        # Create a PdfWriter object which will be used to write the merged PDF
        pdf_writer = PyPDF2.PdfWriter()

        # Loop through each file in the input file list
        for file in session_page['input_file_list']:
            # If the file is a PDF (either .pdf or .PDF extension), read it directly
            if file.name.endswith('.pdf') or file.name.endswith('.PDF'):
                pdf_reader = PyPDF2.PdfReader(file)
                # Add each page of the PDF to the PdfWriter object
                for page in range(len(pdf_reader.pages)):
                    pdf_writer.add_page(pdf_reader.pages[page])
            else:
                # If the file is not a PDF, assume it's an image and convert it to PDF
                image_pdf = img2pdf.convert(file.read())
                image_pdf = BytesIO(image_pdf)
                # Append the converted image PDF to the PdfWriter object
                pdf_writer.append(PyPDF2.PdfReader(image_pdf))

        # Create a BytesIO object to hold the merged PDF
        merged_pdf = BytesIO()
        # Write the merged PDF to the BytesIO object
        pdf_writer.write(merged_pdf)
        # Reset the pointer of the BytesIO object to the start
        merged_pdf.seek(0)

    # Store the merged PDF in the session data
    session_page['merged_pdf'] = merged_pdf
    # Update the session state with the new session data
    st.session_state['pdf_merger'] = session_page

def reset(session_page, page):
    """
    Function to reset the session state.
    """
    session_page = {}
    st.session_state[page] = session_page