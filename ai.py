from langflow.load import run_flow_from_json

def dict_to_string(obj,level=0):
    strings=[]
    indent = " " * level

    if isinstance(obj, dict):
        for key,value in obj.items():
            if isinstance(value,(dict,list)):
                nested_string = dict_to_string(value,level+1)
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