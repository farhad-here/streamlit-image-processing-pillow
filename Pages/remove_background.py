from rembg import remove
import streamlit as st
from PIL import Image
import io
#upload file
file = st.file_uploader('Upload image here')
#remove bg
if file:
    img = Image.open(file)
    rm = remove(img)
    name = st.sidebar.text_input('Put a name for file')
    if name:
        buffer = io.BytesIO()
        rm.save(buffer, format="PNG")
        dw=st.sidebar.download_button(
            label="Download",
            data=buffer,  # download image from the in-memory buffer
            file_name=f"{name}.png",
            mime="image/png",
        )
        buffer.close()

