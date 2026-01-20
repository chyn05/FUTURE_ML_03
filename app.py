
from flask import Flask, request, jsonify, render_template
import sqlite3

app = Flask(__name__)

def init_db():
    conn = sqlite3.connect("chat.db")
    c = conn.cursor()
    c.execute("""CREATE TABLE IF NOT EXISTS chats (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        user TEXT,
        bot TEXT
    )""")
    conn.commit()
    conn.close()

def save_chat(user, bot):
    conn = sqlite3.connect("chat.db")
    c = conn.cursor()
    c.execute("INSERT INTO chats (user, bot) VALUES (?,?)", (user, bot))
    conn.commit()
    conn.close()

def bot_reply(msg):
    msg = msg.lower()
    if "hello" in msg or "hi" in msg:
        return "Hello! How can I help you today?"
    elif "order" in msg:
        return "Please share your order ID."
    elif "refund" in msg:
        return "Refunds are processed within 5–7 business days."
    elif "contact" in msg:
        return "You can contact support at support@example.com"
    else:
        return "Sorry, I did not understand. Can you rephrase?"

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/chat", methods=["POST"])
def chat():
    user_msg = request.json.get("message")
    reply = bot_reply(user_msg)
    save_chat(user_msg, reply)
    return jsonify({"reply": reply})

if __name__ == "__main__":
    init_db()
    app.run(debug=True)
