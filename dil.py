import streamlit as st

def main():
    st.title("Anion Test with Dilute H₂SO₄")
    st.write("This app helps identify anions using dilute sulfuric acid and confirmatory tests.")
    
    # List of common anions
    anions = [
        "Carbonate (CO₃²⁻)",
        "Sulphite (SO₃²⁻)",
        "Sulphide (S²⁻)",
        "Nitrite (NO₂⁻)",
        "Acetate (CH₃COO⁻)",
        "Chloride (Cl⁻)",
        "Bromide (Br⁻)",
        "Iodide (I⁻)",
        "Nitrate (NO₃⁻)"
    ]
    
    # User selects an anion to test
    selected_anion = st.selectbox("Select an anion to test:", anions)
    
    st.header("Step 1: Test with Dilute H₂SO₄")
    st.write("Add a few drops of dilute sulfuric acid to a small amount of the salt.")
    
    if st.button("Perform Dilute H₂SO₄ Test"):
        if "Carbonate" in selected_anion:
            st.success("Effervescence occurs with colorless, odorless gas (CO₂) that turns lime water milky.")
        elif "Sulphite" in selected_anion:
            st.success("Effervescence occurs with colorless gas (SO₂) with choking smell that turns acidified K₂Cr₂O₇ paper green.")
        elif "Sulphide" in selected_anion:
            st.success("Colorless gas (H₂S) with rotten egg smell that turns lead acetate paper black.")
        elif "Nitrite" in selected_anion:
            st.success("Effervescence occurs with brown fumes (NO₂) and colorless gas (NO).")
        elif "Acetate" in selected_anion:
            st.success("Vinegar-like smell (CH₃COOH) is observed.")
        elif "Chloride" in selected_anion:
            st.warning("No reaction with dilute H₂SO₄. Proceed to confirmatory test.")
        elif "Bromide" in selected_anion:
            st.warning("No reaction with dilute H₂SO₄. Proceed to confirmatory test.")
        elif "Iodide" in selected_anion:
            st.warning("No reaction with dilute H₂SO₄. Proceed to confirmatory test.")
        elif "Nitrate" in selected_anion:
            st.warning("No reaction with dilute H₂SO₄. Proceed to confirmatory test.")
    
    st.header("Step 2: Confirmatory Test")
    
    if st.button("Perform Confirmatory Test"):
        if "Carbonate" in selected_anion:
            st.success("Confirmatory Test: Pass the gas through lime water. If it turns milky, CO₃²⁻ is confirmed.")
        elif "Sulphite" in selected_anion:
            st.success("Confirmatory Test: Add BaCl₂ solution to the salt solution. White precipitate soluble in dilute HCl confirms SO₃²⁻.")
        elif "Sulphide" in selected_anion:
            st.success("Confirmatory Test: Add sodium nitroprusside solution. Violet color confirms S²⁻.")
        elif "Nitrite" in selected_anion:
            st.success("Confirmatory Test: Add KI solution and starch. Blue color confirms NO₂⁻.")
        elif "Acetate" in selected_anion:
            st.success("Confirmatory Test: Add FeCl₃ solution. Red color that disappears on heating confirms CH₃COO⁻.")
        elif "Chloride" in selected_anion:
            st.success("Confirmatory Test: Add AgNO₃ solution. White precipitate insoluble in NH₄OH confirms Cl⁻.")
        elif "Bromide" in selected_anion:
            st.success("Confirmatory Test: Add AgNO₃ solution. Pale yellow precipitate sparingly soluble in NH₄OH confirms Br⁻.")
        elif "Iodide" in selected_anion:
            st.success("Confirmatory Test: Add AgNO₃ solution. Yellow precipitate insoluble in NH₄OH confirms I⁻.")
        elif "Nitrate" in selected_anion:
            st.success("Confirmatory Test: Brown ring test with FeSO₄ and conc. H₂SO₄ confirms NO₃⁻.")
    
    st.header("Full Test Summary")
    if st.button("Show Full Test Summary"):
        st.subheader(f"Test Results for {selected_anion}")
        
        # Dilute H2SO4 test results
        st.write("**Dilute H₂SO₄ Test:**")
        if "Carbonate" in selected_anion:
            st.write("- Effervescence with colorless, odorless gas (CO₂)")
            st.write("- Gas turns lime water milky")
        elif "Sulphite" in selected_anion:
            st.write("- Effervescence with colorless gas (SO₂) with choking smell")
            st.write("- Gas turns acidified K₂Cr₂O₇ paper green")
        elif "Sulphide" in selected_anion:
            st.write("- Colorless gas (H₂S) with rotten egg smell")
            st.write("- Gas turns lead acetate paper black")
        elif "Nitrite" in selected_anion:
            st.write("- Effervescence with brown fumes (NO₂) and colorless gas (NO)")
        elif "Acetate" in selected_anion:
            st.write("- Vinegar-like smell (CH₃COOH)")
        else:
            st.write("- No visible reaction with dilute H₂SO₄")
        
        # Confirmatory test results
        st.write("\n**Confirmatory Test:**")
        if "Carbonate" in selected_anion:
            st.write("- Pass gas through lime water → milky appearance confirms CO₃²⁻")
        elif "Sulphite" in selected_anion:
            st.write("- BaCl₂ + salt solution → white ppt soluble in dilute HCl confirms SO₃²⁻")
        elif "Sulphide" in selected_anion:
            st.write("- Sodium nitroprusside → violet color confirms S²⁻")
        elif "Nitrite" in selected_anion:
            st.write("- KI + starch → blue color confirms NO₂⁻")
        elif "Acetate" in selected_anion:
            st.write("- FeCl₃ → red color that disappears on heating confirms CH₃COO⁻")
        elif "Chloride" in selected_anion:
            st.write("- AgNO₃ → white ppt insoluble in NH₄OH confirms Cl⁻")
        elif "Bromide" in selected_anion:
            st.write("- AgNO₃ → pale yellow ppt sparingly soluble in NH₄OH confirms Br⁻")
        elif "Iodide" in selected_anion:
            st.write("- AgNO₃ → yellow ppt insoluble in NH₄OH confirms I⁻")
        elif "Nitrate" in selected_anion:
            st.write("- Brown ring test with FeSO₄ + conc. H₂SO₄ confirms NO₃⁻")

if __name__ == "__main__":
    main()