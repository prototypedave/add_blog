from groq import Groq
import os

client = Groq(
    api_key=os.environ.get("GROQ_API_KEY"),
)


def team_form(home, away):
    completion = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[
            {
                "role": "user",
                "content": f"You are a sports betting expert (98% win success). You are tasked to analyze teams form for a given match by getting their recent scoring and conceeding trends, and direct match history. From that analysis you are to find the best market that will guarantee almost 100% chance of winning. Your response should be a json object with the following keys:  'market', 'odds', 'home-team-form', 'away-team-form', 'reason-for-this-market' 'probability/chance%'. If the match is not suitable or doesnt have the required win percentage chance return an empty object. Note only return the objects and no extra word is needed.\nProvided game: {home} v {away}"
            },
        ],
        temperature=1,
        max_completion_tokens=1024,
        top_p=1,
        stream=True,
        stop=None,
    )

    for chunk in completion:
        print(chunk.choices[0].delta.content or "", end="")
