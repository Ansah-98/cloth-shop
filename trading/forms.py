from pyexpat import model
from django.forms import ModelForm
from .models import Product,ContactInfo

class ProductForm(ModelForm):
    class Meta:
        model= Product
        fields = ['name','price','type_of','brand','image']

    ordering = ['-updated','-updated']


class ContactInfoForm(ModelForm) :
    class Meta:
        model = ContactInfo
        fields  =['email','phone_number','address']
