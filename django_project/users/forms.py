from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profile

# Create a new class that inherits from UserCreationForm
class UserRegisterForm(UserCreationForm):
    # Add an email field to the form
    email = forms.EmailField(required=True)

    # Create a nested namespace for configurations and keep the configurations in one place
    class Meta:
        # Specify the model that we want the form to interact with
        model = User
        # Specify the fields that we want in our form in a list
        fields = ['username', 'email', 'password1', 'password2']


class UserUpdateForm(forms.ModelForm):
    # Add an email field to the form
    email = forms.EmailField(required=True)

    # Create a nested namespace for configurations and keep the configurations in one place
    class Meta:
        # Specify the model that we want the form to interact with
        model = User
        # Specify the fields that we want in our form in a list
        fields = ['username', 'email']


class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['image']