# Import raw data from csv file to a relational db

import csv
import os

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "melp.settings")
import django
django.setup()

from melp_res.models import Restaurants

with open('restaurantes.csv') as csvfile:
	reader = csv.DictReader(csvfile)
	for row in reader:
		restaurant = Restaurants(
			id = row['id'],
			rating = row['rating'],
			name = row['name'],
			site = row['site'],
			email = row['email'],
			phone = row['phone'],
			street = row['street'],
			city = row['city'],
			state = row['state'],
			lat = row['lat'],
			lng = row['lng']
		)
		restaurant.save()
