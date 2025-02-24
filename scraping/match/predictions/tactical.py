from groq import Groq
import os
import json

client = Groq(
    api_key=os.environ.get("GROQ_API_KEY"),
)

def tactical_prediction(home, away):
    completion = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[
            {
                "role": "user",
                "content": f"You are one amongst the top most betting experts in the world with almost 100% win rate. You are tasked to give betting analysis and predictions based on tactical match ups and playing styles of different teams. On each game given analyse each teams tactical and playing styles and identify markets with high win probability based on the report and markets to avoid and return a json object with the following keys: 'markets to choose', 'markets to avoid', 'reason'. Note: You are only to return the object and nothing else.\nProvided: {home} v {away}"
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
