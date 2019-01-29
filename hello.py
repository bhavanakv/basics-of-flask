from flask import Flask, redirect, url_for, render_template
app = Flask(__name__, template_folder = 'templates') #Flask object that is basically Werkzueg applicatiom

@app.route("/")
def print_Data():
    print("Hello world!")
    return "Hello!!"

@app.route("/hello/<name>")
def hello_word(name):
    return "<h1>Hello %s!<h1>" %name

#Page rendering through render_template()
@app.route("/render/<user>")
def hello_rendering(user):
    return render_template('hello.html', name = user)

#redirect the page when different parameters are passed
@app.route("/admin")
def print_admin():
    return "Hello admin!"

@app.route("/guest/<guest>")
def print_guest(guest):
    return "Hello %s as guest user!" %guest

@app.route("/user/<name>")
def print_user(name):
    if name=='admin':
        return redirect(url_for('print_admin'))
    else:
        return redirect(url_for('print_guest', guest=name))

#redirect the page when different parameters are passed (Another approach)
@app.route("/user_type/<user>")
def find_result(user):
    return render_template('result.html', name = user)

"""
def hello_world():
   return ‘hello world’
app.add_url_rule(‘/’, ‘hello’, hello_world)

The above function can also be written as add_url_rule() function
"""
if(__name__ == "__main__"):
    app.run(debug=True)