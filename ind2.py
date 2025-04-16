import streamlit as st

# Function for Sulphate Test Procedure
def procedure_sulphate():
    st.subheader("Sulphate (SO₄²⁻) Test Procedure")
    st.write("""
        1. Take a small amount of the unknown solution in a test tube.
        2. Add a few drops of barium chloride (BaCl₂) solution.
    """)

# Function for Sulphate Test Observation
def observation_sulphate():
    st.subheader("Sulphate (SO₄²⁻) Test Observation")
    st.write("""
        - A white precipitate forms if sulphate ions (SO₄²⁻) are present.
    """)

# Function for Sulphate Confirmatory Test
def confirmatory_sulphate():
    st.subheader("Sulphate (SO₄²⁻) Confirmatory Test")
    st.write("""
        1. Add a few drops of dilute hydrochloric acid (HCl) to dissolve the precipitate.
        2. If the precipitate remains after adding hydrochloric acid, the presence of sulphate ions is confirmed.
    """)

# Function for Phosphate Test Procedure
def procedure_phosphate():
    st.subheader("Phosphate (PO₄³⁻) Test Procedure")
    st.write("""
        1. Add ammonium molybdate ((NH₄)₂MoO₄) and a few drops of nitric acid (HNO₃) to the unknown solution.
    """)

# Function for Phosphate Test Observation
def observation_phosphate():
    st.subheader("Phosphate (PO₄³⁻) Test Observation")
    st.write("""
        - A yellow precipitate forms if phosphate ions (PO₄³⁻) are present.
    """)

# Function for Phosphate Confirmatory Test
def confirmatory_phosphate():
    st.subheader("Phosphate (PO₄³⁻) Confirmatory Test")
    st.write("""
        1. Gently heat the solution.
        2. If a yellow crystalline precipitate forms, the presence of phosphate ions is confirmed.
    """)

# Function for Borate Test Procedure
def procedure_borate():
    st.subheader("Borate (BO₃³⁻) Test Procedure")
    st.write("""
        1. Add a small piece of turmeric paper to the unknown solution.
    """)

# Function for Borate Test Observation
def observation_borate():
    st.subheader("Borate (BO₃³⁻) Test Observation")
    st.write("""
        - If the turmeric paper turns red, it indicates the presence of borate ions (BO₃³⁻).
    """)

# Function for Borate Confirmatory Test
def confirmatory_borate():
    st.subheader("Borate (BO₃³⁻) Confirmatory Test")
    st.write("""
        1. Heat the solution with a few drops of sodium hydroxide (NaOH).
        2. If a yellow color forms in the solution, it confirms the presence of borate ions.
    """)

# Main function to create the app
def main():
    st.title("Anion Test for Independent Radicals")

    st.write("""
        This app provides interactive tests for the detection of three anions:
        - Sulphate (SO₄²⁻)
        - Phosphate (PO₄³⁻)
        - Borate (BO₃³⁻)
    """)

    st.header("Select the anion test and see details below:")

    # Sulphate Test Buttons
    if st.button('Sulphate Test Procedure'):
        procedure_sulphate()

    if st.button('Sulphate Test Observation'):
        observation_sulphate()

    if st.button('Sulphate Test Confirmatory Test'):
        confirmatory_sulphate()

    # Phosphate Test Buttons
    if st.button('Phosphate Test Procedure'):
        procedure_phosphate()

    if st.button('Phosphate Test Observation'):
        observation_phosphate()

    if st.button('Phosphate Test Confirmatory Test'):
        confirmatory_phosphate()

    # Borate Test Buttons
    if st.button('Borate Test Procedure'):
        procedure_borate()

    if st.button('Borate Test Observation'):
        observation_borate()

    if st.button('Borate Test Confirmatory Test'):
        confirmatory_borate()

if __name__ == "__main__":
    main()
