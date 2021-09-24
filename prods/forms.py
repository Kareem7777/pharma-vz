from django import forms
from django.db.models.base import Model
from django.forms import ModelForm
from django.forms import fields
from .models import *
class add_productForm (forms.ModelForm):
    class Meta:
        model = products
        fields = ['p_id' ,'p_name' ,'p_description' ,'p_price' ,'p_category' ,'p_img']

class add_categoryForm(forms.ModelForm):
    class Meta:
        model = categories
        fields = ['c_id','c_name']

class add_specialtyForm(forms.ModelForm):
    class Meta:
        model= specialties
        fields=['specialties_id','specialties_name']

class add_countryForm(forms.ModelForm):
    class Meta:
        model= countries
        fields= ['countries_id','countries_name']

class add_regionForm(forms.ModelForm):
    class Meta:
        model= regions
        fields= ['regions_id','regions_name','regions_f_countries']
