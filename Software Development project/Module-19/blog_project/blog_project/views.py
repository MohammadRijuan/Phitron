from django.shortcuts import render,redirect
from posts.models import posts
from categories.models import Category


# Create your views here.
def home(request,category_slug = None):
    data =posts.objects.all()
    if category_slug is not None:
        category = Category.objects.get(slug = category_slug)
        data=posts.objects.filter(category = category)
    categories = Category.objects.all()
    print(data)
    

    return render(request,'home.html',{'data': data,'categories':categories})
     