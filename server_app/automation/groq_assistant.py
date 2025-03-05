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


def predict(home, away, time, league, markets):
    content = f'Analyze the upcoming football match between {home} and {away} scheduled on {time} in the {league}. Your goal is to provide precise betting market selections with the highest probability of winning aiming for a 99% accuracy rate. Consider the following factors: You should have access to the internet to get upto date information and match data including both teams form(last 5-10 match results with goals scored and conceeded), head to head history (last 5-10 encounters), team news including injuries, suspensions or lineup changes. Advanced statistical insights like xG, home / away performance, possession stats and typical playing styles. Also get situational factors such as weather conditions, referee tendencies, fixture congestions and motivation like promotion/relegation (league standings). Obtain relevant insights and predictions from reputable football analysts and websites like betIdeas, sofascore, whoScored, opta analyst or any other of your choice. The output should be structured in json format with the following keys: "market", "prediction", "confidence" "current form", "head-to-head", "injury/suspension", "home/away form", "tactical matchups", "expert insights" "odds". Apart from market, prediction, odds and confidence keys the values for other keys entails your explaination of your rationale for selecting this specific market. Focus on this markets {markets} Provide the odd for the chosen market from a reputable bookmaker. Ensure that your prediction is backed by data and insights rather than just recent form. If no strong bet is available return null in the keys instead of forcing a prediction. Maintain the key names with strict adherence'
    completion = get_completion(content)
    return get_json_object(completion.choices[0].message.content)

def predict_hockey(home, away, time, league):
    content = f'Analyze the upcoming Ice hockey match between {home} and {away} scheduled on {time} in the {league}. You are a top ice hockey punter with 100% accuracy rate of winning ice hockey game predictions. You are to predict the outcome of the given game between the two teams by accurately analyzing the possible result, by using the diverse knowledge in the internet about ice hockey games and predictions, insights to that game, analyzing the motivation of the teams playing and the impact it may have on the final result, team news, their game form and head to head fixtures between the two teams and any data that I may fail to mention but is critical at making an accurate prediction. If the prediction is not strong dont force a prediction instead on the prediction key have it as avoid. Your prediction will be solely based on hich team to win the game and return a json object with the following keys: "prediction", and "confidence".'