import sqlite3
from flask import Flask
app = Flask(__name__)

def mysql():
    #Connecting to the database
    con = sqlite3.connect('examples')
    print("openned database successfully!")

    #Creating cursor 
    cur = con.cursor()

    #Creating a table
    con.execute("CREATE TABLE details(name varchar(30), phone varchar(10), city varchar(30))")
    print("Table created successfully!")
    
    #Inserting the values to the database
    con.execute("INSERT INTO details VALUES('Bhavana', '8951534306', 'Bangalore')")
    con.execute("INSERT INTO details VALUES('Harshita', '9740026935', 'Bangalore')")

    #Fetching the data from the table
    cur.execute("SELECT * FROM details")
    rows = cur.fetchall()
    print(rows)
    
    #Closing the connection
    con.close()

mysql()