import streamlit as st
from io import BytesIO
import img2pdf
import fitz

def merge_files(session_page):
    with st.spinner('Merging files...'):
        merged_pdf = fitz.open()  # create a new empty PDF

        for file in session_page['input_file_list']:
            if file.name.endswith('.pdf') or file.name.endswith('.PDF'):
                doc = fitz.open("pdf", BytesIO(file.getvalue()))
                if doc.needs_pass:
                    st.error("The file is password protected. Please upload a decrypted file.")
                    return
                else:
                    for page in doc:
                        merged_pdf.insert_pdf(doc, from_page=page.number, to_page=page.number)
            else:
                image_pdf = img2pdf.convert(file.read())
                image_pdf = BytesIO(image_pdf)
                image_doc = fitz.open("pdf", image_pdf.read())
                merged_pdf.insert_pdf(image_doc)

        output = BytesIO()
        merged_pdf.save(output, garbage=4, deflate=True)
        output.seek(0)

    session_page['merged_pdf'] = output
    st.session_state['pdf_merger'] = session_page

def reset(session_page, page):
    """
    Function to reset the session state.
    """
    session_page = {}
    st.session_state[page] = session_page