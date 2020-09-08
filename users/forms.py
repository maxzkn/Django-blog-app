from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profile


class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()  # required=False if not required

    class Meta:  # override the parent class, gives us a nested namespace for configurations and keeps the configurations in one place
        # and within the configuration we're saying that the model that will be affected is the User model
        # (for e.g., if we do form.save(), it will save it to this User model (user database))
        model = User
        fields = ['username', 'email', 'password1', 'password2']  # these are the fields that we want in the form and in what order
        # we need to specify email field bc parent class don't know anything about it


class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email']


class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['image']