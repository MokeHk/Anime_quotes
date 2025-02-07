from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms

class SignUpForm(UserCreationForm):
	# email = forms.EmailField(label="", widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Email Address'}))
	# first_name = forms.CharField(label="", max_length=100, widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'First Name'}))
	# last_name = forms.CharField(label="", max_length=100, widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Last Name'}))


	class Meta:
		model = User
		fields = ('username', 'password1', 'password2')


	def __init__(self, *args, **kwargs):
		super(SignUpForm, self).__init__(*args, **kwargs)

		self.fields['username'].widget.attrs.update({
			'name': 'username',
			"required": '',
			"type": "text",
			'placeholder': 'Username',
			"label":""
		})
		self.fields['password1'].widget.attrs.update({
			'name': 'password',
			"required": '',
			"type": "password",
			'placeholder': 'Password',
			"label":""
		})
		self.fields['password2'].widget.attrs.update({
			'name': 'confirm password',
			"required": '',
			"type": "password",
			'placeholder': 'Confirm Password',
			"label":""
		})

		# self.fields['password1'].widget.attrs['class'] = 'row'
		# self.fields['password1'].widget.attrs['placeholder'] = 'Password'
		# self.fields['password1'].label = ''
		# self.fields['password1'].help_text = '<ul class="form-text text-muted"><li><small>Your password can\'t be too similar to your other personal information.</small></li><li>Your password must contain at least 8 characters.</li><li>Your password can\'t be a commonly used password.</li><li>Your password can\'t be entirely numeric.</li></ul>'

		# self.fields['password2'].widget.attrs['class'] = 'row'
		# self.fields['password2'].widget.attrs['placeholder'] = 'Confirm Password'
		# self.fields['password2'].label = ''
		# self.fields['password2'].help_text = '<span class="form-text text-muted"><small>Enter the same password as before, for verification.</small></span>'	
