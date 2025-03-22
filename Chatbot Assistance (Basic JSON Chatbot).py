import json

with open("chatbot_data.json") as f:
    chatbot_responses = json.load(f)

def chatbot_response(user_input):
    return chatbot_responses.get(user_input.lower(), "Sorry, I don't have information on that.")
