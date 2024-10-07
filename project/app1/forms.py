from django import forms
from .models import *


class CategoryForm(forms.ModelForm):
    class Meta:
        model=categories
        fields=['name','image']
class productsForm(forms.ModelForm):
    class Meta:
        model=products
        fields=['name','image','rate','Category','description']

