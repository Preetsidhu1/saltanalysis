import streamlit as st

# Function to display cation test information based on selected group
def cation_test(cation_group):
    if cation_group == "Group 0 (Ammonium)":
        result = """
        ### Experiment: Test for Ammonium Ion (NH₄⁺)
        1. Add sodium hydroxide (NaOH) solution to the ammonium salt.
        2. Heat the mixture gently.

        **Observation**: 
        - Ammonia gas (NH₃) is released, which has a pungent odor.
        - Ammonia gas turns damp red litmus paper blue.

        **Chemical Equation**: 
        NH₄⁺ + OH⁻ → NH₃ (gas) + H₂O

        **Inference**: 
        - The release of ammonia gas indicates the presence of ammonium ions (NH₄⁺).
        """
        
    elif cation_group == "Group 1 (Alkali Metals)":
        result = """
        ### Experiment: Test for Alkali Metals (Li⁺, Na⁺, K⁺, Rb⁺, Cs⁺)
        1. Perform a flame test by placing the salt in a flame.

        **Observation**: 
        - **Li⁺**: Crimson red flame
        - **Na⁺**: Yellow flame
        - **K⁺**: Lilac flame

        **Chemical Equation**: 
        - For Na⁺: 2Na + O₂ → 2Na₂O
        - For K⁺: 2K + O₂ → 2K₂O

        **Inference**: 
        - The distinct flame color corresponds to the presence of a specific alkali metal ion.
        """
        
    elif cation_group == "Group 2 (Alkaline Earth Metals)":
        result = """
        ### Experiment: Test for Alkaline Earth Metals (Ca²⁺, Mg²⁺, Ba²⁺)
        1. Perform a flame test by placing the salt in a flame.

        **Observation**: 
        - **Ca²⁺**: Brick-red flame
        - **Ba²⁺**: Green flame
        - **Mg²⁺**: No distinct flame color (white precipitate with NaOH)

        **Chemical Equation**: 
        - For Ca²⁺: Ca + O₂ → CaO
        - For Ba²⁺: Ba + O₂ → BaO

        **Inference**: 
        - The flame colors help identify the alkaline earth metal present in the solution.
        """
        
    elif cation_group == "Group 3 (Aluminium, Zinc)":
        result = """
        ### Experiment: Test for Aluminium (Al³⁺) and Zinc (Zn²⁺)
        1. Add sodium hydroxide (NaOH) to the solution.

        **Observation**: 
        - **Al³⁺**: White precipitate, dissolves in excess NaOH to form a colorless solution.
        - **Zn²⁺**: White precipitate, dissolves in excess NaOH to form a colorless solution.

        **Chemical Equation**: 
        - For Al³⁺: Al³⁺ + 3OH⁻ → Al(OH)₃ (white precipitate)
        - For Zn²⁺: Zn²⁺ + 2OH⁻ → Zn(OH)₂ (white precipitate)

        **Inference**: 
        - The formation of a white precipitate that dissolves in excess NaOH indicates the presence of aluminum or zinc ions.
        """
        
    elif cation_group == "Group 4 (Copper, Lead, Iron)":
        result = """
        ### Experiment: Test for Copper (Cu²⁺), Lead (Pb²⁺), and Iron (Fe³⁺)
        1. Add sodium hydroxide (NaOH) to the solution.

        **Observation**: 
        - **Cu²⁺**: Blue precipitate with NaOH.
        - **Pb²⁺**: White precipitate with NaOH, dissolves in excess NaOH.
        - **Fe³⁺**: Brown precipitate with NaOH.

        **Chemical Equation**: 
        - For Cu²⁺: Cu²⁺ + 2OH⁻ → Cu(OH)₂ (blue precipitate)
        - For Pb²⁺: Pb²⁺ + 2OH⁻ → Pb(OH)₂ (white precipitate)
        - For Fe³⁺: Fe³⁺ + 3OH⁻ → Fe(OH)₃ (brown precipitate)

        **Inference**: 
        - The color of the precipitate indicates the presence of copper, lead, or iron ions.
        """
        
    elif cation_group == "Group 5 (Silver, Lead)":
        result = """
        ### Experiment: Test for Silver (Ag⁺) and Lead (Pb²⁺)
        1. Add hydrochloric acid (HCl) to the solution.

        **Observation**: 
        - **Ag⁺**: White precipitate of AgCl.
        - **Pb²⁺**: White precipitate of PbCl₂.

        **Chemical Equation**: 
        - For Ag⁺: Ag⁺ + Cl⁻ → AgCl (white precipitate)
        - For Pb²⁺: Pb²⁺ + 2Cl⁻ → PbCl₂ (white precipitate)

        **Inference**: 
        - The formation of white precipitates confirms the presence of either silver or lead ions.
        """
        
    elif cation_group == "Group 6 (Calcium, Magnesium)":
        result = """
        ### Experiment: Test for Calcium (Ca²⁺) and Magnesium (Mg²⁺)
        1. Add sodium hydroxide (NaOH) to the solution.

        **Observation**: 
        - **Ca²⁺**: White precipitate, slightly soluble in excess NaOH.
        - **Mg²⁺**: White precipitate, insoluble in excess NaOH.

        **Chemical Equation**: 
        - For Ca²⁺: Ca²⁺ + 2OH⁻ → Ca(OH)₂ (white precipitate)
        - For Mg²⁺: Mg²⁺ + 2OH⁻ → Mg(OH)₂ (white precipitate)

        **Inference**: 
        - The formation of white precipitates indicates the presence of calcium or magnesium ions.
        """
    
    return result


# Streamlit app layout
st.title("Cation Group Identification Test")

# Select group
cation_group = st.selectbox(
    "Select Cation Group for Identification:",
    ["Group 0 (Ammonium)", "Group 1 (Alkali Metals)", "Group 2 (Alkaline Earth Metals)", 
     "Group 3 (Aluminium, Zinc)", "Group 4 (Copper, Lead, Iron)", 
     "Group 5 (Silver, Lead)", "Group 6 (Calcium, Magnesium)"]
)

# Show cation test details based on selected group
st.write(cation_test(cation_group))
