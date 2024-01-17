# PDF Merger Web Application

This is a simple web application that allows users to merge multiple PDF files into one. It's built using the Streamlit library in Python, which makes it easy to create beautiful, interactive web applications.

## Features

- Upload multiple PDF files at once
- Merge uploaded PDF files into a single PDF
- Download the merged PDF file with a custom name

## How to Use

1. Upload your PDF files using the file uploader. The uploader accepts multiple files at once, and only PDF files are allowed.
2. Click the 'Merge!' button to merge the uploaded PDF files. The button is disabled until you upload at least one PDF file.
3. After the PDF files are merged, you can name your merged PDF file in the text input field.
4. Click the 'Download' button to download your merged PDF file.

## Dependencies

- Streamlit
- PyPDF2
- io
- uuid

## Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.