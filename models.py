
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

app = Flask(__name__)
app.secret_key = 'SUNDERED'

class Tribe(db.Model):
	"""Indigeneous peoples in North America"""

	__tablename__ = 'tribes'

	tribe_id = db.Column(db.Integer(), autoincrement=True, primary_key=True)
	name = db.Column(db.String(), nullable=True, unique=True)
	region = db.Column(db.String(), nullable=True)
	description = db.Column(db.String(), nullable=True)
	language_id = db.Column(db.Integer(), db.ForeignKey('languages.language_id'))
	
	def __repr__(self):

		return f'<Tribe id = {tribe_id}, name = {name}>'


class Language(db.Model):
	"""Languages of North America"""

	__tablename__ = 'languages'

	language_id = db.Column(db.Integer(), autoincrement=True, primary_key=True)
	language_name = db.Column(db.String(), nullable=True, unique=True)
	language_family = db.Column(db.String(), nullable=True)


	def __repr__(self):

		return f'<Language id = {language_id}, language = {language}>'


def connect_to_db(app):

	app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///kindred'
	app.config['SQLALCHEMY_ECHO'] = True
	app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

	db.app = app
	db.init_app(app)


if __name__ == "__main__":

	from server import app
	connect_to_db(app, 'kindred')
	print('Connected to database.')