import tensorflow as tf
import streamlit as st
import pandas as pd
import numpy as np
st.title('Technocrats Fashion Arena ')
st.subheader("Upload your image and get recommendations")

# Create a file uploader widget
uploaded_file = st.file_uploader("Choose a file")

# Check if a file was uploaded
if uploaded_file is not None:
    # Check if the uploaded file is an image
    if uploaded_file.type.startswith('image'):
        # Display the image
        st.image(uploaded_file, caption='Uploaded Image')
    # If the uploaded file is not an image, assume it's a document
    else:
        # Display the file name and size
        file_details = {"FileName":uploaded_file.name,"FileType":uploaded_file.type,"FileSize":uploaded_file.size}
        st.write(file_details)
        
        # Read and display the file content
        file_content = uploaded_file.read()
        st.write(file_content)
