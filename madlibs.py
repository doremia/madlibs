"""A madlib game that compliments its users."""

from random import choice

from flask import Flask, render_template, request

# "__name__" is a special Python variable for the name of the current module.
# Flask wants to know this to know what any imported things are relative to.
app = Flask(__name__)

AWESOMENESS = [
    'awesome', 'terrific', 'fantastic', 'neato', 'fantabulous', 'wowza',
    'oh-so-not-meh', 'brilliant', 'ducky', 'coolio', 'incredible', 'wonderful',
    'smashing', 'lovely',
]


@app.route('/')
def start_here():
    """Display homepage."""

    return "Hi! This is the home page."


@app.route('/hello')
def say_hello():
    """Say hello to user."""

    return render_template("hello.html")

@app.route('/game')
def show_madlib_form():
    """Ask user if they want to play a game."""

    choice = request.args.get("choice") # what route is the render compliment
    if choice == "yes":
        return render_template("game.html")

    else:
        return render_template("goodbye.html")


    # return render_template("compliment.html",
    #                        choice=choice)

@app.route('/madlib')
def show_madlib():

    firstname = request.args.get("firstname")
    noun = request.args.get("noun")
    adj = request.args.get("adj")
    country = request.args.getlist("country")


    return render_template("madlib.html",
        firstname=firstname,noun=noun,adj=adj,country=country)


@app.route('/goodbye')
def say_goodbye():
    """Get the user's response"""
    return render_template("goodbye.html")



@app.route('/greet')
def greet_person():
    """Greet user with compliment."""

    player = request.args.get("person")

    compliment = choice(AWESOMENESS)

    return render_template("compliment.html",
                           person=player,
                           compliment=compliment)


if __name__ == '__main__':
    # Setting debug=True gives us error messages in the browser and also
    # "reloads" our web app if we change the code.

    app.run(debug=True)
