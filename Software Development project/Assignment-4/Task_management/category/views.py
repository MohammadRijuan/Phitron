from django.shortcuts import render,redirect
from . forms import Category_form
# Create your views here.
def add_category(request):
    form=Category_form()

    if request.method== 'POST':
        form=Category_form(request.POST)

        if form.is_valid():
            form.save()
        return redirect('add_category')
    return render(request,'add_category.html',{'form':form})