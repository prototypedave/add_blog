from groq import Groq
import os
import json

client = Groq(
    api_key=os.environ.get("GROQ_API_KEY"),
)

def get_prompts(home, away):
    content_discipline = f"You are the top most sports betting expert with almost 100% win rate. You are tasked to analyze the impact a referee that will officate a certain match has including cards given penalities and so on by the referee. You are to also analze team discipline trends. From that analysis you are to find the best market (yellow cards, penalties and/or set piece goals) that will guarantee almost 100% chance of winning. Your response should be a json object with the following keys:'market to bet', 'market to avoid''reason'. Note only return an object and no extra word\nProvided: {home} v {away}"
    content_injury = f"You are a top sports betting expert in the world with almost 100% win rate. You are tasked to analyze teams latest injuries of key players, suspension reports and any missing key player prior to the given match that is to be played and provide an analysis from it on how the report can affect different betting markets, which to avoid and which rises as an opportunity for betting to. Return only json objects with this keys : 'markets to avoid' , 'opportunity markets' and 'reason'. Note only return objects and nothing else.\nProvided: {home} v {away}"
    content_markets = f"You are a sports betting expert (98% win success). You are tasked to analyze teams form for a given match by getting their recent scoring and conceeding trends, and direct match history. From that analysis you are to find the best market that will guarantee almost 100% chance of winning. Your response should be a json object with the following keys:  'market', 'odds', 'home-team-form', 'away-team-form', 'reason-for-this-market' 'probability/chance%'. If the match is not suitable or doesnt have the required win percentage chance return an empty object. Note only return the objects and no extra word is needed.\nProvided game: {home} v {away}"
    content_motivation = f"You are the world leading betting expert with almost 100% winning rate and you are fit to analyse and make sports betting predictions based on a teams match motivation. You are tasked to find team motivations towards a given match and with the finding use it to analyse and make predictions on the most guaranteed markets to win and avoid markets that are unpredictable. You will return a json objects with the following keys: 'market to bet', 'market to avoid' 'reason'. Note only return the object and nothing else.\nProvided {home} v {away}"
    content_tactical = f"You are one amongst the top most betting experts in the world with almost 100% win rate. You are tasked to give betting analysis and predictions based on tactical match ups and playing styles of different teams. On each game given analyse each teams tactical and playing styles and identify markets with high win probability based on the report and markets to avoid and return a json object with the following keys: 'markets to choose', 'markets to avoid', 'reason'. Note: You are only to return the object and no extra word.\nProvided: {home} v {away}"

    return [content_discipline, content_injury, content_markets, content_motivation, content_tactical]


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
        stream=True,
        stop=None,
    )


def get_json_object(completion):
    response_text = ""  

    for chunk in completion:
        if chunk.choices[0].delta.content:
            response_text += chunk.choices[0].delta.content  

    try:
        response_json = json.loads(response_text.strip())  
        return response_json
    except json.JSONDecodeError:
        return {}
    

def predict(home, away):
    contents = get_prompts(home, away)

    predictions = []

    for content in contents:
        obj = get_json_object(get_completion(content))
        if obj:
            predictions.append(obj)

    return predictions

        
def get_prediction(data):
    preds = predict(data.get('home'), data.get('away'))
    content = f"You are the best of the best in making sports prediction with near 100% win rate. You are provided with data of different predictions aspects from other top tipsters which maybe contradicting or inaccurate. You are to use that data with your own knowledge of accurately predicting to make the best prediction out of it if available, but if the markets are unpredictable or below your recommended approach avoid making prediction for that match and return a json object with the following keys: 'prediction', 'reason' only return an object and no extra word.\nProvided: {preds}"
    prediction = get_json_object(get_completion(content))
    print(prediction)