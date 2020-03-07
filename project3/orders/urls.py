from django.urls import path

from . import views

urlpatterns = [
 path("price",views.Price, name="Price"),
 path("subs",views.sub, name="Subs"),
 path("salads",views.salad, name="Salads"),
 path("pasta",views.pasta, name="Pasta"),
 path("dinner_platter",views.Dinner_platter, name="Dinner_platter"),
 path("checkout",views.Checkout,name="Checkout"),
 path("delete_basket",views.delete_basket,name="Delete"),
 path("confirm_basket",views.confirm_basket,name="Confirm")    
]
