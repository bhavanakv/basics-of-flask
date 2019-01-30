from flask import Flask, session, redirect, url_for, request
app = Flask(__name__)
app.secret_key = 'SecretKey'

@app.route("/log")
def basic():
    return "Succesfully logged out!"

@app.route("/session")
def index():
    if 'username' in session:
        username = session['username']
        return "Logged in as" + username + "<br /><a href='/logout'>Click here to logout</a>"
    return "You are not logged in" + "<br /><a href='/login'>Click here to login</a>"

@app.route("/login", methods = ['GET', 'POST'])
def login():
    if request.method == 'POST':
        session['username'] = request.form['username']
        return redirect(url_for("index"))
    return '''
        <form action="" method="post">
            <p>Enter name: <input type='text' name='username' /></p>
            <p><input type='submit' value='Submit' /></p>
    '''

@app.route("/logout")
def logout():
    session.pop('username', None)
    return redirect(url_for("basic"))

if __name__ == '__main__':
    app.run(port = 5001,debug = True)
