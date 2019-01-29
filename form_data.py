from flask import Flask, render_template, request
app = Flask(__name__)

@app.route("/")
def form():
    return render_template('login.html')

@app.route('/form', methods= ['GET', 'POST'])
def print_form():
    form_data = request.form
    return render_template('data.html', data = form_data)

if __name__ == '__main__':
    app.run(port=5001, debug = True)