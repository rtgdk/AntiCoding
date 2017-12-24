from django import forms
from .models import Info

class InfoForm(forms.ModelForm):
    class Meta:
        model = Info
        fields = ('name', 'email', 'mobno','college','ans1','ans2','ans3','ans4')