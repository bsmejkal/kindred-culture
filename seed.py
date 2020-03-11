""""""

from sqlalchemy import func
from models import Tribes, Locations, connect_to_db, db 
from routes import app
import json


def json_reader(file_path):
	"""Opens & loads json files"""
	
	with open(file_path) as file:
		json_dict = json.load(file)

	return json_dict


def load_tribes():
	"""Load Tribe info from indigenousTerritories.json into 
	database."""

	# print('Tribes')

	# Tribes.query.delete()

	tribe_file = "seed_data/indigenousTerritories.json"

	tribe_dict = json_reader(tribe_file)

	return tribe_dict
	