from flask import Flask, redirect, render_template, url_for, request, jsonify
import psycopg2
import random

connect = psycopg2.connect(
    database="zvkklrad",
    user="zvkklrad",
    password="JPyYJiOpDoO74LVugWuXdfoNqV85jHbG",
    host="john.db.elephantsql.com",
    port="5432"
)

cursor = connect.cursor()

lives =6
word = []
answer = []
hint = ""

app = Flask(__name__)
app = Flask(__name__, template_folder='templates')

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

    global word, answer, lives, hint, question
    number = random.randint(0, len(data) - 1)
    question = data[number][1]
    word = list(question)
    answer = []
    lives = 6
    hint = data[number][2]


    return render_template("game.html", title="Main", hint=hint, lives=lives, len=len(question))

@app.route('/game', methods=['POST'])
def game():
    print(request.form)
    userChar = request.form.get("answer")

    global lives, answer
    if len(answer) != len(word):
        for i in range(len(word)):
            answer.append("_")

    if userChar not in word:
        lives -= 1
    
    elif userChar in word:
        for i in range(len(word)):
            if word[i] == userChar:
                answer[i] = userChar
    
    if "_" not in answer:
        return "You Win <a href='/main'>Start new game</a>"

    print(userChar, word, answer)
    if lives <= 0:
        return "You Lose"
    else:
        return render_template("gameRun.html", title="Game", hint=hint, lives=lives, answer=answer)

if __name__ == '__main__':
    app.run(debug=True, port=3000)