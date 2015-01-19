from RunCmd import RunCmd
from flask import Flask, request

app = Flask(__name__)

@app.route("/run")
def run():
    command = request.values.get("command")
    print command
    return RunCmd(command, 1).Run()

app.run(host="0.0.0.0", port=8000)

