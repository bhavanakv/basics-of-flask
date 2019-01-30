from flask import Flask, render_template, request, make_response
app = Flask(__name__, static_url_path='/home/bhavana/Desktop/Flask/', static_folder='static/')

@app.route("/")
def form():
    return render_template('login.html')

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