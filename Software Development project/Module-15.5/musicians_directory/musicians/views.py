from django.shortcuts import render,redirect
from . forms import Musician_form
from albums.models import Albums
from  musicians.models import Musicians
from . import models

# Create your views here.
def add_musicians(request):
    form=Musician_form()

    if request.method == 'POST':
        form= Musician_form(request.POST)

        if form.is_valid():
            form.save()
            return redirect('add_musicians')
    return render(request,'add_musicians.html',{'form':form})

def edit_musicians(request, id):
    musician=models.Musicians.objects.get(pk=id)
    form = Musician_form(instance=musician)
    
    if request.method == "POST":
        form = Musician_form(request.POST, instance=musician)
        
        if form.is_valid():
            form.save()
            return redirect("edit_musicians",id=musician.id)
        
    return render(request, "add_musicians.html", {"form": form})

def delete_musicians(request, id):
    musician=models.Musicians.objects.get(pk=id)
    musician.delete()
    return redirect("home")

