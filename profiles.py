from db import personal_data_collection

# Function to get default profile values
def get_values(_id):
    return {
        "_id": _id,
        "general": {
            "name": "",
            "age": 30,
            "nationality": "",
            "gender": "Male",
            "level": "Beginner",
            "movie_types": []
        }
    }

# Function to create a new profile in the database
def create_profile(_id):
    profile_values = get_values(_id)
    result = personal_data_collection.insert_one(profile_values)
    return result.inserted_id, profile_values

# Function to get a profile from the database
def get_profile(_id):
    return personal_data_collection.find_one({"_id": {"$eq": _id}})