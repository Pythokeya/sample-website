from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def hello_world():
    return render_template('home.html')

SERVER_NAME = "jobec"

if __name__ == "__main__":
    app.run('0.0.0.0', 2010, True)