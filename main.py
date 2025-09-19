import streamlit as st
from profiles import create_profile,  get_profile
from form_submit import update_personal_info
from ai import ask_ai

# Set main title of the app
st.title("Personal Movie Recommendation App")

# Form to collect and update personal data
@st.fragment
def personal_data_form():
    # Create a form for personal data input, everything inside the form will be submitted together with one button
    with st.form("personal_data"):
        # Form title
        st.header("Personal Data")
        
        # Load existing profile data from session state
        profile = st.session_state.profile
        
        # Input fields with pre-filled values from the existing profile
        name = st.text_input("Name",value=profile["general"]["name"])
        age = st.number_input("Age", min_value=1, max_value=120, step=1,value=profile["general"]["age"])
        nationality = st.text_input("Nationality",value=profile["general"]["nationality"])    
        genders = ["Male","Female","Other"]
        gender = st.radio('Gender',genders,genders.index(profile["general"].get("gender","Male")))
        levels = ["Beginner", "Intermediate", "Expert"]
        level = st.selectbox("Movie Enthusiast Level", levels,index=levels.index(profile["general"].get("level","Beginner")))
        types = ("Action", "Comedy", "Drama", "Horror", "Sci-Fi", "Romance", "Documentary","Thriller", "Animation", "Fantasy")
        movie_types = st.multiselect("Preferred Movie Types", types, default=profile["general"].get("movie_types", []))
        
        # Submit button for the form
        personal_data_submit = st.form_submit_button("Save")
        
        # When the submit button is pressed
        if personal_data_submit:
            # Validate that all fields are filled
            if all([name,age,nationality,gender,level,movie_types]):
                # Update the profile in the database
                with st.spinner():
                    update_personal_info(profile,"general",name=name,age=age,nationality=nationality,gender=gender,level=level,movie_types=movie_types)
                    st.success("Data saved successfully!")
            else :
                st.warning("Please fill in all fields.")  
    
# AI interaction section
@st.fragment
def ask_ai_func():
    # Get the profile from session state
    profile = st.session_state.profile
    # AI section
    st.subheader('AI Movie Recommendations')
    # Input for user question/goal
    user_question = st.text_input("Ask for movie recommendations or preferences: ")
    # Button to trigger AI response
    if st.button("Ask AI"):
        # return the AI response
        with st.spinner():
            result = ask_ai(profile.get("general"),user_question)
            st.write(result)

# Main function to handle forms and session state
def forms():
    # Initialize session state for profile if not already set
    if "profile" not in st.session_state:
        profile_id = 1 # In a real app, this would be the user ID from authentication
        profile = get_profile(profile_id)
        if not profile:
            profile_id, profile = create_profile(profile_id)        
        
        st.session_state.profile = profile
        st.session_state.profile_id = profile_id
    
    # Display the personal data form and AI interaction section  
    personal_data_form() 
    ask_ai_func()
    
if __name__ == "__main__":
    forms()                
        