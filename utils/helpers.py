import streamlit as st
import PyPDF2
from io import BytesIO
import img2pdf

def merge_files(session_page):
    with st.spinner('Merging files...'):
        pdf_writer = PyPDF2.PdfWriter()

        for file in session_page['input_file_list']:
            if file.name.endswith('.pdf') or file.name.endswith('.PDF'):
                pdf_reader = PyPDF2.PdfReader(file)
                if pdf_reader.is_encrypted:
                    st.error("The file is password protected. Please upload a decrypted file.")
                    return
                for page in range(len(pdf_reader.pages)):
                    pdf_writer.add_page(pdf_reader.pages[page])
            else:
                image_pdf = img2pdf.convert(file.read())
                image_pdf = BytesIO(image_pdf)
                pdf_writer.append(PyPDF2.PdfReader(image_pdf))

        merged_pdf = BytesIO()
        pdf_writer.write(merged_pdf)
        merged_pdf.seek(0)

    session_page['merged_pdf'] = merged_pdf
    st.session_state['pdf_merger'] = session_page

def reset(session_page, page):
    """
    Function to reset the session state.
    """
    session_page = {}
    st.session_state[page] = session_page