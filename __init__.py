import Game
from flask import Flask, render_template


app = Flask(__name__)

@app.route('/')
def login():
    """@brief This is a flask route for the first page

    This routes the user to a login page that renders
    login.html. The user will have to submit a username and password.
    @param : none
    """
    return render_template('login.html')

@app.route('/home')
def home():
    """@brief This is a flask route for the homepage

    Once the user is logged in, it will route them to the home screen
    which renders the home.html page.
    @param : none
    """
    return render_template('home.html')

@app.route('/play')
def play():
    """@brief This is a flask route for the play page

    If the user selects the play tab in the navbar, they will be
    routed to the play page which renders play.html.
    @param : none
    """
    return render_template('play.html')

@app.route('/about')
def about():
    """@brief This is a flask route for the about page

    If the user selects the about tab in the navbar they will be routed
    to the about page which renders about.html.
    @param : none
    """
    return render_template('about.html')

@app.route('/resetPass')
def resetPass():
    """@brief This is a flask route for the password reset page

    If the user forgets their password on the login page, they can click a button
    to redirect them here
    @param : none
    """
    return render_template('resetPass.html')

@app.route('/signUp')
def signUp():
    """@brief This is a flask route for the sign up page

    The user can sign up for an account; upon success, it will redirect them to the home page
    @param : none
    """
    return render_template('signUp.html')

if __name__ == '__main__':
    app.run(debug=True)
    ourgame = Game.Game()
    ourgame.gameloop()
