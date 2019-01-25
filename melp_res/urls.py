from django.urls import include, path
from rest_framework import routers

from . import views

router = routers.DefaultRouter()
router.register(r'restaurants',views.RestaurantsViewSet)

app_name = 'melp_res'
urlpatterns = [
	path('',include(router.urls)),
	path('restaurants/statics',views.RestaurantsEndPoint.as_view(), name='statics'),
]