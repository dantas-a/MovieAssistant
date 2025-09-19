from db import personal_data_collection

# Function to update personal information in the database
def update_personal_info(existing,update_type,**kwargs):
    existing[update_type] = kwargs
    update_field = {update_type: existing[update_type]}
        
    personal_data_collection.update_one({"_id": existing["_id"]},{"$set": update_field})
    return existing