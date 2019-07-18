from django.contrib.auth.models import User
from .models import *
from django import forms

class ProductForm(forms.ModelForm):
	class Meta:
		model = Product
		fields = {
			'image',
			'title',
			'content',
			'price',
			'slug',
		}