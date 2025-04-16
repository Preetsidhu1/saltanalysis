import streamlit as st

# Dictionary containing anion information
anion_data = {
    "Chloride (Cl⁻)": {
        "test_with_h2so4": "White fumes of HCl gas are evolved which turn blue litmus red.",
        "confirmatory_test": "Add silver nitrate solution - white precipitate soluble in NH4OH.",
        "chemical_eq": "NaCl + H2SO4 → NaHSO4 + HCl↑"
    },
    "Nitrate (NO₃⁻)": {
        "test_with_h2so4": "Brown fumes of NO2 gas are evolved.",
        "confirmatory_test": "Brown ring test with FeSO4 and conc. H2SO4.",
        "chemical_eq": "2NaNO3 + H2SO4 → Na2SO4 + 2HNO3\n4HNO3 → 4NO2↑ + O2↑ + 2H2O"
    },
    "Carbonate (CO₃²⁻)": {
        "test_with_h2so4": "Effervescence with colorless CO2 gas which turns lime water milky.",
        "confirmatory_test": "Bubble gas through lime water - turns milky.",
        "chemical_eq": "Na2CO3 + H2SO4 → Na2SO4 + H2O + CO2↑"
    },
    "Sulfate (SO₄²⁻)": {
        "test_with_h2so4": "No reaction with conc. H2SO4 alone.",
        "confirmatory_test": "Add BaCl2 solution - white precipitate insoluble in acids.",
        "chemical_eq": "Ba²⁺ + SO₄²⁻ → BaSO4↓ (white)"
    },
    "Acetate (CH₃COO⁻)": {
        "test_with_h2so4": "Vinegar-like smell of acetic acid.",
        "confirmatory_test": "Add ethanol and conc. H2SO4 - fruity ester smell.",
        "chemical_eq": "CH3COONa + H2SO4 → NaHSO4 + CH3COOH"
    }
}

def main():
    st.title("Anion Test with Concentrated H₂SO₄")
    st.write("This app guides you through testing anions using concentrated sulfuric acid.")
    
    # Step 1: Select a salt
    st.header("Step 1: Select a Salt")
    selected_anion = st.selectbox(
        "Choose an anion to test:",
        list(anion_data.keys())
    )
    
    if st.button("Confirm Selection"):
        st.success(f"You selected: {selected_anion}")
        st.session_state.selected_anion = selected_anion
    
    # Step 2: Test with H2SO4
    if 'selected_anion' in st.session_state:
        st.header("Step 2: Test with Concentrated H₂SO₄")
        if st.button("Perform H₂SO₄ Test"):
            st.info(f"Observation for {st.session_state.selected_anion}:")
            st.write(anion_data[st.session_state.selected_anion]["test_with_h2so4"])
            st.write("Chemical equation(s):")
            st.code(anion_data[st.session_state.selected_anion]["chemical_eq"])
            st.session_state.h2so4_test_done = True
    
    # Step 3: Confirmatory Test
    if 'h2so4_test_done' in st.session_state:
        st.header("Step 3: Confirmatory Test")
        if st.button("Perform Confirmatory Test"):
            st.info(f"Confirmatory test for {st.session_state.selected_anion}:")
            st.write(anion_data[st.session_state.selected_anion]["confirmatory_test"])
            st.session_state.confirmatory_test_done = True
    
    # Step 4: Summary
    if 'confirmatory_test_done' in st.session_state:
        st.header("Step 4: Full Summary")
        if st.button("Show Summary"):
            anion = st.session_state.selected_anion
            st.subheader(f"Summary for {anion}")
            
            col1, col2 = st.columns(2)
            
            with col1:
                st.write("**Test with H₂SO₄:**")
                st.info(anion_data[anion]["test_with_h2so4"])
                
            with col2:
                st.write("**Confirmatory Test:**")
                st.success(anion_data[anion]["confirmatory_test"])
            
            st.write("**Chemical Equations:**")
            st.code(anion_data[anion]["chemical_eq"])
            
            st.balloons()

if __name__ == "__main__":
    main()
