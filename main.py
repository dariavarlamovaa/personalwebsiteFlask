from flask import Flask, render_template, request
import os
import sqlite3
from Database import DataBase

app = Flask(__name__,
            
            static_url_path='',
            static_folder='static',
            template_folder='templates')
app.config.from_object(__name__)

app.config.update({'DATABASE': os.path.join(app.root_path, 'my_wb.db')})


def connect_db():
    con = sqlite3.connect(app.config['DATABASE'])
    con.row_factory = sqlite3.Row
    return con


def create_db():
    db = connect_db()
    with open('my_wb.sql', 'r') as f:
        db.cursor().executescript(f.read())
    db.commit()
    db.close()


@app.route('/')
@app.route('/home')
def home():
    connection = connect_db()
    db = DataBase(connection)
    return render_template('home.html', title='home', menu=db.get_menu())


@app.route('/me')
def me():
    connection = connect_db()
    db = DataBase(connection)
    return render_template('me.html', title='me', menu=db.get_menu())


@app.route('/portfolio')
def portfolio():
    connection = connect_db()
    db = DataBase(connection)
    return render_template('projects.html', title='projects', menu=db.get_menu())


# @app.errorhandler(404)
# def page_not_found(error):
#     connection = connect_db()
#     db = DataBase(connection)
#     return render_template('page_not_found.html', title='Page not found', menu=db.get_menu())


if __name__ == '__main__':
    create_db()
    app.run(debug=True)
