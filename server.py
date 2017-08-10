from flask import Flask
from flask import render_template
import start
import time

app = Flask(__name__)

@app.route("/")
def index():
	return render_template("index.html")

@app.route("/mahmoud")
def dispense():
	start.runServo(20)
	return "<html><body><h1>It is serving right now, go get it</h1></body></html>"

if __name__ == "__main__":
	app.run(host="172.20.84.157", port=80)
