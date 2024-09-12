from django.shortcuts import render,redirect
from posts.models import posts

# Create your views here.
def home(request):
    data =posts.objects.all()
    print(data)
    
    # to see category optional brcause its lengthy
    # for i in data:
    #     print(i.title)
    #     for j in i.Category.all():
    #         print(j)
    #     print()

    return render(request,'home.html',{'data': data})
     