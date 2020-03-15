"""Utility file to seed kindred database from Native-Land data"""

from sqlalchemy import func
from models import Tribe, Language, connect_to_db, db 
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

	Tribe.query.delete()

	tribe_file = "seed_data/indigenousTerritories.json"
	tribe_dict = json_reader(tribe_file)

	i = 0

	for key in tribe_dict['features']:
		name = tribe_dict['features'][i]['properties']['Name']
		region = None
		description = None
		i += 1

		tribe = Tribe(name=name,
					  region=region,
					  description=description
					  )

		db.session.add(tribe)

	db.session.commit()


def load_languages():
	"""Load language infor from indigenousLanguages.json into 
	database."""
	
	print('Languages')

	Language.query.delete()

	lang_file = "seed_data/indigenousLanguages.json"
	lang_dict = json_reader(lang_file)

	i = 0

	for key in lang_dict['features']:
		language_name = lang_dict['features'][i]['properties']['Name']
		i += 1

		language = Language(language_name=language_name)

		db.session.add(language)

	db.session.commit()



def set_val_tribe_id():
	"""Set value for the next tribe_id after seeding database"""

	result = db.session.query(func.max(Tribe.tribe_id)).one()
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
    load_languages()
    set_val_tribe_id()
