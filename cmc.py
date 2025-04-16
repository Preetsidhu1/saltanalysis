import streamlit as st

st.title("Anion Test with Concentrated H₂SO₄")
st.write("Click on an anion to see its reaction with concentrated sulfuric acid.")

def test_carbonate():
    st.subheader("Carbonate (CO₃²⁻)")
    st.write("**Reaction:** CO₃²⁻ + 2H⁺ → CO₂ (gas) + H₂O")
    st.write("**Observation:** Effervescence due to CO₂ gas. Turns limewater milky.")

def test_sulfite():
    st.subheader("Sulfite (SO₃²⁻)")
    st.write("**Reaction:** SO₃²⁻ + 2H⁺ → SO₂ (gas) + H₂O")
    st.write("**Observation:** Pungent smell of SO₂. Turns acidified potassium dichromate from orange to green.")

def test_sulfate():
    st.subheader("Sulfate (SO₄²⁻)")
    st.write("**Reaction:** No visible reaction with H₂SO₄ alone.")
    st.write("**Observation:** No gas or visible change.")

def test_chloride():
    st.subheader("Chloride (Cl⁻)")
    st.write("**Reaction:** Cl⁻ + H₂SO₄ → HCl (gas)")
    st.write("**Observation:** Steamy fumes of HCl. Turns moist blue litmus red.")

def test_nitrate():
    st.subheader("Nitrate (NO₃⁻)")
    st.write("**Reaction:** NO₃⁻ + H₂SO₄ + Cu → NO₂ (brown gas) + others")
    st.write("**Observation:** Brown gas of NO₂ evolved if copper is present.")

# Buttons for each anion
if st.button("Test Carbonate"):
    test_carbonate()

if st.button("Test Sulfite"):
    test_sulfite()

if st.button("Test Sulfate"):
    test_sulfate()

if st.button("Test Chloride"):
    test_chloride()

if st.button("Test Nitrate"):
    test_nitrate()
