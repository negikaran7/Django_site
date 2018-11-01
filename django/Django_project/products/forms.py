from django import forms
from .models import Product

class ProductForm(forms.ModelForm):
    class Meta:
        model=Product
        fields=[
            'title',
            'description',
            'price'
    ]

class RawProductForm(forms.Form):
    title=forms.CharField(label='',widget=forms.TextInput(attrs={"placeholder":"your title"}))
    description=forms.CharField(required=False,widget=forms.Textarea(attrs={
        "class":"new-class-name two",
        "rows":2,
        "cols":20,
        "placeholder":"your description"

    }))
    price=forms.FloatField(initial=99.99)
