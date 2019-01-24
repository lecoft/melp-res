from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

class Restaurants(models.Model):
	id = models.CharField(max_length=30, primary_key=True)
	rating = models.PositiveSmallIntegerField(validators=[MaxValueValidator(4), MinValueValidator(0)])
	name = models.CharField(max_length=80)
	site = models.URLField(max_length=70)
	email = models.EmailField(max_length=80)
	phone = models.CharField(max_length=10)
	street = models.CharField(max_length=50)
	city = models.CharField(max_length=35)
	state = models.CharField(max_length=35)
	lat = models.FloatField()
	lng = models.FloatField()
	
	class Meta:
		verbose_name = 'Restaurant'
		verbose_name_plural = 'Restaurants'

	def __str__(self):
		return self.name