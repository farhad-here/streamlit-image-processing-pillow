import streamlit as st
from streamlit_cropper import st_cropper
import streamlit as st
from PIL import Image
import io

st.markdown("# crop image")
st.sidebar.markdown("# crop image")


# Upload an image and set some options for demo purposes
img_file = st.sidebar.file_uploader(label='Upload a file', type=['png', 'jpg'])
box_color = st.sidebar.color_picker(label="Box Color", value='#0000FF')
aspect_choice = st.sidebar.radio(label="Aspect Ratio", options=["1:1", "16:9", "4:3", "2:3", "Free"])
aspect_dict = {
    "1:1": (1, 1),
    "16:9": (16, 9),
    "4:3": (4, 3),
    "2:3": (2, 3),
    "Free": None
}
aspect_ratio = aspect_dict[aspect_choice]

if img_file:
    img = Image.open(img_file)
    # Get a cropped image from the frontend
    cropped_img = st_cropper(img, box_color=box_color,
                                aspect_ratio=aspect_ratio)
    # Manipulate cropped image at will
    st.write("Preview")
    cropped_img.thumbnail((300,300))
    st.image(cropped_img)
    buffer = io.BytesIO()
    cropped_img.save(buffer,format='PNG')
    btn = st.sidebar.download_button(
                label="Download image",
                data=buffer,
                file_name=img_file.name,

            )
    buffer.close()