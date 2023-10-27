from django import forms
from . models import shop

class ModeForm(forms.ModelForm):
    class Meta:
        model=shop
        fields=['name','desc','price','img']