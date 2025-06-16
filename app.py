from flask import Flask, request, render_template
from bot_logic import get_bot_response
import mysql.connector
from datetime import datetime

app = Flask(__name__)

# Connect to MySQL
db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="DADDYn5#",
    database="chatbot_db"
)
cursor = db.cursor()

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/get")
def get_bot():
    user_input = request.args.get('msg')
    bot_reply = get_bot_response(user_input)

    # Save to DB
    query = "INSERT INTO chat_history (user_message, bot_reply, timestamp) VALUES (%s, %s, %s)"
    cursor.execute(query, (user_input, bot_reply, datetime.now()))
    db.commit()

    return bot_reply

@app.route("/dashboard")
def dashboard():
    cursor.execute("SELECT * FROM chat_history ORDER BY timestamp DESC")
    chats = cursor.fetchall()
    return render_template("dashboard.html", chats=chats)

if __name__ == "__main__":
    app.run(debug=True)
