from django import forms
from crispy_forms.helper import FormHelper
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import CustomUser

class CustomUserCreationForm(UserCreationForm):
	

	class Meta(UserCreationForm):
		model = CustomUser
		fields = (
			'username',
			'email',
			'password1',
			'password2',
			'address1',
			'address2',
			'city',
			'state',
			'zipcode'
		)

	def __init__(self, *args, **kwargs):
		super(CustomUserCreationForm,self).__init__(*args, **kwargs)
		self.helper = FormHelper()
		self.helper.form_show_errors = True






class CustomUserChangeForm(UserChangeForm):

	class Meta:
		model = CustomUser
		fields = (
			'username',
			'email',
			'password',
			'address1',
			'address2',
			'city',
			'state',
			'zipcode'
		)
	

