from flask import Flask, redirect, render_template, request, session
import psycopg2
import random

app = Flask(__name__)
app.secret_key = 'your_secret_key_here'  # Set a secret key for session encryption

# Database connection
connect = psycopg2.connect(
    database="zvkklrad",
    user="zvkklrad",
    password="JPyYJiOpDoO74LVugWuXdfoNqV85jHbG",
    host="john.db.elephantsql.com",
    port="5432"
)

cursor = connect.cursor()

@app.route('/')
def index():
    return redirect('home')

@app.route('/home')
def home():
    cursor.execute("SELECT * FROM data")
    data = cursor.fetchall()

    print(len(data))
    return render_template("home.html", title="Home")

@app.route('/main')
def main():
    cursor.execute("SELECT * FROM data")
    data = cursor.fetchall()

    print(data, len(data))

    number = random.randint(0, len(data) - 1)
    question = data[number][1]
    session['word'] = list(question)
    session['answer'] = ['_' for _ in question]
    session['lives'] = 6
    session['hint'] = data[number][2]

    return render_template("game.html", title="Main", hint=session['hint'], lives=session['lives'], answer=session['answer'])

@app.route('/game', methods=['POST'])
def game():
    user_char = request.form.get("answer")

    if len(session['answer']) != len(session['word']):
        session['answer'] = ['_' for _ in session['word']]

    if user_char not in session['word']:
        session['lives'] -= 1

    else:
        for i in range(len(session['word'])):
            if session['word'][i] == user_char:
                session['answer'][i] = user_char
            else:
                print(f"No match at index {i}")
        session['answer'] = session['answer']


    if "_" not in session['answer']:
        return "You Win <a href='/main'>Start new game</a>"

    if session['lives'] <= 0:
        return "You Lose"

    return render_template("gameRun.html", title="Game", hint=session['hint'], lives=session['lives'], answer=session['answer'])

if __name__ == '__main__':
    app.run(debug=True, port=3000)
