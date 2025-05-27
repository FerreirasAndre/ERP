from django.db import models

# Create your models here.
class Asset(models.Model):
	name = models.CharField(max_length=128)
	quantity = models.IntegerField()
	description = models.TextField(max_length=2048, blank=True)
	category = models.CharField(max_length=64)
	timestamp = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return self.name
	
	def get_quantity(self):
		return self.quantity
	
	def get_description(self):
		return self.description
	
	def get_category(self):
		return self.category
	
	def get_timestamp(self):
		return self.timestamp