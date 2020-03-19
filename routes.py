"""Routes to render html page views"""

from flask import Flask, render_template
from models import Tribe


app = Flask(__name__)

@app.route('/')
def index():
	"""Home page"""
	tribes = Tribe.query.all()

	return render_template('index.html',
						   tribes=tribes)


@app.route('/about')
def show_about():
	"""About page"""

	return render_template('about.html')


@app.route('/details/<int:tribe_id>')
def display_details(tribe_id):
	"""Tribe details page."""

	tribe = Tribe.query.get(tribe_id)

	return render_template('details.html',
						   tribe=tribe)