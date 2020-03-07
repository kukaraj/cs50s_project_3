from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.shortcuts import render, redirect
from django.urls import reverse
from accounts.forms import CustomUserCreationForm
from django.contrib.auth import authenticate, logout as dj_logout, login as dj_login

from orders.models import Toppings, Crust, Size, Topping_type
from orders.views import check_for_cart_total

# Create your views here.

def index(request):
    if not request.user.is_authenticated:
    	return render(request,"accounts/login.html", {"message": None})
    
    context = {
    "crust": Crust.objects.all(),
    "size": Size.objects.all(),
    "toppings": Toppings.objects.all(),
    "no_of_toppings":Topping_type.objects.all(),
    "basket_total":check_for_cart_total(request)
    }

    return render(request,"orders/pizza.html", context)

def login(request):

	if request.method == "POST":
		try:
			username = request.POST["username"]
			password = request.POST["password"]
		except username.DoesNotExists:
			return render(request,"accounts/login.html", {"message": "Input valid username"})
		except password.DoesNotExists:
			return render(request,"accounts/login.html", {"message": "Input valid password"})

		user = authenticate(request, username=username, password=password)
		if user is not None:
			dj_login(request, user)
			return HttpResponseRedirect(reverse("index"))
		else:
			return render(request,"accounts/login.html",{"message": "Invalid credentials"})

	else:
		return render(request,"accounts/login.html")

def logout(request):
	dj_logout(request)
	return render(request, "accounts/login.html")


def signup(request):

	if request.method == "POST":
		form = CustomerRegistrationForm(request.POST)

		if form.is_valid():
			form.save()
			username = form.cleaned_data.get('username')
			raw_password = form.cleaned_data.get('password1')
			user = authenticate(username=username, password=raw_password)
			dj_login(request, user)
			return redirect("index")
			
	else:
		form = CustomerRegistrationForm()
	
	return render(request, "accounts/signup.html",{"form": form})