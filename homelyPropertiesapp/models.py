from __future__ import unicode_literals

from django.db import models
from datetime import datetime
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings

# Create your models here.

class User(AbstractUser):
	is_owner = models.BooleanField(default = False)
	def __str__(self):
		res = str(self.username)
		return res

class Renter(models.Model):
	user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
	id = models.AutoField(primary_key = True)
	profile = models.TextField(blank = False)
	pref_location = models.CharField(max_length = 30) 
	def __str__(self):
		return self.user.username;

class Owner(models.Model):
	user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
	id = models.AutoField(primary_key = True)
	num_properties = models.IntegerField(default=0)
	owner_name = models.CharField(max_length=30)
	def __str__(self):
		return self.owner_name

class HomelyProperties(models.Model):
	id = models.AutoField(primary_key = True) 
	date = models.DateTimeField(auto_now_add=True, blank=True)
	description = models.TextField(default = '',blank = False)
	price = models.IntegerField(blank = False)
	image = models.ImageField(upload_to='static/property_images', null=True)
	location = models.CharField(max_length = 50,blank = False,null = False) 
	availability = models.BooleanField(default = True)
	visitor_id = models.ForeignKey(Renter, on_delete=models.CASCADE, null = True) 
	owner = models.ForeignKey(Owner, on_delete=models.CASCADE, null = True)
	booked_from = models.CharField(max_length = 50,blank=True, null=True)
	booked_to = models.CharField(max_length = 50,blank=True, null=True)
	def __str__(self):
		return str(self.id)

class RentedProperties(models.Model):
	owner_id = models.ForeignKey(Owner,on_delete = models.CASCADE )
	prop_id = models.ForeignKey(HomelyProperties,on_delete = models.CASCADE )
	visitor_id = models.ForeignKey(Renter,on_delete = models.CASCADE )
	rent_to_be_paid = models.IntegerField(default=0)
	def __str__(self):
		return "%s %s %s" % (self.owner_id, self.visitor_id, self.rent_to_be_paid)
