import streamlit as st
from pages import BMI_calculator, blur_image, counter


def main():
    st.title("Welcome to the my Web App")
    st.write("This is the home page. Choose a page from the sidebar to explore.")
    st.write("\t1- Do you want to know your BMI? Just click on BMI Calculator and fill the form.")
    st.write("\t2- Do you want to blur your image? Just click on Blur Image and upload your image.")
    st.write("\t3- Do you want to count? Just click on Counter and start counting.")
    st.write("")
    st.write("")

    st.write("If you want to know more about me, I am available on:")
    st.write("- LinkedIn: https://www.linkedin.com/in/m-navidi/")
    st.write("- Github: https://github.com/masoud-n91")
    st.write("")
    st.write("")
    st.write("")
    st.markdown("---")  # Add a separator
    st.write("Made by: Masoud Navidi - 2024")

if __name__ == "__main__":
    main()
