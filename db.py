from astrapy import DataAPIClient
from dotenv import load_dotenv
import streamlit as st

load_dotenv()

# set the endpoint
ENDPOINT = ""
# set the token
TOKEN = ""

@st.cache_resource
def get_db() :
    client = DataAPIClient(TOKEN)
    db = client.get_database_by_api_endpoint(ENDPOINT)
    return db

db = get_db()
# create the collection if it doesn't exist
try:
    db.create_collection("personal_data")
except:
    pass

personal_data_collection = db.get_collection("personal_data")
