from django.shortcuts import render, get_object_or_404, redirect
from .models import Product
from django.http import Http404, HttpResponseRedirect
from .forms import *
from django.contrib.auth.decorators import login_required
# Create your views here.

@login_required
def product_list(request):
	item = Product.objects.all()
	context = {
		'item' : item
	}
	return render(request, 'product_list.html', context)

@login_required
def product_detail(request, slug, *args, **kwargs):
	item = get_object_or_404(Product, slug=slug)
	context = {
		'item' : item
	}
	return render(request, 'product_detail.html', context)




@login_required
def product_post(request):
	form = ProductForm()
	if request.method == 'POST':
		form = ProductForm(request.POST or None,)
		print(form.is_valid())
		print(form.errors)
		if form.is_valid():
			print(form.is_valid())
			print(form.errors)
			title = form.cleaned_data.get('title')
			content = form.cleaned_data.get('content')
			price = form.cleaned_data.get('price')
			slug = form.cleaned_data.get('slug')
			image = request.FILES.get('image') 
			author = request.user
			Product.objects.create(
				title = title,
				content = content,
				price = price,
				slug = slug,
				author = author,
				image = image,
			)

			return redirect('product')

	context = {
		'form':form
	}
	return render(request, 'product_post.html', context)


@login_required
def user_inventory(request):
	user = request.user
	user_posts= Product.objects.filter(author=request.user).order_by('date_posted')
	context = {'user': user,'user_posts': user_posts}
	return render(request, 'user_inventory.html',context)