from flask import Flask, request, jsonify, render_template

app = Flask(__name__)

def chatbot_response(message):
    message = message.lower()
    if message == "hello":
        return "Hi!"
    elif message == "how are you":
        return "I'm fine, thanks!"
    elif message == "bye":
        return "Goodbye!"
    else:
        return "I don't understand that."

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/get", methods=["GET"])
def get_response():
    user_msg = request.args.get("msg")
    return jsonify({"response": chatbot_response(user_msg)})

if __name__ == "__main__":
    app.run(debug=True)
