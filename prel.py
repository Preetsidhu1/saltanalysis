import streamlit as st

# Function to identify ion based on color
def identify_ion_by_color(color):
    # Convert input to lowercase to match with the function checks
    color = color.lower()
    
    if color == "blue":
        return "Cu²⁺ (Copper(II) ion) - Blue precipitate"
    elif color == "green":
        return "Fe²⁺ (Iron(II) ion) - Green precipitate"
    elif color == "rust-brown":
        return "Fe³⁺ (Iron(III) ion) - Rust-brown precipitate"
    elif color == "yellow":
        return "Cr³⁺ (Chromium(III) ion) - Yellow solution"
    elif color == "white":
        return "Ca²⁺ (Calcium ion) - White precipitate"
    elif color == "purple":
        return "MnO₄⁻ (Permanganate ion) - Purple color in solution"
    else:
        return "Ion is absent"

# Streamlit title
st.title('Color Test Simulation')

# Add a dropdown menu for the user to select the color
color = st.selectbox('Select the color observed:',
                     ['Blue', 'Green', 'Rust-Brown', 'Yellow', 'White', 'Purple'])

# Display the result when the button is pressed
if st.button('Identify Ion'):
    result = identify_ion_by_color(color)
    st.write(f'The identified ion is: {result}')
