from django import forms
from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model, authenticate
from django.contrib.auth.forms import UserChangeForm, UserCreationForm
from django.forms import TextInput, EmailInput, PasswordInput
from .models import *
User = get_user_model()

class RegisterForm(UserCreationForm):
	username = forms.CharField(widget=TextInput(attrs={ 'class': 'input-field', 'style': 'display:block', 'required': False}))
	first_name = forms.CharField(widget=TextInput(attrs={'class': 'input-field' , 'style': 'display:block', 'required': False}))
	last_name = forms.CharField(widget=TextInput(attrs={'class': 'input-field', 'style': 'display:block', 'required': False}))
	email = forms.CharField(widget=EmailInput(attrs={'type':'text','class': 'input-field', 'style': 'display:block', 'required': False}))
	password1 = forms.CharField(widget=PasswordInput(attrs={'class': 'input-field', 'style': 'display:block', 'required': False}))
	password2 = forms.CharField(widget=PasswordInput(attrs={'class': 'input-field', 'style': 'display:block', 'required': False}))
	class Meta:
		model = User
		fields = {
			'username',
			'first_name',
			'last_name',
			'email',
			'password1',
			'password2'
		}


class UserUpdateForm(forms.ModelForm):
	username = forms.CharField(widget=TextInput(attrs={ 'class': 'input-field', 'style': 'display:block', 'required': 'False'}))
	first_name = forms.CharField(widget=TextInput(attrs={'class': 'input-field' , 'style': 'display:block', 'required': 'False'}))
	last_name = forms.CharField(widget=TextInput(attrs={'class': 'input-field', 'style': 'display:block', 'required': 'False'}))
	email = forms.CharField(widget=EmailInput(attrs={'type':'text','class': 'input-field', 'style': 'display:block', 'required': 'False'}))
	password1 = forms.CharField(widget=PasswordInput(attrs={'class': 'input-field', 'style': 'display:block', 'required': 'False'}))
	password2 = forms.CharField(widget=PasswordInput(attrs={'class': 'input-field', 'style': 'display:block', 'required': 'False'}))
	class Meta:
		model = User
		fields = {
			'username',
			'first_name',
			'last_name',
			'email',
			'password1',
			'password2'
		}
class ProfileUpdateForm(forms.ModelForm):
	photo = forms.ImageField()
	occupation = forms.CharField(widget=TextInput(attrs={'class': 'input-field' , 'style': 'display:block', 'required': 'False'}))
	address = forms.CharField(widget=TextInput(attrs={'class': 'input-field' , 'style': 'display:block', 'required': 'False'}))
	bio = forms.CharField(widget=TextInput(attrs={'class': 'input-field' , 'style': 'display:block', 'required': 'False'}))
	class Meta:
		model = Profile
		fields = {
			'photo',
			'occupation',
			'address',
			'bio',
		}

	def save(self, commit=True):
	    profile = super().save(commit=False)
	    profile.photo = self.cleaned_data["photo"]
	    profile.occupation = self.cleaned_data["occupation"]
	    profile.address = self.cleaned_data["address"]
	    profile.bio = self.cleaned_data["bio"]
	    
	    if commit:
	        profile.save()
	    return profile 