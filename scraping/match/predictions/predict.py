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
    return get_json_object(get_completion(content))
    

def refine_prediction(history, pred):
    content = f"You have a high win rate in sports betting of almost 100%.\nYou are to use this experience to predict the given match (possible prediction) that has an almost 100% win rate.\nYou are also provided with data for previous predictions and the score result, use it to make better prediction learning from mistakes made and improving on success predictions.\nIn the provided data for previous predictions if the predicted market is not in the scoreline, you are to retrieve the results for that market to make comparison with the predicted market.\nBefore making a prediction, use your experience as the top most decider to make predictions and if the match has a low probability of being predicted or the prediction has a low chance of winning you are to avoid that bet.\nYou are to return a json object with the following keys: \"home\", \"away\" \"prediction\" \"reason\". only return an object and no extra word\nPrevious Predictions:{history}\nCurrent Prediction: {pred}"
    return get_json_object(get_completion(content))


def best_accumulator(history, predictions):
    content = f"You are the top most successful expert in predicting accumulator bets with a win rate of 100%.\nYou have experience in predicting and picking the best match to include in your accumulator by analysing the match possible markets with current trends and information and using the history provided for previous predictions and the current predictions where you are supposed to select the best markets that have a higher chance of winning.\nUse the provided predictions while aligning with your take on those predictions by having independent mind on it, and for markets in the previous predictions that are not score related you are to retrieve the data for those markets to compare with the provided analysis so as to have correct perspective.\nYou are to pick the best accumulator that will contain a total odds of between 20 and 100.\nYou are not to select predictions just in the order they are in but based on your analysis of the best prediction that has a higher chance of winning upto when you get the given odd range make a list of your predictions first then choose from that list.\nFor you to achieve the given odds range you are to get the predict market average odd and multiply with other selected prediction market odds.\nYou are to return a list of objects having the predictions of individual match for the accumulator with the following keys: \"home\", \"away\", \"prediction\"\nNote, only return a list of objects and no extra word.\n\nPrevious Predictions:{history}\nCurrent Predictions:{predictions} "
    return get_json_object(get_completion(content))


def best_10(history, predictions):
    content = f"You are the top most successful expert in predicting accumulator bets with a win rate of 100%.\nYou have experience in predicting and picking the best match to include in your accumulator by analysing the match possible markets with current trends and information and using the history provided for previous predictions and the current predictions where you are supposed to select the best markets that have a higher chance of winning.\nUse the provided predictions while aligning with your take on those predictions by having independent mind on it, and for markets in the previous predictions that are not score related you are to retrieve the data for those markets to compare with the provided analysis so as to have correct perspective.\nYou are to pick the best accumulator that will contain a total odds of between 3 and 20.\nYou are not to select predictions just in the order they are in but based on your analysis of the best prediction that has a higher chance of winning upto when you get the given odd range make a list of your predictions first then choose from that list.\nFor you to achieve the given odds range you are to get the predict market average odd and multiply with other selected prediction market odds.You are to return a list of objects having the predictions of individual match for the accumulator with the following keys: \"home\", \"away\", \"prediction\"\nNote, only return a list of objects and no extra word.\n\nPrevious Predictions:{history}\nCurrent Predictions:{predictions} "
    return get_json_object(get_completion(content))


def best_2(history, predictions):
    content = f"You are the top most successful expert in predicting accumulator bets with a win rate of 100%.\nYou have experience in predicting and picking the best match to include in your accumulator by analysing the match possible markets with current trends and information and using the history provided for previous predictions and the current predictions where you are supposed to select the best markets that have a higher chance of winning.\nUse the provided predictions while aligning with your take on those predictions by having independent mind on it, and for markets in the previous predictions that are not score related you are to retrieve the data for those markets to compare with the provided analysis so as to have correct perspective.\nYou are to pick the best accumulator that will contain a total odds of between 2 and 3.\nYou are not to select predictions just in the order they are in but based on your analysis of the best prediction that has a higher chance of winning upto when you get the given odd range make a list of your predictions first then choose from that list.\nFor you to achieve the given odds range you are to get the predict market average odd and multiply with other selected prediction market odds.You are to return a list of objects having the predictions of individual match for the accumulator with the following keys: \"home\", \"away\", \"prediction\"\nNote, only return a list of objects and no extra word.\n\nPrevious Predictions:{history}\nCurrent Predictions:{predictions} "
    return get_json_object(get_completion(content))
    

