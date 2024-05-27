import nltk
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer
import re

# Download necessary NLTK resources
nltk.download('punkt')
nltk.download('stopwords')

# Define the chatbot's responses
responses = {
    'greeting': "Hello! How can I assist you today?",
    'goodbye': "Goodbye! Have a great day.",
    'default': "I'm sorry, I didn't understand that. Could you please rephrase your question?"
}

# Define the chatbot's logic
def chatbot_response(user_input):
    # Preprocess the user's input
    user_input = user_input.lower()
    user_input = re.sub(r'[^a-zA-Z0-9\s]', '', user_input)
    words = nltk.word_tokenize(user_input)
    stop_words = set(stopwords.words('english'))
    words = [word for word in words if word not in stop_words]
    stemmer = PorterStemmer()
    words = [stemmer.stem(word) for word in words]

    # Check for keywords in the user's input
    if 'hello' in words or 'hi' in words:
        return responses['greeting']
    elif 'goodbye' in words or 'bye' in words:
        return responses['goodbye']
    else:
        return responses['default']

# Run the chatbot
while True:
    user_input = input("You: ")
    print("Chatbot:", chatbot_response(user_input))