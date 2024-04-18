from flask import Flask, render_template
import sqlite3
import pathlib 
import pandas as pd

base_path = pathlib.Path(r'C:\Users\super\OneDrive\Documents\GitHub\python')
db_name = "Games1.db"
db_path = base_path / db_name
print(db_path)

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index_links.html") 

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/readme")
def readme():
    return render_template("Readme.html")

@app.route("/data")
def data():
    con = sqlite3.connect(db_path)
    cursor = con.cursor()
    Game = cursor.execute("SELECT * FROM Game").fetchall()
    con.close()

    return render_template("data_table.html", Game = Game)

if __name__=="__main__":
    app.run(debug=True)

