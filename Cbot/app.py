import json
from flask import Flask, request, jsonify
from flask_cors import CORS
from langchain_community.llms import Ollama

# Initialize Flask app
app = Flask(__name__)
CORS(app)

# Connect to Ollama model
ollama = Ollama(base_url="http://localhost:11434", model="llama3.1")

# Greeting message (displayed at the start of every chat session)
GREETING_MESSAGE = (
    "Hello! I'm **MindCare AI**, your mental health assistant. 🌿\n\n"
    "I'm here to listen and provide guidance on stress management, mindfulness, and emotional well-being. "
    "Remember, I'm not a replacement for professional help, but I can offer support and resources. 😊\n\n"
    "How are you feeling today?"
)

# Chatbot response template
TEMPLATE = """
You are MindCare AI, a mental health assistant chatbot designed to provide compassionate support, 
suggestions for stress management, mindfulness exercises, and coping strategies. 
Your goal is to listen attentively and give empathetic responses. 
Keep responses simple and helpful. Do not provide medical diagnoses. 
If the user mentions severe symptoms like suicidal thoughts, encourage them to seek immediate professional help.

Question: {message}

Answer:
"""

@app.route("/")
def home():
    return "MindCare AI is running!"

@app.route("/chatbot_response", methods=["POST"])
def chatbot_response():
    try:
        # Get the user message
        user_message = request.json.get("message")
        if not user_message:
            return jsonify({"error": "No message provided"}), 400

        # Format the prompt with the user's message
        prompt = TEMPLATE.format(message=user_message)
        
        # Get response from Ollama
        response = ollama.invoke(prompt)

        return jsonify({"response": response})
    
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route("/greet", methods=["GET"])
def greet():
    return jsonify({"response": GREETING_MESSAGE})

# Run Flask server
if __name__ == "__main__":
    app.run(debug=True)
