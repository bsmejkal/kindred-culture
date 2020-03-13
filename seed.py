"""Utility file to seed kindred database from Native-Land data"""

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

	print('Tribes')

	Tribes.query.delete()

	tribe_file = "seed_data/indigenousTerritories.json"
	tribe_dict = json_reader(tribe_file)

	i = 0

	for key in tribe_dict['features']:
		name = tribe_dict['features'][i]['properties']['Name']
		# coordinates = tribe_dict['features'][i]['geometry']['coordinates']
		i += 1

		tribe = Tribes(name=name)

		db.session.add(tribe)

	db.session.commit()
	

def set_val_tribe_id():
	"""Set value for the next tribe_id after seeding database"""

	result = db.session.query(func.max(Tribes.tribe_id)).one()
	max_id = int(result[0])

	query = "SELECT setval('tribes_tribe_id_seq', :new_id)"
	db.session.execute(query, {'new_id': max_id + 1})
	db.session.commit()


if __name__ == "__main__":
    connect_to_db(app)

    # In case tables haven't been created, create them
    db.create_all()

    # Import different types of data
    load_tribes()
    set_val_user_id()
