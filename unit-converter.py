import streamlit as st

# Custom CSS for styling
st.markdown(
    """
    <style>
        /* Change the background color of the main content */
        [data-testid="stAppViewContainer"] {
            background-color: #f0f0f0;
        }

        /* Style the button */
        .stButton > button {
            background-color: #007bff !important;
            color: white !important;
            border-radius: 5px;
            padding: 10px 20px;
            border: none;
        }
    </style>
    """,
    unsafe_allow_html=True
)

st.title("🌏 Unit Converter App")
st.markdown("### Convert Length, Weight, Time, and More Instantly")
st.write("Welcome! Select a category, enter a value, and get the converted result in real-time.")

# Category selection
category = st.selectbox("Choose a category", [
    "Length", "Weight", "Time", "Temperature", "Speed",
    "Area", "Volume", "Energy", "Pressure", "Data Storage"
])

# Function to perform conversion
def convert_units(category, value, unit):
    if category == "Length":
        conversions = {
            "Kilometers to miles": value * 0.621371,
            "Miles to kilometers": value / 0.621371,
            "Meters to feet": value * 3.28084,
            "Feet to meters": value / 3.28084
        }
    elif category == "Weight":
        conversions = {
            "Kilograms to pounds": value * 2.20462,
            "Pounds to kilograms": value / 2.20462,
            "Grams to kilograms": value / 1000,
            "Kilograms to grams": value * 1000
        }
    elif category == "Time":
        conversions = {
            "Seconds to minutes": value / 60,
            "Minutes to seconds": value * 60,
            "Minutes to hours": value / 60,
            "Hours to minutes": value * 60,
            "Hours to days": value / 24,
            "Days to hours": value * 24,
            "Seconds to hours": value / 3600,
            "Hours to seconds": value * 3600
        }
    elif category == "Temperature":
        conversions = {
            "Celsius to Fahrenheit": (value * 9/5) + 32,
            "Fahrenheit to Celsius": (value - 32) * 5/9,
            "Celsius to Kelvin": value + 273.15,
            "Kelvin to Celsius": value - 273.15
        }
    elif category == "Speed":
        conversions = {
            "Kilometers/hour to Miles/hour": value * 0.621371,
            "Miles/hour to Kilometers/hour": value / 0.621371,
            "Meters/second to Kilometers/hour": value * 3.6,
            "Kilometers/hour to Meters/second": value / 3.6
        }
    elif category == "Area":
        conversions = {
            "Square meters to Square feet": value * 10.7639,
            "Square feet to Square meters": value / 10.7639
        }
    elif category == "Volume":
        conversions = {
            "Liters to Gallons": value * 0.264172,
            "Gallons to Liters": value / 0.264172
        }
    elif category == "Energy":
        conversions = {
            "Joules to Calories": value * 0.239006,
            "Calories to Joules": value / 0.239006
        }
    elif category == "Pressure":
        conversions = {
            "Pascals to Atmospheres": value / 101325,
            "Atmospheres to Pascals": value * 101325
        }
    elif category == "Data Storage":
        conversions = {
            "Bytes to Kilobytes": value / 1024,
            "Kilobytes to Bytes": value * 1024,
            "Kilobytes to Megabytes": value / 1024,
            "Megabytes to Kilobytes": value * 1024
        }
    else:
        conversions = {}

    return conversions.get(unit, None)

# Unit selection based on category
units_dict = {
    "Length": ["Kilometers to miles", "Miles to kilometers", "Meters to feet", "Feet to meters"],
    "Weight": ["Kilograms to pounds", "Pounds to kilograms", "Grams to kilograms", "Kilograms to grams"],
    "Time": ["Seconds to minutes", "Minutes to seconds", "Minutes to hours", "Hours to minutes",
             "Hours to days", "Days to hours", "Seconds to hours", "Hours to seconds"],
    "Temperature": ["Celsius to Fahrenheit", "Fahrenheit to Celsius", "Celsius to Kelvin", "Kelvin to Celsius"],
    "Speed": ["Kilometers/hour to Miles/hour", "Miles/hour to Kilometers/hour",
              "Meters/second to Kilometers/hour", "Kilometers/hour to Meters/second"],
    "Area": ["Square meters to Square feet", "Square feet to Square meters"],
    "Volume": ["Liters to Gallons", "Gallons to Liters"],
    "Energy": ["Joules to Calories", "Calories to Joules"],
    "Pressure": ["Pascals to Atmospheres", "Atmospheres to Pascals"],
    "Data Storage": ["Bytes to Kilobytes", "Kilobytes to Bytes", "Kilobytes to Megabytes", "Megabytes to Kilobytes"]
}

unit = st.selectbox("Select Conversion", units_dict[category])

# Input value
value = st.number_input("Enter the value to convert", min_value=0.0)

# Conversion button
if st.button("Convert"):
    result = convert_units(category, value, unit)
    if result is not None:
        st.success(f"The result is {result:.4f}")
    else:
        st.error("Invalid conversion selection.")
