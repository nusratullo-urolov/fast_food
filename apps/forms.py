from django.contrib.auth import authenticate
from django.contrib.auth.hashers import make_password
from django.core.exceptions import ValidationError
from django.db.models import CharField
from django.forms import ModelForm, PasswordInput, Form

from apps.models import User


class RegisterForm(ModelForm):
    confirm_password = CharField(PasswordInput())

    class Meta:
        model = User
        fields = ('first_name', 'username', 'phone_number', 'password')

    def clean_password(self):
        password = self.data.get('password')
        confirm_password = self.data.get('confirm_password')
        if password != confirm_password:
            raise ValidationError("Password do not match")
        return make_password(password)


class LoginForm(Form):
    def clean_password(self):
        username = self.data.get('username')
        password = self.data.get('password')
        user = User.objects.get(username=username)
        if not user or user.check_password(password):
            raise ValidationError("Password or Username Do NOt Match")
        return password
