from groq import Groq
import os
import json

client = Groq(
    api_key=os.environ.get("GROQ_API_KEY"),
)

def get_completion(content):
    return client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[
            {
                "role": "user",
                "content": content 
            },
        ],
        temperature=1,
        max_completion_tokens=1024,
        top_p=1,
        stream=False,
        response_format={"type": "json_object"},
        stop=None,
    )

def get_json_object(response_text):
    try:
        response_json = json.loads(response_text)  
        return response_json 
    except json.JSONDecodeError as e:
        print("JSON Decode Error:", e)
        return {}


def predict(home, away, markets):
    content = f"You are an expert in Football (soccer) betting and have diverse upto date knowledge of football.\nYou are tasked to do extensive research on the given game and identify the best market to bet on that market, this includes analysing every important details that can assist you in making the prediction which stands a high chance of winning.\nYou may use reliable sources that talk about football betting to gather public opinion to make comparison with your judgement of the prediction you made.\nYou will be provided with possible markets to predict on but you are not limited to make prediction on those markets as your key responsiblity is to assess and find the best winning market and make prediction on it.\nYou are to find the odds of that market that is common among different bookies.\nYou will return a json object containing the following keys: 'prediction', 'reason' 'odds' and not extra word.\n\nGame: {home} v {away} \nPossible Markets: {markets}"
    completion = get_completion(content)
    return get_json_object(completion.choices[0].message.content)