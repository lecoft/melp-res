from django.urls import path

from . import views

app_name = 'melp_res'
urlpatterns = [
	path('',views.index, name='index'),
]