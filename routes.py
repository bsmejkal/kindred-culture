  
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
	"""Home page"""

	return render_template('index.html')