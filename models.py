
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash

db = SQLAlchemy()

app = Flask(__name__)
app.secret_key = 'SUNDERED'


ancestry_table = db.Table('ancestry',
						  db.Column('user_id', db.Integer, db.ForeignKey('users.id')),
						  db.Column('tribe_id', db.Integer, db.ForeignKey('tribes.tribe_id')))


class ModelMix:

	def save(self):
		db.session.add(self)
		db.session.commit()


class Tribe(db.Model):
	"""Indigeneous peoples in North America"""

	__tablename__ = 'tribes'

	tribe_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
	name = db.Column(db.String, nullable=True, unique=True)
	region = db.Column(db.String, nullable=True)
	description = db.Column(db.String, nullable=True)
	language_id = db.Column(db.Integer, db.ForeignKey('languages.language_id'))
	
	def __repr__(self):

		return f'<Tribe ID = {self.tribe_id}, name = {self.name}>'


class Language(db.Model):
	"""Languages of North America"""

	__tablename__ = 'languages'

	language_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
	language_name = db.Column(db.String, nullable=True, unique=True)
	language_family = db.Column(db.String, nullable=True)


	def __repr__(self):

		return f'<Language ID = {self.language_id}, language = {self.language_name}>'


class User(ModelMix, db.Model):
	"""Users"""

	__tablename__ = 'users'

	id = db.Column(db.Integer, autoincrement=True, primary_key=True)
	email = db.Column(db.String, nullable=False, unique=True)
	first_name = db.Column(db.String(50))
	last_name = db.Column(db.String(50))
	username = db.Column(db.String(100), nullable=False, unique=True)
	password = db.Column(db.String(250), nullable=False)
	about = db.Column(db.String, nullable=True)
	city = db.Column(db.String, nullable=True)

	ancestry = db.relationship('Tribe', secondary='ancestry')

	def __repr__(self):

		return f'<User ID = {self.id}, username = {self.username}>'

	def create_password(self, password):
		self.password = generate_password_hash(password)

	def is_valid_password(self, password):
		check_password_hash(self.password, password)


class Connection(db.Model):
	"""User connections"""

	__tablename__ = "connection"

	id = db.Column(db.Integer, autoincrement=True, primary_key=True)
	user1 = db.Column(db.Integer, db.ForeignKey('users.id'))
	user2 = db.Column(db.Integer, db.ForeignKey('users.id'))

	def __repr__(self):

		return f'<Connection user 1 = {self.user1} user 2 = {self.user2}>'


def connect_to_db(app):

	app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///kindred'
	app.config['SQLALCHEMY_ECHO'] = True
	app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

	db.app = app
	db.init_app(app)


if __name__ == "__main__":

	from server import app
	connect_to_db(app)
	print('Connected to database.')