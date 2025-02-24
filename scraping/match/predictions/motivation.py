from groq import Groq
import os
import json

client = Groq(
    api_key=os.environ.get("GROQ_API_KEY"),
)

def match_motivation(home, away):
    completion = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[
            {
                "role": "user",
                "content": f"You are the world leading betting expert with almost 100% winning rate and you are fit to analyse and make sports betting predictions based on a teams match motivation. You are tasked to find team motivations towards a given match and with the finding use it to analyse and make predictions on the most guaranteed markets to win and avoid markets that are unpredictable. You will return a json objects with the following keys: 'market to bet', 'market to avoid' 'reason'. Note only return the object and nothing else.\nProvided {home} v {away}"
            }
        ],
        temperature=1,
        max_completion_tokens=1024,
        top_p=1,
        stream=True,
        stop=None,
    )

    response_text = ""  

    for chunk in completion:
        if chunk.choices[0].delta.content:
            response_text += chunk.choices[0].delta.content  

    try:
        response_json = json.loads(response_text.strip())  
        return response_json
    except json.JSONDecodeError:
        return {}
