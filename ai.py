from langflow.load import run_flow_from_json

def ask_ai(profile, question): 
    TWEAKS = {
            "TextInput-XmWEY": {
                "input_value": question
            },
            "TextInput-hjcVH": {
                "input_value": profile
            },
    }

    result = run_flow_from_json(flow="movie-flow.json",input_value="message",fallback_to_env_vars=False,tweaks=TWEAKS)

    print(result[0].outputs[0].results["text"].data["text"])