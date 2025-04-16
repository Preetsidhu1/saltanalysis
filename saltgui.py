import importlib
import streamlit as st
from streamlit_option_menu import option_menu
import io
import sqlite3
import bcrypt


with st.sidebar:
   opt=option_menu("Dashboard",["login page","Home","Inorganic","Organic"],icons=["people","house","flask","flask"],menu_icon="cast",default_index=0)
if opt=="login page":

  # Function to create a SQLite database and users table
   def create_db():
     conn = sqlite3.connect('users.db')  # Connect to SQLite database (or create it if it doesn't exist)
     cursor = conn.cursor()
     cursor.execute('''CREATE TABLE IF NOT EXISTS users (
                        username TEXT PRIMARY KEY, 
                        password TEXT NOT NULL)''')
     conn.commit()
     conn.close()

  # Function to register a new user
   def register_user(username, password):
     conn = sqlite3.connect('users.db')
     cursor = conn.cursor()
    
     # Check if username already exists
     cursor.execute("SELECT * FROM users WHERE username = ?", (username,))
     if cursor.fetchone():
        return False  # User already exists
    
     # Hash the password before storing it
     hashed_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
    
     # Insert the new user into the database
     cursor.execute("INSERT INTO users (username, password) VALUES (?, ?)", 
                   (username, hashed_password))
     conn.commit()
     conn.close()
     return True

   # Function to authenticate a user during login
   def authenticate_user(username, password):
    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()
    if st.button("select"):
            apple=cursor.execute("SELECT * FROM users " )
            st.write("apple")
    # Query the database for the given username
    cursor.execute("SELECT * FROM users WHERE username = ?", (username,))
    user = cursor.fetchone()
    conn.close()
    
    # If user exists and password matches the hash
    if user and bcrypt.checkpw(password.encode('utf-8'), user[1]):
        return True
    return False

  # Function to display the login page
   def login_page():
    st.title("Login Page")
    
    username = st.text_input("Username")
    password = st.text_input("Password", type='password')
    
    if st.button("Login"):
        if authenticate_user(username, password):
            st.success("Login successful!")
            st.write(f"Welcome, {username}!")
            home_page()  # Redirect to the home page if login is successful
        else:
            st.error("Invalid username or password.")

  # Function to display the signup page
   def signup_page():
    st.title("Signup Page")
    
    username = st.text_input("Username")
    password = st.text_input("Password", type='password')
    confirm_password = st.text_input("Confirm Password", type='password')
    
    if st.button("Signup"):
        if password != confirm_password:
            st.error("Passwords do not match!")
        elif register_user(username, password):
            st.success("User registered successfully!")
            st.write("Now, you can log in with your credentials.")
           # login_page()  # Redirect to login page after successful registration
        else:
            st.error("Username already exists. Please choose a different username.")
    

    # Function to display the home page after successful login
   def home_page():
    st.title("Home Page")
    st.write("Welcome to the home page!")

   # Main function to control navigation between pages
   def main():
    create_db()  # Ensure the database and table are created at the start
    
    # Display the choice of either login or signup
    page = st.selectbox("Choose an option", ["Login", "Signup"])
    
    if page == "Login":
        login_page()
    elif page == "Signup":
        signup_page()

    # Run the app
   if __name__ == "__main__":
    main()


elif opt=="Home":
    
    with st.container():
        
        st.header("Introduction")
        st.write("Salt analysis in chemistry refers to the systematic process of identifying the components of a salt, particularly the cations (positively charged ions) and anions (negatively charged ions) present in the sample.  This process is vital for understanding the chemical composition of salts, which are typically formed when acids react with bases.")
        st.header("Key Steps in Salt Analysis:")
        st.write(
                """The primary objectives of this study are as follows:

1. Preparation of the Salt Solution: The salt is dissolved in water to make a solution. If the salt is insoluble in water, it may be treated with other solvents.

2.Preliminary Tests: The solution is tested for any obvious physical properties, such as color, smell, or texture, and this information can provide initial clues about the identity of the salt.

3.Identification of Cations: Various reagents are added to the solution to identify the cations (metal ions or other positively charged species). Common tests for cations include:
    Flame test (for metal ions like sodium, potassium, copper)

4.Identification of Anions: After identifying the cations, anion tests are performed. This involves adding specific reagents that react with the anions to form precipitates or produce characteristic color changes. Common reagents for detecting anions include:
    Silver nitrate (AgNO₃) for chloride, bromide, and iodide ions.
    
5.Confirmatory Tests: Further tests are conducted to confirm the identity of specific ions, often based on their reactions with certain reagents that produce unique and identifiable outcomes.
"""
                )
    with st.container():
        st.write("---")
        c1,c2=st.columns(2)
        with c1:
            st.header("Importance of Salt Anaylsis")
        st.write(
                """The primary importance of salt anaylsis are as follows:

1.Identification of Unknown Substances: In laboratories, salt analysis helps identify unknown salts or compounds.

2.Quality Control: In industrial and environmental chemistry, salt analysis ensures the quality and composition of substances.

3.Understanding Chemical Properties: Salt analysis helps understand the behavior and reactivity of salts in various chemical reactions.
"""
        )
      
        with c2:
            st.write("---") 
            st.image("images/chemistry.jpg")

elif opt=="Inorganic":
    
   a=st.sidebar.selectbox("Select Continents",options=["preliminary test","test for anion","test for cation"])
    
   if a=="preliminary test":
         
      op= st.selectbox("Select test2 ",options=[" colour test and solubility test","flame test"])
      
      
        
      if op=="colour test and solubility test":    
        
       # Function to identify ion, provide its color, and solubility information
            def identify_ion_by_color(color):
             if color == "blue":
              return (
              "Cu²⁺ (Copper(II) ion) - Blue precipitate",
              "Solubility: Insoluble in water; forms blue precipitate with NaOH."
             )
             elif color == "green":
              return (
              "Fe²⁺ (Iron(II) ion) - Green precipitate",
              "Solubility: Soluble in water, forms a green precipitate with NaOH."
            )
             elif color == "rust-brown":
              return (
              "Fe³⁺ (Iron(III) ion) - Rust-brown precipitate",
              "Solubility: Soluble in water, forms a rust-brown precipitate with NaOH."
            )
             elif color == "yellow":
               return (
               "Cr³⁺ (Chromium(III) ion) - Yellow solution",
               "Solubility: Soluble in water, forms a yellow solution in water."
            )
             elif color == "white":
               return (
               "Ca²⁺ (Calcium ion) - White precipitate",
               "Solubility: Slightly soluble in water, forms a white precipitate with NaOH."
            )
             elif color == "purple":
              return (
              "MnO₄⁻ (Permanganate ion) - Purple color in solution",
              "Solubility: Soluble in water, purple color persists in aqueous solution."
            )
             else:
              st.write("Unknown ion or no reaction", "Solubility: Unknown.")

            # Streamlit app layout
            st.title('Chemistry Ion Identification and Solubility Test')

            # Add a dropdown menu for the user to select the color
            color = st.selectbox('Select the color observed:',
                     ['blue', 'green', 'rust-brown', 'yellow', 'white', 'purple'])

            # Display the result when the button is pressed
            if st.button('Identify Ion and Solubility'):
              ion_info, solubility_info = identify_ion_by_color(color)
              st.write(f'The identified ion is: {ion_info}')
              st.write(f'{solubility_info}')
        
      elif op=="flame test":      

            #title foe flame test
            st.title("Flame Test Simulation")

            # Element selection
            flame_color = st.selectbox("Choose an color for the flame test:", 
                       ["Yellow", "Green","Crimson Red", "Lilac", "Orange -Red", "Red", "Green"])

            # Function to determine flame color based on element
            def element(flame_color):
               if flame_color == "Yellow":
                return "Sodium (Na)"
               elif flame_color == "Green":
                return "Copper (Cu)"
               elif flame_color== "Crimson Red":
                return " Lithium (Li)"
               elif flame_color== "Lilac":
                return "Potassium (K)"
               elif flame_color== "Orange-Red":
                return "Calcium (Ca)"
               elif flame_color == "Red":
                return "Strontium (Sr)"
               elif flame_color == "Green":
                 return "Barium (Ba)"
               else:
                 return "Absent"

            # Display the flame color based on selection
            element = element(flame_color)

            #Display the result based on the selected element
            st.write(f"The flame color for {element} is: {flame_color}")

            
   elif a=="test for anion":
      oppt= st.selectbox("Select test3",options=["dilute h2so4","concentrated h2so4","independent radicals"])  

      if oppt =="dilute h2so4":
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
   

      elif oppt=="concentrated h2so4":  
          
       
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

      

       
      elif oppt=="independent radicals":
       
       
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
         

       
   elif a=="test for cation":
        
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
 


elif opt=="Organic" :
    st.write("FUTURE PLAN")   

