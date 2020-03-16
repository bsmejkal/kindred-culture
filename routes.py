  
from flask import Flask, render_template
from models import Tribe


app = Flask(__name__)

@app.route('/')
def index():
	"""Home page"""

	return render_template('index.html')


@app.route('/details/<int:tribe_id>')
def display_details(tribe_id):
	"""Tribe details page."""

	tribe = Tribe.query.get(tribe_id)

	return render_template('details.html',
						   tribe=tribe)