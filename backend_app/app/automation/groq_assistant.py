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
    content = f'Your task is to analyze the upcoming football match between {home} and {away} scheduled on {time} in {league}. Our statistical algorithm has already shortlisted this match as a strong candidate for the {markets} markets based on historical success rates (over 70% probability). \n\nNow, using real-time data available on the internet, including current team form (last 5–10 matches with goals scored and conceded), head-to-head history (last 5–10 encounters), injury/suspension updates, lineup changes, weather conditions, referee tendencies, fixture congestion, and any other relevant situational factors, please perform a comprehensive analysis.\n\nEvaluate the following:\n1. Confirm if the either {markets} market remains the best option.\n2. Alternatively, determine if another betting market (e.g., Both Teams to Score, Favorite Team to Win) might offer a higher expected value given current conditions.\n3. Assess all relevant advanced statistics (xG, possession stats, home/away performance, tactical matchups) and incorporate insights from reputable sources (e.g., betIdeas, sofascore, whoScored, Opta).\n\nThe output must be in strict JSON format with these keys:\n- \"market\": The name of the recommended betting market.\n- \"prediction\": Your prediction for the recommended market.\n- \"confidence\": A numerical value representing your confidence level (0–1 or percentage) in the prediction.\n- \"current form\": An explanation of the teams recent performances.\n- \"head-to-head\": A summary of the head-to-head history between the teams.\n- \"injury/suspension\": Relevant details on player availability.\n- \"home/away form\": Insights into how the teams perform at home versus away.\n- \"tactical matchups\": Analysis of how the teams playing styles interact.\n- \"expert insights\": Any relevant expert opinions or data-backed insights.\n- \"odds\": \"Odds from a reputable bookmaker\" (only the value).\n\nIf no strong bet is available, return null for the keys that would otherwise provide a prediction, but still include all key names. Focus on delivering a data-backed recommendation that builds on our algorithm’s insights, ensuring that your prediction is as accurate as possible.\n If there is no viable strong bet or low confidence dont force a prediction instead return None as the only value \nMake sure your response follows the structure exactly, with no extra keys or text.\"\n'
    completion = get_completion(content)
    return get_json_object(completion.choices[0].message.content)

def predict_hockey(home, away, time, league):
    content = f'Analyze the upcoming Ice hockey match between {home} and {away} scheduled on {time} in the {league}. You are a top ice hockey punter with 100% accuracy rate of winning ice hockey game predictions. You are to predict the outcome of the given game between the two teams by accurately analyzing the possible result, by using the diverse knowledge in the internet about ice hockey games and predictions, insights to that game, analyzing the motivation of the teams playing and the impact it may have on the final result, team news, their game form and head to head fixtures between the two teams and any data that I may fail to mention but is critical at making an accurate prediction. If the prediction is not strong dont force a prediction instead on the prediction key have it as avoid. Your prediction will be solely based on hich team to win the game and return a json object with the following keys: "prediction", and "confidence".'