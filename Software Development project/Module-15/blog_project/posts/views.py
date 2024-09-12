from django.shortcuts import render,redirect
from . import forms
from . import models
# Create your views here.
def add_posts(request):
    if request.method == 'POST':  
        post_form = forms.post_form(request.POST)
        if post_form.is_valid():
            post_form.save()
            return redirect('add_posts')
    else:
        post_form = forms.post_form()
    return render(request,'add_posts.html',{'form':post_form})


def edit_posts(request, id):

    post=models.posts.objects.get(pk=id) #post er instance ck korte models er function dhore call korbo..r kon id seta primary key diye detact kora jbe
    post_form = forms.post_form(instance=post)
    
    if request.method == 'POST':  
        post_form = forms.post_form(request.POST,instance=post)
        if post_form.is_valid():
            post_form.save()
            return redirect('add_posts')
    else:
        post_form = forms.post_form()
    post_form = forms.post_form(request.POST)
    return render(request,'add_posts.html',{'form':post_form})

def delete_posts(request,id):
    post = models.posts.objects.get(pk=id)
    post.delete()
    return redirect('homepage')