from django.shortcuts import redirect, render, HttpResponse
from django.http import HttpResponseRedirect, response
from .models import *
from .forms import *
from django.db import connection
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from django.views.generic import View
from django.forms import modelformset_factory
from django.shortcuts import render , redirect
from django.contrib.sessions.models import Session
from django.db.models import Max


# Create your views here.
@login_required
def home (request):
    title = 'Home'
    random_products= products.objects.all()
    context = {
        'random_products':random_products,
        'title':title,
    }
    return render(request, 'home.html',context )

@login_required
def base (request):
    title = 'base'
    context = {
    'title':title,
    }
    return render(request, 'base.html',context )

@login_required
def products_fun (request):
    title = 'Products'
    product = products.objects.all()
    context = {
        'products':product,
        'title':title,
    }
    return render(request, 'product.html' ,context)

def add_product (request):
    title = 'Add New Product'
    categories_holder = categories.objects.all()
    if request.method == "POST":
        new_product = add_productForm(request.POST,request.FILES )
        if new_product.is_valid():
            new_product.save()
            return redirect ('product')
    else:
        new_product = add_productForm
    context = {
        'title':title ,
        'categories':categories_holder,
    }
    return render (request, 'add_product.html',context)

def delete_product(request,id):
    deleted_product = products.objects.get(p_id = id)
    deleted_product.delete()
    return redirect('product')

def update_product(request,id):
    categories_holder = categories.objects.all()
    title = 'update Product'
    updated_product = products.objects.get(p_id = id)
    updated_product_form = add_productForm(request.POST , instance=updated_product)
    if request.method == "POST":
        updated_product_form.save()
        return redirect('product')
    context = {
        'title':title,
        'updated_product':updated_product,
        'updated_product_form':updated_product_form,
        'categories':categories_holder,
        }
    return render (request,'update_product.html',context)

def category(request):
    title = 'Categories'
    categories_holder = categories.objects.all()
    context = {
        'categories':categories_holder,
        'title':title,
    }
    return render (request,'categories.html',context)

def add_category(request):
    title = 'Add Category'
    if request.method == "POST":
        new_category = add_categoryForm(request.POST)
        if new_category.is_valid():
            new_category.save()
            return redirect('category')
    else:
        new_category = add_categoryForm
    context = {
        'title':title,
    }
    return render (request,'add_category.html',context)

def delete_category(request,id):
    deleted_category = categories.objects.get(c_id = id)
    deleted_category.delete()
    return HttpResponseRedirect(reverse('category'))

def update_category(request,id):
    title = 'update Category'
    updated_category = categories.objects.get(c_id = id)
    updated_category_form = add_categoryForm(request.POST , instance=updated_category)
    if request.method == "POST":
        updated_category_form.save()
        return redirect('category')
    context = {
        'title':title,
        'updated_category':updated_category,
        'updated_category_form':updated_category_form,
        }
    return render (request,'update_category.html',context)

def specialties_list(request):
    title = 'Specialties'
    listed_specialties = specialties.objects.all()
    context = {
        'title': title,
        'specialties':listed_specialties,
    }
    return render(request,'specialties_list.html',context)

def add_specialty(request):
    title = 'Add Specialty'
    if request.method == "POST":
        new_specialty = add_specialtyForm(request.POST)
        if new_specialty.is_valid():
            new_specialty.save()
            return redirect('specialties_list')
    else:
        new_specialty = add_specialtyForm
    context = {
        'title':title,
    }
    return render (request,'add_specialty.html',context)

def countries_list(request):
    title = 'Countries'
    listed_countries = countries.objects.all()
    context = {
        'title': title,
        'countries':listed_countries,
    }
    return render(request,'countries_list.html',context)

def add_country(request):
    title = 'Add Country'
    if request.method == "POST":
        new_country = add_countryForm(request.POST)
        if new_country.is_valid():
            new_country.save()
            return redirect('countries_list')
    else:
        new_country = add_countryForm
    context = {
        'title':title,
    }
    return render (request,'add_country.html',context)

def regions_list(request):
    title = 'Regions'
    listed_regions = regions.objects.all()
    context = {
        'title': title,
        'regions':listed_regions,
    }
    return render(request,'regions_list.html',context)

def add_region(request):
    title = 'Add Region'
    countries_holder = countries.objects.all()
    if request.method == "POST":
        new_region = add_regionForm(request.POST)
        if new_region.is_valid():
            new_region.save()
            return redirect('regions_list')
    else:
        new_region = add_regionForm
    context = {
        'title':title,
        'countries':countries_holder,
    }
    return render (request,'add_region.html',context)
    
#################################################################################################################################################





def search_fun(request):
    title = 'products'
    if request.method == "POST":
        the_keyword = request.POST['the_keyword']
        filtered_products = products.objects.filter(p_name__contains = the_keyword)
        return render (request,'product.html',{'products':filtered_products,'title':title,'the_keyword':the_keyword})
    else:
        return render(request,'base.html')

def profile(request):
    title = 'Profile'
    return render(request,'profile.html',{'title': title})

class product_view(View):
    def get(self,request):
        allproduct = products.objects.all()
        context={
            'prodcuts': allproduct
        }
        return render(request, "product_view.html", context )

    def post(self,request,*args,**kwargs):
        if request.method=="POST":
            product_ids=request.POST.getlist('id[]')
            for id in product_ids :
                product= products.objects.get(p_id=id)
                product.delete()
            return redirect('product_view')

#def checkboxes (request):
#    ff= products.objects.all()
#    return render(request, 'checkbox.html',{'ff':ff})

# def filer (request,teto):
#     ff = products.objects.filter(p_id = teto)
#     ss = request.GET.get('{{i.p_id}}')
#     return render(request, 'filer.html',{'ff':ff , 'teto':teto , 'ss':ss})

