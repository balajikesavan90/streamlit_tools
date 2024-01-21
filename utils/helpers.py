import streamlit as st
import PyPDF2
from io import BytesIO
import img2pdf
from pdf2image import convert_from_path
from PIL import Image

def merge_pdfs(session_page):
    """
    Function to merge the uploaded PDF files.

    Parameters:
    pdf_list (list): List of uploaded PDF files.
    """
    with st.spinner('Merging pdfs...'):
        pdf_writer = PyPDF2.PdfWriter()  # Create a PdfWriter object

        # Loop through the PDF files
        for pdf in session_page['pdf_list']:
            pdf_reader = PyPDF2.PdfReader(pdf)  # Create a PdfReader object
            # Loop through the pages in the PDF file
            for page in range(len(pdf_reader.pages)):
                pdf_writer.add_page(pdf_reader.pages[page])  # Add the page to the PdfWriter object

        merged_pdf = BytesIO()
        pdf_writer.write(merged_pdf)  # Write the pages to the BytesIO object
        merged_pdf.seek(0)  # Go to the start of the BytesIO object

    session_page['merged_pdf'] = merged_pdf  # Add the merged PDF to the session state
    st.session_state['pdf_merger'] = session_page  # Update the session state

def convert_images_to_pdf(session_page):

    with st.spinner('Converting images to pdf...'):
        image_list = session_page['image_list']
        pdf_bytes = img2pdf.convert([image.read() for image in image_list])
        pdf_bytes = BytesIO(pdf_bytes)
    
    session_page['output_pdf'] = pdf_bytes
    st.session_state['image_to_pdf'] = session_page

from pdf2image import convert_from_bytes

def convert_pdf_to_image(session_page):
    with st.spinner('Converting pdf to image...'):
        uploaded_file = session_page['pdf']
        images = []
        pdf_bytes = uploaded_file.getvalue()
        pages = convert_from_bytes(pdf_bytes)
        for page in pages:
            byte_arr = BytesIO()
            page.save(byte_arr, format='PNG')
            byte_arr = byte_arr.getvalue()
            images.append(byte_arr)
        session_page['output_images'] = images
    st.session_state['pdf_to_image'] = session_page

def reset(session_page, page):
    """
    Function to reset the session state.
    """
    session_page = {}
    st.session_state[page] = session_page