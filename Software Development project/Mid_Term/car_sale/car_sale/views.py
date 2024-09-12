from django.shortcuts import render,redirect
from cars.models import Car,Purchase,Brand




# Create your views here.

def home(request, category_slug = None):
    data = Car.objects.all()
    categories = Brand.objects.all()

    if category_slug is not None:
        category = Brand.objects.get(slug=category_slug)
        data = Car.objects.filter(brand=category)
    print(data)

    return render(request,'home.html',{'data':data , 'categories':categories})

