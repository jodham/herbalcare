from django import forms
from django.contrib.auth.models import User
from betterforms.multiform import MultiModelForm
from django.contrib.auth.forms import UserCreationForm
from .models import Profile, Disease, Herb, Post


class UserRegistration(UserCreationForm):
	email = forms.EmailField()
	
	class Meta:
		model = User
		fields =['username','email', 'password1', 'password2']


class UserUpdateForm(forms.ModelForm):
	email = forms.EmailField()

	class Meta:
		model = User
		fields = ['username', 'email']


class ProfileUpdateForm(forms.ModelForm):
	class Meta:
		model = Profile
		fields = ['image']


class DiseaseUpdateForm(forms.ModelForm):
	class Meta:
		model = Disease
		fields = ['DiseaseName', 'DiseaseDescription', 'status', 'DiseasePhoto']


class PostCreateForm(forms.ModelForm):
	class Meta:
		model = Post
		fields = ['title', 'content', 'date_posted']


class HerbUpdateForm(forms.ModelForm):
	class Meta:
		model = Herb
		fields = ['HerbName', 'diseaseName']


class PostCreationMultiForm(MultiModelForm):
	form_classes = {
		'disease': DiseaseUpdateForm,
		'post': PostCreateForm,
	}
