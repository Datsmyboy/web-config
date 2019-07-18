from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, get_user_model
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render, redirect
from .forms import *
from .models import *
from django.contrib.auth.models import User
from django.contrib.auth.forms import PasswordChangeForm

#HOMEPAGE VIEW
def home_page(request):
	context = {
		"variable" : ""
	}
	return render(request, "home_page.html", context)
#REGISTER VIEW
def user_register(request):
	# VARIABLES
	if request.method == 'POST':
		form = RegisterForm(request.POST)
		if form.is_valid():
			form.save()
	else:
		form = RegisterForm()
	# CONTEXT TO TEMPLATE
	context = {
		"form" : form
	}
	return render(request, "user_register.html", context)


# USER PROFILE VIEW
@login_required
def user_profile(request):
	context = {
		"info" : request.user
	}
	return render(request, "user_profile.html", context)

# EDIT PROFILE INFO
@login_required
def user_profile_edit(request):
	if request.method == 'POST':
		user_form = UserUpdateForm(request.POST, instance=request.user)
		profile_form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.profile)
		print(user_form.is_valid(), profile_form.is_valid())
		print(request.FILES)
		if user_form.is_valid() and profile_form.is_valid():
			user_form.save()
			profile_form.save()
			return redirect('profile')
	else:
		user_form = UserUpdateForm(instance=request.user)
		profile_form = ProfileUpdateForm(instance=request.user.profile)

	context = {
		"user_form" : user_form,
		"profile_form": profile_form
	}
	return render(request, "user_profile_edit.html", context)

# EDIT PASSWORD INFO
@login_required
def user_password_edit(request):
	if request.method == 'POST':
		form = PasswordChangeForm(data=request.POST, user=request.user)

		if form.is_valid():
			form.save()
			return redirect('profile')
	else:
		form = PasswordChangeForm(user=request.user)

	context