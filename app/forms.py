from django import forms
from .models import Info
from django.contrib.auth.models import User

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())
    confirm_password = forms.CharField(widget=forms.PasswordInput())

    def clean_username(self):
        users = self.cleaned_data["username"]
        if User.objects.filter(username=users).count() > 0:
            raise forms.ValidationError("This username already exists.")
        return users

    def clean(self):
        password = self.cleaned_data.get('password')
        confirm_password = self.cleaned_data.get('confirm_password')
        if password and password != confirm_password:
            raise forms.ValidationError("Passwords don't match.")

        return self.cleaned_data

    class Meta:
        model = User
        fields = ('username', 'password', 'confirm_password')

class InfoForm(forms.ModelForm):
    class Meta:
        model = Info
        fields = ('teamname1','teamname2','email1','email2','mobno1','mobno2')