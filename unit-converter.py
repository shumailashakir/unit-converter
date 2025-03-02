import streamlit as st

st.title("🌏 Unit Converter App")
st.markdown("### Convert Length, Weight, and Time Instantly")
st.write("Welcome! Select a category, enter a value, and get the converted result in real-time.")

# Category selection
category = st.selectbox("Choose a category", ["Length", "Weight", "Time"])

# Function to perform conversion
def convert_units(category, value, unit):
    if category == "Length":
        if unit == "Kilometers to miles":
            return value * 0.621371
        elif unit == "Miles to kilometers":
            return value / 0.621371
        elif unit == "Meters to feet":
            return value * 3.28084
        elif unit == "Feet to meters":
            return value / 3.28084

    elif category == "Weight":
        if unit == "Kilograms to pounds":
            return value * 2.20462
        elif unit == "Pounds to kilograms":
            return value / 2.20462
        elif unit == "Grams to kilograms":
            return value / 1000
        elif unit == "Kilograms to grams":
            return value * 1000

    elif category == "Time":
        if unit == "Seconds to minutes":
            return value / 60
        elif unit == "Minutes to seconds":
            return value * 60
        elif unit == "Minutes to hours":
            return value / 60
        elif unit == "Hours to minutes":
            return value * 60
        elif unit == "Hours to days":
            return value / 24
        elif unit == "Days to hours":
            return value * 24
        elif unit == "Seconds to hours":
            return value / 3600
        elif unit == "Hours to seconds":
            return value * 3600

    return None  # In case no valid conversion is found

# Unit selection based on category
if category == "Length":
    unit = st.selectbox("📏 Select Conversion", ["Kilometers to miles", "Miles to kilometers", "Meters to feet", "Feet to meters"])
elif category == "Weight":
    unit = st.selectbox("⚖ Select Conversion", ["Kilograms to pounds", "Pounds to kilograms", "Grams to kilograms", "Kilograms to grams"])
elif category == "Time":
    unit = st.selectbox("⏱ Select Conversion", ["Seconds to minutes", "Minutes to seconds", 
                                                "Minutes to hours", "Hours to minutes", 
                                                "Hours to days", "Days to hours",
                                                "Seconds to hours", "Hours to seconds"])

# Input value
value = st.number_input("Enter the value to convert", min_value=0.0)

# Conversion button
if st.button("Convert"):
    result = convert_units(category, value, unit)
    if result is not None:
        st.success(f"The result is {result:.2f}")
    else:
        st.error("Invalid conversion selection.")
