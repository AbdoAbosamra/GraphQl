from django.db import models

# Create your models here.

class productModel(models.Model):
	Segment = models.CharField(max_length=100)
	Country = models.CharField(max_length=100)
	Product = models.CharField(max_length=100)
	Units = models.IntegerField()
	Sales = models.IntegerField()
	Datesold = models.CharField(max_length=100)


	def __str__():
		return self.Product