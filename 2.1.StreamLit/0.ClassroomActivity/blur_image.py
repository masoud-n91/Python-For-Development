import streamlit as st
from PIL import Image, ImageFilter

def show():
    st.title("Image Blur App")

    uploaded_file = st.file_uploader("Choose your image", type=['jpg', 'jpeg', 'png'])
    if uploaded_file is not None:
        image = Image.open(uploaded_file)
        st.image(image, caption='Uploaded Image', use_column_width=True)
        st.write("")
        st.write("Processed Image")

        blur_amount = st.slider("Select the amount of blur", min_value=1, max_value=99, value=5, step=2)

        blur_img = image.filter(ImageFilter.GaussianBlur(blur_amount))

        st.image(blur_img, caption='Blurred Image', use_column_width=True)

if __name__ == "__main__":
    show()
