from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
import uuid
import os

def get_file_path(instance, filename):
    ext = filename.split('.')[-1]
    filename = "%s.%s" % (uuid.uuid4(), ext)
    return os.path.join('product', filename)

class Product(models.Model):
	author = models.ForeignKey(User, on_delete=models.CASCADE)
	image = models.ImageField(upload_to=get_file_path, default="product.jpg")
	title = models.CharField(max_length=100)
	content = models.TextField()
	price = models.DecimalField(decimal_places=2, max_digits=20, default=00.00)
	date_posted = models.DateTimeField(auto_now_add=True)
	slug = models.SlugField(blank=False, unique=True)
	
	def __str__(self):
		return self.title 


	def get_absolute_url(self):
		return reverse('post-detail', kwargs={'pk':self.pk}) 