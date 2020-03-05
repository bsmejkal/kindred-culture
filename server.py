""""""

from jinja2 import StrictUndefined

from flask import (Flask, render_template, redirect, request, flash, session)
from flask_debugtoolbar import DebugToolbarExtension

from model import Tribe, Location, connect_to_db, db 


app = Flask(__name__)

app.secret_key = "SUNDERED"

app.jinja_env.undefined = StrictUndefined


@app.route('/')
def index():
	"""Splash page"""

	return render_template("")


@app.route('/about')
def about():
	"""About project"""

	return render_template("")


if __name__ == "__main__":

	app.debug = True
	app.jinja_env.auto_reload = app.debug

	connect_to_db(app)

	DebugToolbarExtension(app)

	app.run(port=5000, host='0.0.0.0')
