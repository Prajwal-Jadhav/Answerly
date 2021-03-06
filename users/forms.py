from django.contrib.auth.forms import UserCreationForm, UserChangeForm

from .models import User


class CustomUserCreationForm(UserCreationForm):

    class Meta(UserCreationForm):
        model = User
        fields = ('email', 'first_name', 'last_name',
                  'PRN', 'year', 'branch', 'division')


class CustomUserChangeForm(UserChangeForm):

    class Meta(UserChangeForm):
        model = User
        fields = ('email', 'first_name', 'last_name',
                  'PRN', 'year', 'branch', 'division')
