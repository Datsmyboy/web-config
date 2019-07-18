from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.utils import timezone


class Profile(models.Model):
	user 		= models.OneToOneField(User, on_delete= models.CASCADE)
	photo		= models.ImageField(upload_to='profile', default="default.jpg")
	birthday	= models.DateField(null=True, blank=True, auto_now_add=False)
	occupation 	= models.CharField(max_length=120, null=False, blank=False)
	address 	= models.CharField(max_length=120, null=False, blank=False)
	bio			= models.TextField(null=False, blank=True)

	def __str__(self):
		return self.user.first_name 

	def create_profile(sender, **kwargs):
		if kwargs['created']:
			user_profile = Profile.objects.create(user=kwargs['instance'])

	post_save.connect(create_profile, sender=User)


class State(models.Model):
	user 		= models.OneToOneField(User, on_delete= models.CASCADE)
	tax			= models.DecimalField(max_digits=4, decimal_places=2)
	def __str__(self):
		return self.user.first_name 