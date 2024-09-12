from django.shortcuts import render,redirect,get_object_or_404
from . import models, forms
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required
def add_posts(request):
    if request.method == 'POST':  
        post_form = forms.post_form(request.POST)
        if post_form.is_valid():
            post_form.instance.author = request.user
            post_form.save()
            return redirect('profile')
    else:
        post_form = forms.post_form()
    return render(request,'add_posts.html',{'form':post_form})

@login_required
def edit_posts(request, id):
    post=models.posts.objects.get(pk=id)
    # post = get_object_or_404(models.posts, pk=id) #post er instance ck korte models er function dhore call korbo..r kon id seta primary key diye detact kora jbe
    post_form = forms.post_form(instance=post)
    
    if request.method == 'POST':  
        post_form = forms.post_form(request.POST,instance=post)
        if post_form.is_valid():
            post_form.instance.author = request.user
            post_form.save()
            return redirect('add_posts')
    else:
        post_form = forms.post_form()
    post_form = forms.post_form(request.POST)
    return render(request,'add_posts.html',{'form':post_form})

@login_required
def delete_posts(request,id):
    post = models.posts.objects.get(pk=id)
    post.delete()
    return redirect('homepage')