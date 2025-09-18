import streamlit as st
from profiles import create_profile,  get_profile
from form_submit import update_personal_info
from ai import ask_ai

st.title("Personal Movie Recommendation App")

@st.fragment
def personal_data_form():
    with st.form("personal_data"):
        st.header("Personal Data")
        
        profile = st.session_state.profile
        
        name = st.text_input("Name",value=profile["general"]["name"])
        age = st.number_input("Age", min_value=1, max_value=120, step=1,value=profile["general"]["age"])
        nationality = st.text_input("Nationality",value=profile["general"]["nationality"])
        
        genders = ["Male","Female","Other"]
        gender = st.radio('Gender',genders,genders.index(profile["general"].get("gender","Male")))
        
        levels = ["Beginner", "Intermediate", "Expert"]
        level = st.selectbox("Movie Enthusiast Level", levels,index=levels.index(profile["general"].get("level","Beginner")))
        
        types = ("Action", "Comedy", "Drama", "Horror", "Sci-Fi", "Romance", "Documentary","Thriller", "Animation", "Fantasy")
        movie_types = st.multiselect("Preferred Movie Types", types, default=profile["general"].get("movie_types", []))
        
        personal_data_submit = st.form_submit_button("Save")
        if personal_data_submit:
            if all([name,age,nationality,gender,level,movie_types]):
                with st.spinner():
                    update_personal_info(profile,"general",name=name,age=age,nationality=nationality,gender=gender,level=level,movie_types=movie_types)
                    st.success("Data saved successfully!")
            else :
                st.warning("Please fill in all fields.")  
       
@st.fragment
def ask_ai_func():
    profile = st.session_state.profile
    st.subheader('AI Movie Recommendations')
    user_question = st.text_input("Ask for movie recommendations or preferences: ")
    if st.button("Ask AI"):
        with st.spinner():
            result = ask_ai(profile.get("general"),user_question)
            st.write(result)

def forms():
    if "profile" not in st.session_state:
        profile_id = 1
        profile = get_profile(profile_id)
        if not profile:
            profile_id, profile = create_profile(profile_id)        
        
        st.session_state.profile = profile
        st.session_state.profile_id = profile_id
        
    personal_data_form() 
    ask_ai_func()
    
if __name__ == "__main__":
    forms()                
        