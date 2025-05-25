from django.db import models

# Create your models here.
class AssetModel(models.Model):
	name = models.CharField(max_length=128)
	supplier = models.CharField(max_length=64)
	description = models.TextField(max_length=2048, blank=True)
	available = models.BooleanField(default=False)
	timestamp = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return self.name
	
	def get_supplier(self):
		return self.supplier
	
	def get_description(self):
		return self.description
	
	def get_timestamp(self):
		return self.timestamp