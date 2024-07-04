from flask_sqlalchemy import SQLAlchemy

from main import app

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///my_wb.db'
db = SQLAlchemy(app)