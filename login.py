from flask import Flask, redirect, url_for, request, render_template
app = Flask(__name__)

@app.route("/success/<name>")
def success(name):
    return "Hello %s, you have successfully logged in!" % name

@app.route("/failure")
def fail():
    return "Entered wrong password, try again!"

@app.route("/login", methods=["POST"])
def login():
    user = request.form["name"]
    pwd = request.form["pwd"]
    button = request.form["submit_button"]
    if button == "Submit":
        if request.method == "POST":
            if(pwd == '123456'):
                return redirect(url_for('success', name = user))
            else:
                return redirect(url_for('fail'))

if __name__ == '__main__':
    app.run(debug = True) 