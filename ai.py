from langflow.load import run_flow_from_json

# This function takes a dictionary (or list) and converts it to a string
def dict_to_string(obj,level=0):
    # Set an empty string list to hold the strings
    strings=[]
    # Set the indent level
    indent = " " * level

    # Check the type of the object
    if isinstance(obj, dict):
        # Iterate through the dictionary
        for key,value in obj.items():
            # If the value is a dict or list, we need to go deeper
            if isinstance(value,(dict,list)):
                # Recursively call the function
                nested_string = dict_to_string(value,level+1)
                # Append the key and the nested string to the list
                strings.append(f"{indent}{key}: {nested_string}")
            else:
                strings.append(f"{indent}{key}: {value}")
    elif isinstance(obj,list):
        for idx,item in enumerate(obj):
            nested_string = dict_to_string(item,level+1)
            strings.append(f"{indent}Item {idx+1}: {nested_string}")
    else:
        strings.append(f"{indent}{obj}")
        
    return ", ".join(strings)

# This function takes a user profile and his question/goal
# Then we execute the langflow flow to get the AI response
# The flow is defined in movie-flow.json
# Flow explenation:
# The flow starts with two inputs (profile and goal), then we use a prompt template to format the input for the LLM
# A first LLM (llama3.2:1b) is used to generate the name of a movie that matches the user profile and goal
# The first LLM only returns the movie name, because if we ask too much (actors, directors, prizes, etc) it tends to "hallucinate" and invent wrong information
# So we use Wikipedia API to get the real information about the movie
# Finally we use a second LLM (llama3.2:1b) to generate a warm response to the user, using the facts from Wikipedia and linking it to the user profile and goal.
def ask_ai(profile, goals): 
    TWEAKS = {
            "TextInput-XmWEY": {
                "input_value": goals
            },
            "TextInput-hjcVH": {
                "input_value": dict_to_string(profile)
            },
    }
    
    result = run_flow_from_json(flow="movie-flow.json",input_value="message",fallback_to_env_vars=False,tweaks=TWEAKS)

    return result[0].outputs[0].results["text"].data["text"]