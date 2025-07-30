# app.py
from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Dummy login data for testing
VALID_USERS = {
    "SnuggleTail": "9943",
    "RyanBlue": "1234"
}

@app.route('/')
def home():
    return render_template("index.html")

@app.route('/login', methods=['POST'])
def login():
    username = request.form['username']
    pin = request.form['pin']

    if username in VALID_USERS and VALID_USERS[username] == pin:
        return redirect(url_for('pet_dashboard', username=username))
    else:
        return "Login failed. Please try again."

@app.route('/pet/<username>')
def pet_dashboard(username):
    return f"Welcome back, {username}! Your pet missed you 💙"

if __name__ == '__main__':
    app.run(debug=True)
