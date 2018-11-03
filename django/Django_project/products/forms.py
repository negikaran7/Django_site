from django import forms
from .models import Product

class ProductForm(forms.ModelForm):
    title=forms.CharField()
    # email=forms.EmailField()
    description=forms.CharField(required=False,widget=forms.Textarea(attrs={
        "class":"new-class-name two",
        "rows":2,
        "cols":20,
        "placeholder":"your description"

    }))
    price=forms.FloatField(initial=99.99)
    class Meta:
        model=Product
        fields=[
            'title',
            'description',
            'price'
    ]

    # def clean_title(self,*args,**kwargs):
    #     title=self.cleaned_data.get("title")
    #     if "karan" in title:
    #         return title
    #     else:
    #         raise forms.ValidationError("this is not a valid title")

    # def clean_email(self,*args,**kwargs):
    #     email=self.cleaned_data.get("email")
    #     if not email.endswith("com"):
    #         raise forms.ValidationError("this is not a valid email")
    #     return email

class RawProductForm(forms.Form):
    title=forms.CharField()
    description=forms.CharField(required=False,widget=forms.Textarea(attrs={
        "class":"new-class-name two",
        "rows":2,
        "cols":20,
        "placeholder":"your description"

    }))
    price=forms.FloatField(initial=99.99)
