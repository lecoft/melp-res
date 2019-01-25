import math
from rest_framework import viewsets, serializers, views
from .models import Restaurants
from .serializers import RestaurantsSerializer
from rest_framework.response import Response
from django.contrib.gis.geos import Point
from geopy.distance import distance as geopy_distance

class RestaurantsViewSet(viewsets.ModelViewSet):
	"""
	Melp's system REST API.
	
	Get: Return a list of all the existing restaurants, or an especific restaurant depending on the query.
	Show all existing restaurants ../restaurants/ 		
	Show the restaurant with the specified id ../restaurants/{id}		
	
	Post: Create a new restaurant.

	Put, Patch: Update data from a restaurant.

	Delete: Delete a restaurant.

	EndPoint: ../restaurants/statics?latitude=x&longitude=y&radius=z

	"""
	queryset = Restaurants.objects.all()
	serializer_class = RestaurantsSerializer

class RestaurantsEndPoint(views.APIView):
	"""
	Melp's system Endpoint ../restaurants/statics?latitude=x&longitude=y&radius=z
	"""

	def get(self,request):
		latitude = self.request.query_params.get('latitude')
		longitude = self.request.query_params.get('longitude')
		radius = self.request.query_params.get('radius')
		point1 = Point(float(latitude), float(longitude))

		count = 0
		avg = 0
		std = 0
		values = []
		for res in Restaurants.objects.raw('select * from melp_res_restaurants'):
			point2 = Point(res.lat, res.lng)
			result = geopy_distance(point1,point2).meters
			if int(result) <= int(radius):
				count = count + 1;
				avg = avg + res.rating
				values.append(res.rating)
		avg = avg/count
		addition = 0
		for val in values:
			addition = addition + abs(val-avg)**2
		std = math.sqrt(addition/count)

		return Response({
			"count": count,
			"avg": avg,
			"std": std,
		})