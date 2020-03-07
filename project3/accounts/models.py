from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.

class CustomUser(AbstractUser):
	email = models.EmailField(verbose_name ='emailaddress', max_length=255, unique=True)
	address1 = models.CharField(max_length=64, blank=True)
	address2 = models.CharField(max_length=64, blank=True)
	city = models.CharField(max_length=64,blank=True)
	state = models.CharField(max_length=64,blank=True)
	zipcode = models.CharField(max_length=64,blank=True)


	def __str__(self):
		return self.email