""""""

from sqlalchemy import func
from models import Tribes, Locations, connect_to_db, db 
from routes import app


def load_tribes():
	"""Load Tribe info from indigenousTerritories.json into database."""

	print('Tribes')

	# Tribes.query.delete()

	file = open("seed_data/indigenousTerritories.json")
	b_str = file.buffer.read()
	lines = b_str.decode()
	return lines
	# for tribe in tribes:
	# 	name = tribes["features"]["properties"]["Name"]
	# 	print(name)