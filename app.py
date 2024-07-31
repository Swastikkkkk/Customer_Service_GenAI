from flask import Flask, render_template, request, redirect, url_for, session,flash
from chatbot import get_Chat_response

app = Flask(__name__)
app.secret_key = "ChatBotBOB_devansh"

@app.route("/")
def index():
    return redirect(url_for("chat_page"))

@app.route("/chat",methods=['POST','GET'])
def chat_page():
    return render_template('chat.html')

@app.route("/chat/get", methods=["GET", "POST"])
def chat():
    msg = request.form["msg"]
    input = msg
    return get_Chat_response(input)
        
if __name__ == '__main__':
    app.run(debug=True)