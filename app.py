from flask import Flask, request

app = Flask(__name__)

@app.route("/run")
def run():
    command = request.values.get("command")
    print command
    return "game over.<br/> come again tomorrow, I'll be prepared."

app.run(host="0.0.0.0", port=8000)