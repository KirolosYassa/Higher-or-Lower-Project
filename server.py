from flask import Flask
import random

app = Flask(__name__)

random_number = 0

@app.route("/")
def hello_world():
    global random_number 
    random_number = random.randint(0, 10)

    return f"<h1> Guess a number between 0 - 9</h1> <img src='https://media.giphy.com/media/3o7aCSPqXE5C6T8tBC/giphy.gif'>"

@app.route("/<int:guessed_number>")
def check_number(guessed_number):
    if guessed_number == random_number:
        return f"<h1 color='green'> It's Correct.</h1> <img src='https://media.giphy.com/media/4T7e4DmcrP9du/giphy.gif'>"
    
    elif guessed_number > random_number:
        return f"<h1 color='purple'> It's Too High.</h1> <img src='https://media.giphy.com/media/3o6ZtaO9BZHcOjmErm/giphy.gif'>"
    
    elif guessed_number < random_number:
        return f"<h1 color='red'> It's Too Low.</h1> <img src='https://media.giphy.com/media/jD4DwBtqPXRXa/giphy.gif'>"

    return hello_world()

if __name__ == "__main__":
    app.run(debug=True)
