from django.db import models

# Create your models here.
class Asset(models.Model):
	
	name = models.CharField(max_length=128, blank= True, null=True)
	id = models.AutoField(primary_key=True)
	quantity = models.IntegerField(blank=True, null=True, default=0)
	category = models.CharField(blank=True, null=True, max_length=2048)
	price = models.DecimalField(blank=True, null=True, max_digits=10, decimal_places=2, default=0.00)
	timestamp = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return self.name
	
	def get_id(self):
		return self.id
		
	def get_quantity(self):
		return self.quantity
	
	def get_category(self):
		return self.description
	
	def get_price(self):
		return self.preco
	
	def get_timestamp(self):
		return self.timestamp
	
