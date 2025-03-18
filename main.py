import streamlit as st
import io as BytesIO

# Page configuration
st.set_page_config(
    page_title="Unit Convertor created by Amna",
    page_icon="🧊",
    layout="centered",
    initial_sidebar_state="expanded"
)

# Custom CSS Styling
st.markdown("""
    <style>
        .stApp {
            background-color: #2e2e2e; /* Dark background */
            color: #ffffff; /* White text */
        }

        h1, h3 {
            text-align: center;
        }

        .main-title {
            color: #00b4d8;
            font-size: 42px;
            margin-top: 10px;
        }

        .sub-title {
            color: #90e0ef;
            font-size: 24px;
            margin-bottom: 30px;
        }

        .result-box {
            background-color: #d4edda;
            padding: 16px;
            border-radius: 10px;
            color: #155724;
            font-weight: bold;
            font-size: 20px;
            text-align: center;
            border: 1px solid #c3e6cb;
            margin-top: 20px;
        }

        .success-msg {
            color: lightgreen;
            text-align: center;
            font-size: 20px;
            margin-top: 15px;
        }

        .error-msg {
            color: #ff4d4d;
            text-align: center;
            font-size: 18px;
        }

        .stButton > button {
            background-color: #4CAF50;
            color: white;
            border: 2px solid #4CAF50;
            padding: 10px 24px;
            border-radius: 8px;
            font-size: 16px;
            margin-top: 15px;
            cursor: pointer;
        }

        .stButton > button:hover {
            background-color: #45a049;
        }
    </style>
""", unsafe_allow_html=True)

# Title Section
st.markdown('<h1 class="main-title">🌐 Unit Convertor</h1>', unsafe_allow_html=True)
st.markdown('<h3 class="sub-title">Converts Length, Weight, Temperature & Time</h3>', unsafe_allow_html=True)
st.write("***📌 Welcome to the Unit Convertor App. Select a category and enter your value to convert in real time.***")

# Category Selection
category = st.selectbox("Select a Category", ["Length", "Weight", "Temperature", "Time"])

# Unit Conversion Function
def Convert_Units(category, value, unit):
    if category == "Length":
        if unit == "Kilometers to Miles":
            return value * 0.621371
        elif unit == "Miles to Kilometers":
            return value * 1.60934
        elif unit == "Meters to Feet":
            return value * 3.28084
        elif unit == "Feet to Meters":
            return value * 0.3048
        elif unit == "Centimeters to Inches":
            return value * 0.393701
        elif unit == "Inches to Centimeters":
            return value * 2.54

    elif category == "Weight":
        if unit == "Kilograms to Pounds":
            return value * 2.20462
        elif unit == "Pounds to Kilograms":
            return value * 0.453592
        elif unit == "Grams to Ounces":
            return value * 0.035274
        elif unit == "Ounces to Grams":
            return value * 28.3495

    elif category == "Temperature":
        if unit == "Celsius to Fahrenheit":
            return (value * 9 / 5) + 32
        elif unit == "Fahrenheit to Celsius":
            return (value - 32) * 5 / 9

    elif category == "Time":
        if unit == "Seconds to Minutes":
            return value / 60
        elif unit == "Minutes to Seconds":
            return value * 60
        elif unit == "Minutes to Hours":
            return value / 60
        elif unit == "Hours to Minutes":
            return value * 60
        elif unit == "Hours to Days":
            return value / 24
        elif unit == "Days to Hours":
            return value * 24
    return None

# Unit Selection
if category == "Length":
    unit = st.selectbox("Select Conversion", ["Kilometers to Miles", "Miles to Kilometers", "Meters to Feet", "Feet to Meters", "Centimeters to Inches", "Inches to Centimeters"])
elif category == "Weight":
    unit = st.selectbox("Select Conversion", ["Kilograms to Pounds", "Pounds to Kilograms", "Grams to Ounces", "Ounces to Grams"])
elif category == "Temperature":
    unit = st.selectbox("Select Conversion", ["Celsius to Fahrenheit", "Fahrenheit to Celsius"])
elif category == "Time":
    unit = st.selectbox("Select Conversion", ["Seconds to Minutes", "Minutes to Seconds", "Minutes to Hours", "Hours to Minutes", "Hours to Days", "Days to Hours"])

# Input
value = st.number_input("Enter your Value to Convert", min_value=0.0, step=0.1)

# Conversion Result
if st.button("Convert"):
    result = Convert_Units(category, value, unit)
    if result != 0:
        st.markdown('<div class="success-msg">✅ Conversion Successful</div>', unsafe_allow_html=True)
        st.markdown(f'<div class="result-box">The result is {result:.2f}</div>', unsafe_allow_html=True)
        st.balloons()
    else:
        st.markdown('<div class="error-msg">⚠ Conversion failed. Please check your inputs.</div>', unsafe_allow_html=True)

# Footer
st.markdown("---")
st.write("Made with ❤️ by [Amna](https://www.linkedin.com/in/amna-kh-0507532b4/)")

