from django import forms
from django.core.exceptions import ValidationError

class LoginForm(forms.Form):
    username = forms.CharField(max_length=150)
    password = forms.CharField(widget=forms.PasswordInput)

    def clean_username(self):
        username = self.cleaned_data.get('username')
        if len(username) < 4:
            raise ValidationError("Username must contain at least 4 letters.")
        return username

    def clean_password(self):
        password = self.cleaned_data.get('password')
        if not password.isdigit():
            raise ValidationError("Password must be an integer.")
        return password
