from groq import Groq
import os
import json

client = Groq(
    api_key=os.environ.get("GROQ_API_KEY"),
)


def predict_discipline(home, away):
    completion = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[
            {
                "role": "user",
                "content": f"You are the top most sports betting expert with almost 100% win rate. You are tasked to analyze the impact a referee that will officate a certain match has including cards given penalities and so on by the referee. You are to also analze team discipline trends. From that analysis you are to find the best market (yellow cards, penalties and/or set piece goals) that will guarantee almost 100% chance of winning. Your response should be a json object with the following keys:'market to bet', 'market to avoid''reason'. Note only return an object and no extra word\nProvided: {home} v {away}"
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

