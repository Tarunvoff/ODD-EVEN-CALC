import streamlit as st

# Function to check if the number is odd or even
def check_odd_even(number):
    if number % 2 == 0:
        return "Even"
    else:
        return "Odd"

# Streamlit App UI
def main():
    # Title for the app
    st.title("Odd or Even Number Checker")

    # Instructions for users
    st.write("### Enter a number below to check if it's odd or even:")

    # Input field for user to enter a number
    number_input = st.text_input("Enter a number", "")

    # Check if the input is a valid number
    if number_input:
        try:
            number = int(number_input)
            result = check_odd_even(number)
            st.success(f"The number {number} is {result}.")
        except ValueError:
            st.error("Please enter a valid integer.")

    # Some additional style for UI
    st.write("Made for Gen AI students learning Python with Streamlit!")

if __name__ == "__main__":
    main()