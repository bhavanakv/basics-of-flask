from flask import Flask, render_template, request, make_response
app = Flask(__name__)

@app.route("/")
def form():
    return render_template('login.html')

@app.route('/form', methods= ['GET', 'POST'])

#def print_form():
#    form_data = request.form
#    return render_template('data.html', data = form_data)

def setcookie():
    if request.method == 'POST':
        user = request.form["name"]
        resp = make_response(render_template('login.html')) #make_response() for creating a response object
        resp.set_cookie('user', user)
        return resp

@app.route('/getcookie')
def get_cookie():
    return "<h1>The cookie that is created: %s</h1>" % request.cookies.get('user') 

if __name__ == '__main__':
    app.run(port=5001, debug = True)