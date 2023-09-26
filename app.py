from flask import Flask, render_template, request
import random

import os

app = Flask(__name__, static_url_path='/static')

@app.route('/')
def index():
    image_path = os.path.join(app.root_path, 'static', 'images', 'rock.jpg')
    print(image_path)
    

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/play', methods=['POST'])
def play():
    choices = ["rock", "paper", "scissors"]

    player_choice = request.form['choice']
    computer_choice = random.choice(choices)

    result = determine_winner(player_choice, computer_choice)

    return render_template('result.html', player_choice=player_choice, computer_choice=computer_choice, result=result)

def determine_winner(player_choice, computer_choice):
    if player_choice == computer_choice:
        return "It's a tie!"
    elif (
        (player_choice == "rock" and computer_choice == "scissors")
        or (player_choice == "paper" and computer_choice == "rock")
        or (player_choice == "scissors" and computer_choice == "paper")
    ):
        return "Congratulations! You win!"
    else:
        return "Sorry! You lose."

if __name__ == '__main__':
    app.run(debug=True)