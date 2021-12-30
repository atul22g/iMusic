from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    return render_template('index.html')

@app.route("/song")
def song():
    return render_template('song.html')

@app.route("/content")
def content():
    return render_template('content.html')

@app.route("/log-in")
def login():
    return render_template('log-in.html')

@app.route("/create_account")
def create_account():
    return render_template('create_account.html')

@app.route("/forget_Password")
def forget_Password():
    return render_template('forget_Password.html')

@app.route("/Use_phone_no")
def Use_phone_no():
    return render_template('Use_phone_no.html')

app.run(debug=True)