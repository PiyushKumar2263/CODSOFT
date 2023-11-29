import random

def rule_based_chatbot(user_input):
    user_input = user_input.lower()

    # Define rules and responses
    rules = {
        'greeting': ['Hello! How can I assist you today?', 'Hi there!', 'Hey!'],
        'farewell': ['Goodbye! Have a great day.', 'See you later!', 'Farewell!'],
        'thanks': ['You\'re welcome!', 'No problem!', 'Happy to help!'],
        'yes': ['Great!', 'Awesome!', 'Fantastic!'],
        'no': ['Okay, let me know if you change your mind.', 'No worries!', 'Sure thing.'],
        'help': ['I can provide information and answer questions. What do you need help with?', 'How can I assist you today?', 'Ask me anything!'],
        'weather': ['I\'m sorry, I don\'t have real-time weather information. You can check a weather website for that.'],
        'joke': ['Why don’t scientists trust atoms? Because they make up everything!', 'I told my wife she should embrace her mistakes. She gave me a hug.'],
        'age': ['I am a computer program, so I don\'t have an age.'],
        'name': ['You can call me Alice!', 'I don\'t have a personal name, but you can call me whatever you like.'],
    }

    # Check user input against rules
    if any(keyword in user_input for keyword in ['hello', 'hi', 'hey']):
        return random.choice(rules['greeting'])
    elif any(keyword in user_input for keyword in ['bye', 'goodbye']):
        return random.choice(rules['farewell'])
    elif any(keyword in user_input for keyword in ['thanks', 'thank you']):
        return random.choice(rules['thanks'])
    elif any(keyword in user_input for keyword in ['yes', 'yeah', 'yep']):
        return random.choice(rules['yes'])
    elif any(keyword in user_input for keyword in ['no', 'nope']):
        return random.choice(rules['no'])
    elif any(keyword in user_input for keyword in ['help', 'info']):
        return random.choice(rules['help'])
    elif 'weather' in user_input:
        return random.choice(rules['weather'])
    elif any(keyword in user_input for keyword in ['joke', 'funny']):
        return random.choice(rules['joke'])
    elif any(keyword in user_input for keyword in ['age']):
        return random.choice(rules['age'])
    elif any(keyword in user_input for keyword in ['name']):
        return random.choice(rules['name'])
    else:
        return "I'm sorry, I don't understand. Can you please rephrase or ask something else?"

# Example usage
while True:
    user_input = input("You: ")
    if user_input.lower() in ['exit', 'quit', 'bye']:
        print("Bot: Goodbye!")
        break
    response = rule_based_chatbot(user_input)
    print("Bot:", response)
