import streamlit as st
import streamlit_image_coordinates
import numpy as np
from PIL import Image 

st.markdown("# coordinate image")
st.sidebar.markdown("# coordinate image")
img_file = st.sidebar.file_uploader(label='Upload a file', type=['png', 'jpg'])

if img_file:
    nnumpy = np.asarray(Image.open(img_file))
    value = streamlit_image_coordinates.streamlit_image_coordinates(nnumpy)
    if value:
        st.write('coordinate x =>',value['x'])
        st.write('coordinate y =>',value['y'])
