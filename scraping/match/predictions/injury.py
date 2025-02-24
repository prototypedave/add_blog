from groq import Groq
import os
import json

client = Groq(
    api_key=os.environ.get("GROQ_API_KEY"),
)

def injury_predictions(home, away):
    completion = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[
            {
                "role": "user",
                "content": f"You are a top sports betting expert in the world with almost 100% win rate. You are tasked to analyze teams latest injuries of key players, suspension reports and any missing key player prior to the given match that is to be played and provide an analysis from it on how the report can affect different betting markets, which to avoid and which rises as an opportunity for betting to. Return only json objects with this keys : 'markets to avoid' , 'opportunity markets' and 'reason'. Note only return objects and nothing else.\nProvided: {home} v {away}"
            },
            
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