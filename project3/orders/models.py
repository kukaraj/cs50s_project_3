from django.db import models


# Create your models here.
class Crust(models.Model):
	name = models.CharField(max_length=20)	

	def __str__(self):
		return f"{self.name}"

class Size(models.Model):
	name = models.CharField(max_length=20)

	def __str__(self):
		return f"{self.name}"

class Topping_type(models.Model):
	name = models.CharField(max_length=20)

	def __str__(self):
		return f"{self.name}"

class Extra (models.Model):
	name = models.CharField(max_length=20)
	price = models.DecimalField(help_text="Price in US$",max_digits=4, decimal_places=2)

	def __str__(self):
		return f"{self.name} - ${self.price}"

class Subs_topping(models.Model):
	name =  models.CharField(max_length=64)
	def __str__(self):
		return f"{self.name}"

class Subs (models.Model):
	name = models.ForeignKey('Subs_topping',on_delete=models.CASCADE)
	quantity = models.ForeignKey('Size',on_delete=models.CASCADE)
	price = models.DecimalField(help_text="Price in US$",max_digits=4, decimal_places=2)

	def __str__(self):
		return f"{self.name} - {self.quantity} - ${self.price} "

class Pasta(models.Model):
	name = models.CharField(max_length=64)
	price = models.DecimalField(help_text="Price in US$",max_digits=4, decimal_places=2)

	def __str__(self):
		return f"{self.name} - ${self.price}"

class Salads(models.Model):
	name = models.CharField(max_length=64)
	price = models.DecimalField(help_text="Price in US$",max_digits=4, decimal_places=2)

	def __str__(self):
		return f"{self.name} - ${self.price}"

class Dinner_Platter_toppings(models.Model):
	name = models.CharField(max_length=64)

	def __str__(self):
		return f"{self.name}"

class Dinner_Platter(models.Model):
	name = models.ForeignKey('Dinner_Platter_toppings',on_delete=models.CASCADE)
	quantity = models.ForeignKey('Size',on_delete=models.CASCADE)
	price = models.DecimalField(help_text="Price in US$",max_digits=4, decimal_places=2)

	def __str__(self):
		return f"{self.name} - {self.quantity} - ${self.price}"

class Toppings(models.Model):
	name = models.CharField(max_length=64)

	def __str__(self):
		return f"{self.name}"


class Pizza(models.Model):
	name = models.ForeignKey('Crust',on_delete=models.CASCADE,related_name="crust")
	quantity = models.ForeignKey('Size',on_delete=models.CASCADE,related_name="quantity")
	toppings = models.ForeignKey('Topping_type',on_delete=models.CASCADE,related_name="toppings")
	price = models.DecimalField(help_text="Price in US$",max_digits=4, decimal_places=2)
	

	def __str__(self):
		return f"{self.name} {self.quantity} {self.toppings} {self.price}"

class Basket(models.Model):
	User = models.ForeignKey('accounts.CustomUser',on_delete=models.CASCADE,null=True)
	status = models.CharField(max_length=20,choices=(("cmp","completed"),("prc","processing")),default="prc")
	Pizza = models.ManyToManyField('Pizza',through='pizza_with_toppings',blank=True)
	Dinner_Platter = models.ManyToManyField('Dinner_Platter',blank=True)
	Salads = models.ManyToManyField('Salads',blank=True)
	Subs = models.ManyToManyField('Subs',through='Subs_with_add_on',blank=True)
	Pasta = models.ManyToManyField('Pasta',blank=True)
	
	def __str__(self):
		return f"{self.User}"

class Pizza_with_toppings(models.Model):
	Pizza = models.ForeignKey('Pizza',on_delete=models.CASCADE,null=True)
	Toppings = models.ManyToManyField('Toppings',blank=True)
	Basket= models.ForeignKey('Basket',on_delete=models.CASCADE,null=True)

	def __str__(self):
		return f"{self.Pizza}"

class Subs_with_add_on(models.Model):
	Subs = models.ForeignKey('Subs',on_delete=models.CASCADE,null=True)
	Add_on = models.ManyToManyField('Extra',blank=True)
	Basket= models.ForeignKey('Basket',on_delete=models.CASCADE,null=True)

	def __str__(self):
		return f"{self.Subs}"