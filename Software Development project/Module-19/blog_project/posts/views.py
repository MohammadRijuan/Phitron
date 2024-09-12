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


# add post class based view...we can do like that as well
# we can use this instead of previous one
from django.views.generic import CreateView
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator


@method_decorator(login_required,name='dispatch')
class AddPostCreateView(CreateView):
    model =models.posts
    form_class = forms.post_form
    template_name = "add_posts.html"
    success_url = reverse_lazy('add_posts')

    def form_valid(self, form): 
        form.instance.author = self.request.user
        return super().form_valid(form)







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




from django.views.generic import UpdateView

@method_decorator(login_required,name='dispatch')
class EditPostView(UpdateView):
    model = models.posts
    form_class = forms.post_form
    template_name = 'add_posts.html'
    pk_url_kwarg = 'id'
    success_url = reverse_lazy('profile')








@login_required
def delete_posts(request,id):
    post = models.posts.objects.get(pk=id)
    post.delete()
    return redirect('homepage')



from django.views.generic import DeleteView

@method_decorator(login_required,name='dispatch')
class DeletePostView(DeleteView):
    model = models.posts
    
    template_name = 'delete.html'
    pk_url_kwarg = 'id'
    success_url = reverse_lazy('profile')





# to show ur post details
from django.views.generic import DetailView

class DetailPostView(DetailView):
    model = models.posts
    pk_url_kwarg = 'id'
    template_name = 'post_details.html'

    def post(self,request,*args,**kwargs):
        comment_form = forms.CommentForm(data =self.request.POST)
        post = self.get_object()
        if comment_form.is_valid():
            new_comment = comment_form.save(commit=False)
            new_comment.post = post 
            new_comment.save()
        return self.get(request,*args,**kwargs)  

    def get_context_data(self,**kwargs):
        context = super().get_context_data(**kwargs)
        post = self.object # amdr post model er object
        comments = post.comments.all()
        comment_form = forms.CommentForm()

        context['comments'] = comments
        context['comment_form'] = comment_form
        return context


