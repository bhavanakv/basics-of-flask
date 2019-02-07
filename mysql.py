import sqlite3
from flask import Flask, request, render_template
app = Flask(__name__)

@app.route("/")
def render():
    return render_template('mysql.html')


@app.route("/mysql", methods=["GET", "POST"])
def ajax():
    if request.method == 'POST':
        name = request.form['username']
        phone = request.form['phone']
        city = request.form['city']

        #Connecting to examples database
        con = sqlite3.connect('examples')
        print("openned database successfully!")

        # Cursor to move around the details
        cur = con.cursor()
        con.execute("INSERT INTO details VALUES(?,?,?)",(name, phone, city))

        #Fetching the details
        cur.execute("SELECT * FROM details")
        rows = cur.fetchall()
        print(rows)
        #Closing the connection
        con.close()
        return render_template('mysql.html', data = rows)

if __name__ == '__main__':
    app.run(port = 5001, debug = True)
