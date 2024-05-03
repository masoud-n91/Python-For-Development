import streamlit as st

def calculate_bmi(weight, height):
    return weight / ((height / 100) ** 2)

def bmi_category(bmi):
    if bmi < 18.5:
        return "Underweight"
    elif 18.5 <= bmi < 25:
        return "Normal weight"
    elif 25 <= bmi < 30:
        return "Overweight"
    elif 30 <= bmi < 40:
        return "Obesity"
    else:
        return "Extreme Obesity"


def show():
    st.title('Know your BMI')

    weight = st.number_input("Your weight in kg:", min_value=1.0)
    height = st.number_input("Your height in cm:", min_value=1.0)

    if st.button("Calculate"):
        if height > 2 and weight > 2:
            bmi = calculate_bmi(weight, height)
            category = bmi_category(bmi)
            image_path = f"images/{category}.png"

            st.write(f"Your BMI is {bmi:.2f},", f"and your status is: {category}")
            st.image(image_path)
        else:
            st.error("Please enter your height and weight corectly.")


if __name__ == "__main__":
    show()

