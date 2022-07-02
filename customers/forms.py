from django import forms
from .models import Customers, Software

class NewCustomer(forms.ModelForm):
    customer_name = forms.TextInput()
    class Meta: 
        model = Customers
        fields = ['customer_name']

class NewSoftware(forms.ModelForm):
    customer_pk = forms.IntegerField(widget=forms.HiddenInput())
    software_name = forms.TextInput()
    logo = forms.ImageField()
    
    class Meta: 
        model = Software
        fields = ['customer_pk','software_name', 'logo']


