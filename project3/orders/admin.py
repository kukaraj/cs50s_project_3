from django.contrib import admin

from .models import Extra, Subs, Subs_topping, Pasta, Salads, Dinner_Platter_toppings, Dinner_Platter, Toppings, Size, Crust, Topping_type, Pizza, Basket, Pizza_with_toppings, Subs_with_add_on

# Register your models here.

admin.site.register(Extra)
admin.site.register(Subs)
admin.site.register(Pasta)
admin.site.register(Salads)
admin.site.register(Dinner_Platter)
admin.site.register(Toppings)
admin.site.register(Pizza)
admin.site.register(Size)
admin.site.register(Crust)
admin.site.register(Topping_type)
admin.site.register(Basket)
admin.site.register(Pizza_with_toppings)
admin.site.register(Subs_topping)
admin.site.register(Dinner_Platter_toppings)
admin.site.register(Subs_with_add_on)