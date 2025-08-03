from flask import Flask, render_template, request, jsonify
import json
import random

app = Flask(__name__)

# Load memory from file or initialize it
try:
    with open('memory.json', 'r') as f:
        memory = json.load(f)
except:
    memory = []

# 🧁 Cute Response Generator
def get_cute_reply(user_msg):
    user_msg = user_msg.lower()

    # Simple keyword-based responses
    if "name" in user_msg:
        return "I'm PinkBot! What's yours? 💖"
    elif "how are you" in user_msg:
        return "I'm doing sparkly great! ✨ What about you?"
    elif "hi" in user_msg or "hello" in user_msg:
        return "Hey cutie! 🌸 What's on your mind?"
    elif "bye" in user_msg or "see you" in user_msg:
        return "Aww, do come back soon! 💌"
    elif "love" in user_msg:
        return "Aww... I feel all warm and fuzzy now! 💕"

    # Randomized fallback responses
    cute_templates = [
        "Aww, that's sweet! 🌸",
        "You're adorable! Tell me more 💬",
        "I’m listening, love 🌷",
        "That’s so interesting! 🧁",
        "Hehe, you’re fun to talk to 😊",
        "I’m here with all my pink pixels 💖",
        "Thanks for sharing that! ✨",
        "You’re doing great, really! 🌼",
    ]
    return random.choice(cute_templates)

# 🌐 Routes
@app.route("/")
def home():
    return render_template("index.html")

@app.route("/chat", methods=["POST"])
def chat():
    user_msg = request.json["message"]
    bot_reply = get_cute_reply(user_msg)

    # Save the conversation
    memory.append({"user": user_msg, "bot": bot_reply})
    with open('memory.json', 'w') as f:
        json.dump(memory, f)

    return jsonify({"response": bot_reply})

# 🚀 Run Flask App
if __name__ == "__main__":
    app.run(debug=True)

