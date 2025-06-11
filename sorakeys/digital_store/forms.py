from django import forms
from .models import *

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'description', 'price', 'photo', 'stock', 'category', 'publisher', 'platforms']

class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['name', 'description', 'photo']

class CartForm(forms.ModelForm):
    class Meta:
        model = Cart
        fields = ['user']

class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['user', 'total_price', 'status']

class PublisherForm(forms.ModelForm):
    class Meta:
        model = Publisher
        fields = ['name', 'description', 'website']

class PlatformForm(forms.ModelForm):
    class Meta:
        model = Platform
        fields = ['name', 'description']

class DiscountForm(forms.ModelForm):
    class Meta:
        model = Discount
        fields = ['name', 'percentage', 'start_date', 'end_date', 'products']
        widgets = {
            'start_date': forms.DateInput(attrs={'type': 'date'}),
            'end_date': forms.DateInput(attrs={'type': 'date'}),
        }