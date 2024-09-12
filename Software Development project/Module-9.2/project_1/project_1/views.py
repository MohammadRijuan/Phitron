from django.http import HttpResponse

def home(request):
    return HttpResponse("This is Hompage"),

def contact(request):
    return HttpResponse("This is contact page")