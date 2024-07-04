from flask import Flask, render_template, request
from db.models.menu import Menu

app = Flask(__name__,
            static_url_path='',
            static_folder='static',
            template_folder='templates')
app.config.from_object(__name__)

menu = Menu.query.all().values('title', 'url')


@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html', title='home', menu=menu)


@app.route('/me')
def me():
    return render_template('me.html', title='me')


@app.route('/portfolio')
def portfolio():
    return render_template('projects.html', title='projects')


# @app.errorhandler(404)
# def page_not_found(error):
#     connection = connect_db()
#     db = DataBase(connection)
#     return render_template('page_not_found.html', title='Page not found', menu=db.get_menu())


if __name__ == '__main__':
    app.run(debug=True)
