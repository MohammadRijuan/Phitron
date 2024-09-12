from django.shortcuts import render,redirect
from . forms import Album_form


# Create your views here.
def add_albums(request):
    form=Album_form()

    if request.method =='POST':
        form=Album_form(request.POST)

        if form.is_valid():
            form.save()
            return redirect('add_albums')
    return render(request,'add_albums.html',{'form':form})

