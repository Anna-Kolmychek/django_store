from django import forms
from catalog.models import Product

class NewProductForm(forms.ModelForm):
    """Form for the image model"""
    class Meta:
        model = Product
        fields = (
            'name',
            'description',
            'image',
            'category',
            'price',
        )
