from django import forms
from .admin import UserCreationForm
from .models import User

class signupForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('email', 'name', 'password1', 'password2')