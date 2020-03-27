"""Routes to render html page views, user page views, & user auths."""

from flask import Flask, render_template, request, jsonify, session, redirect, flash
from models import Tribe, User


app = Flask(__name__)


# Guest routes:

@app.route('/')
def index():
	"""Home page"""

	tribes = Tribe.query.order_by(Tribe.name.asc()).all()
	# Displays all tribe names in ascending order
	# 	in dropdown list.

	return render_template('index.html',
						   tribes=tribes)


@app.route('/details', methods=['POST'])
def show_details():
	"""Renders description and details in place on index.html"""

	tribe_name = request.form.get('tribe_name')
	print(f'\n \n \n {tribe_name}')
	tribe = Tribe.query.filter(Tribe.name==tribe_name).first()

	return jsonify({'name': tribe.name, 
				    'region': tribe.region,
				    'description': tribe.description})


@app.route('/about')
def show_about():
	"""About page"""

	return render_template('about.html')


@app.route('/register')
def register_user():
	"""User registration page"""

	return render_template('register.html')


@app.route('/login')
def login_form():
	"""User login page"""

	return render_template('login.html')


# Auth routes:

@app.route('/api/auth', methods=['POST'])
def login():
	user = User.query.filter_by(username=request.form.get('username')).first()

	if user.login(request.form.get('password')):
		app.logger.info('...Login successful.')
		session['user_id'] = user.id
	else:
		app.logger.info('-  Login failure  -')
		flash('Invalid username or password.')
		return render_template('login.html')

	return render_template('profile.html', user=user)


@app.route('/logout')
def logout():
	del session['user_id']

	return redirect('/')


@app.route('/api/register', methods=['POST'])
def register_auth():
	"""Handles user registration data"""

	app.logger.info('Registering new user...')

	user_data = dict(request.form)

	if user_data.get('password') == user_data.get('passwordConfirm'):
		del user_data['passwordConfirm']

		user = User(**user_data)
		user.create_password(user_data.get('password'))
		user.save()
		app.logger.info(f'New user {user.id} created. Logging in...')
		session['user_id'] = user.id

		return redirect(f'/users/{user.id}')


# User routes:

@app.route('/users/<int:user_id>')
def get_user(user_id):
	user = User.query.get(user_id)
	app.logger.info(f'Current user = {user}')

	return render_template('profile.html', user=user)


# @app.route('/profile')
# def profile():
# 	"""Another user's profile page"""

# 	return render_template('profile.html')

