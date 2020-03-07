from django.http import HttpResponse, HttpResponseRedirect, Http404, JsonResponse
from django.shortcuts import render
from django.urls import reverse
from django.contrib.auth import authenticate, logout as dj_logout, login as dj_login
from django.core import serializers

from orders.models import Toppings, Subs, Pizza, Basket, Pizza_with_toppings, Salads, Dinner_Platter, Pasta, Extra, Size, Subs_topping, Dinner_Platter_toppings, Subs_with_add_on
from accounts.models import CustomUser
# Create your views here.

def check_for_existing_cart(request):
	email = request.user.email
	user = CustomUser.objects.get(email=email)
	if user == None:
		return render(request,"accounts/login.html")
	else:
		try:
			basket = Basket.objects.filter(User=user,status="prc")[0]
		except IndexError:
			basket = Basket.objects.create(User=user)
		return basket;

def check_for_cart_total(request):
	email = request.user.email
	user = CustomUser.objects.get(email=email)
	if user == None:
		return render(request,"accounts/login.html")
	else:
		subs_total = 0
		pizza_total = 0
		pasta_total = 0
		salads_total = 0
		platter_total = 0
		try:
			basket = Basket.objects.filter(User=user,status="prc")[0]
			pizza = basket.Pizza.all()
			for each in pizza:
				pizza_total = pizza_total+each.price
			pasta = basket.Pasta.all()
			for each in pasta:
				pasta_total = pasta_total+each.price
			salads = basket.Salads.all()
			for each in salads:
				salads_total = salads_total+each.price
			platter = basket.Dinner_Platter.all()
			for each in platter:
				platter_total = platter_total+each.price
			subs = basket.Subs.all()
			for each in subs:
				subs_total = subs_total+each.price
			basket_total = pizza_total+pasta_total+salads_total+subs_total+platter_total
		except IndexError:
			basket_total = "0.00"
		return basket_total;




def Price(request):

	menu = request.POST.get("menu")
	cart = request.POST.get("cart")

	if menu == "pizza":
		data1 = request.POST.get("data1")
		data2 = request.POST.get("data2")
		data3 = request.POST.get("data3")
		price = Pizza.objects.values_list("price",flat=True).get(name__name=data1,quantity__name=data2,toppings__name=data3)

		if cart:
			basket = check_for_existing_cart(request)
			pizza = Pizza.objects.get(name__name=data1,quantity__name=data2,toppings__name=data3)
			basket.Pizza.add(pizza)

	elif menu == "subs":
		data1 = request.POST.get("data1")
		data2 = request.POST.get("data2")
		data3 = request.POST.get("data3")
		sub_price = Subs.objects.values_list("price",flat=True).get(name__name=data1,quantity__name=data3)
		if data2 == "empty":
			price = sub_price

			if cart:
				basket = check_for_existing_cart(request)
				sub = Subs.objects.get(name__name=data1,quantity__name=data3)
				basket.Subs.add(sub)

		else:
			add_price = Extra.objects.values_list("price",flat=True).get(name=data2)
			price =  sub_price + add_price

			if cart:
				basket = check_for_existing_cart(request)
				sub = Subs.objects.get(name__name=data1,quantity__name=data3)
				basket.Subs.add(sub)
				add_on = Extra.objects.get(name=data2)
				

	elif menu == "pasta":
		data1 = request.POST.get("data1")
		price = Pasta.objects.values_list("price",flat=True).get(name=data1)

		if cart:
			basket = check_for_existing_cart(request)
			pasta = Pasta.objects.get(name=data1)
			basket.Pasta.add(pasta)

	elif menu == "salads":
		data1 = request.POST.get("data1")
		price = Salads.objects.values_list("price",flat=True).get(name=data1)

		if cart:
			basket = check_for_existing_cart(request)
			salad = Salads.objects.get(name=data1)
			basket.Salads.add(salad)

	elif menu == "platter":
		data1 = request.POST.get("data1")
		data2 = request.POST.get("data2")
		price = Dinner_Platter.objects.values_list("price",flat=True).get(name__name=data1,quantity__name=data2)

		if cart:
			basket = check_for_existing_cart(request)
			platter = Dinner_Platter.objects.get(name__name=data1,quantity__name=data2)
			basket.Dinner_Platter.add(platter)

	basket_total = check_for_cart_total(request)	
	return JsonResponse({"price":price,"total_price":basket_total})

def sub(request):
	context = {
	"subs": Subs_topping.objects.all(),
	"size":Size.objects.all(),
	"extra":Extra.objects.values_list("name",flat=True),
	"basket_total":check_for_cart_total(request)
	}
	return render(request,"orders/subs.html",context)

def pasta(request):
	context ={
	"pasta":Pasta.objects.values_list("name",flat=True),
	"basket_total":check_for_cart_total(request)
	}

	return render(request,"orders/pasta.html",context)

def salad(request):
	context = {
	"salad":Salads.objects.values_list("name",flat=True),
	"basket_total":check_for_cart_total(request)
	}

	return render(request,"orders/salads.html",context)

def Dinner_platter(request):
	context = {
	"platter":Dinner_Platter_toppings.objects.all(),
	"size":Size.objects.all(),
	"basket_total":check_for_cart_total(request)
	}

	return render(request,"orders/dinner_platter.html",context)

	
def Checkout(request):
	email = request.user.email
	user = CustomUser.objects.get(email=email)
	if user == None:
		return render(request,"accounts/login.html")
	else:
		products = []

		try:
			basket = Basket.objects.filter(User=user,status="prc")[0]
			pizza = basket.Pizza.all()
			for each in pizza:
				products.append(each)
			pasta = basket.Pasta.all()
			for each in pasta:
				products.append(each)
			salads = basket.Salads.all()
			for each in salads:
				products.append(each)
			platter = basket.Dinner_Platter.all()
			for each in platter:
				products.append(each)
			subs = basket.Subs.all()
			for each in subs:
				products.append(each)
		except IndexError:
			products = []

	context = {
	"products":products,
	"basket_total":check_for_cart_total(request)
	}
	return render(request,"orders/checkout.html",context)

def delete_basket(request):
	basket = check_for_existing_cart(request)
	basket.delete()
	return HttpResponseRedirect(reverse("Checkout"))

def confirm_basket(request):
	basket = check_for_existing_cart(request)
	basket.status="cmp"
	basket.save()
	return HttpResponseRedirect(reverse("index"))


