from django.contrib.auth import get_user_model
from django.contrib.auth import forms
from django.contrib.auth.forms import UserCreationForm


class UserForm(UserCreationForm):
    """
    A Custom form for creating new users.
    """

    class Meta:
        model = get_user_model()
        fields = ['mobile','first_name','last_name']