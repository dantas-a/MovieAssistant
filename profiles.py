from db import personal_data_collection

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

def create_profile(_id):
    profile_values = get_values(_id)
    result = personal_data_collection.insert_one(profile_values)
    return result.inserted_id, result

def get_profile(_id):
    return personal_data_collection.find_one({"_id": {"$eq": _id}})