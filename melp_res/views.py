from rest_framework import viewsets
from .models import Restaurants
from .serializers import RestaurantsSerializer

class RestaurantsViewSet(viewsets.ModelViewSet):
	"""
	Melp's system API.
	"""

	queryset = Restaurants.objects.all()
	serializer_class = RestaurantsSerializer