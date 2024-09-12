from django.shortcuts import render
from . forms import modelForm
# Create your views here.
def model(request):
    form=modelForm()
    return render(request,'model.html',{'form':form})