from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    return render_template('home.html')

@app.route("/apply")
def apply_page():
    return render_template('apply.html')

@app.route("/post")
def post_page():
    return render_template('post.html')

SERVER_NAME = "jobec"

if __name__ == "__main__":
    app.run('0.0.0.0', 2010, True)