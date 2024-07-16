from django import forms
from .models import List

class ListForm(forms.ModelForm):
    class Meta:
        model = List
        fields = "__all__" #['firstname', 'lastname', "address"] #  "__all__"