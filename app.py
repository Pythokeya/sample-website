from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello World!</p>"

SERVER_NAME = "Karthikeya"

if __name__ == "__main__":
    app.run('0.0.0.0', 2010, True)