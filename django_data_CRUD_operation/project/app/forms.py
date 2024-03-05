from django import forms
from app.models import Userdetails

class UserInfo(forms.ModelForm):
    class Meta:
        model = Userdetails
        fields = "__all__"
