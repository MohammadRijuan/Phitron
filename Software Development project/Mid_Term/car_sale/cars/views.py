from django.db.models.query import QuerySet
from django.shortcuts import render,redirect,get_object_or_404
from . import forms
from django.contrib.auth.decorators import login_required
from . models import Car,Purchase,Brand
from brands.models import Brand


# Create your views here.
@login_required
def Add_Car(request):
    if request.method == 'POST':
        car_form = forms.CarForm(request.POST)

        if car_form.is_valid():
            car_form.instance.author = request.user
            car_form.save()
            return redirect('profile')
    else:
        car_form = forms.CarForm()
    return render(request,'add_car.html',{'form':car_form})


# we can use anyone of it
# i will use class based view in this project

from django.views.generic import CreateView
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator


@method_decorator(login_required,name='dispatch')
class AddCarView(CreateView):
    model =Car
    form_class = forms.CarForm
    template_name = "add_car.html"
    success_url = reverse_lazy('add_car')

    def form_valid(self, form): 
        form.instance.author = self.request.user
        return super().form_valid(form)


from django.views.generic import ListView, CreateView

class Car_list(ListView):
    model = Car
    template_name = 'car_list.html'

    def get_queryset(self) :
        return Car.objects.all()
    
def car_list_by_brand(request, category_slug=None):
    data = Car.objects.all()
    categories = Brand.objects.all()

    if category_slug is not None:
        category = Brand.objects.get(slug=category_slug)
        data = Car.objects.filter(brand=category)
    print(data)

    return render(request,'car_list.html',{'data':data ,'categories':categories})


from django.views.generic import DetailView

class DetailPostView(DetailView):
    model = Car
    form_class = forms.CarForm
    pk_url_kwarg = 'id'
    template_name = 'car_detail.html'

    def post(self, request, *args, **kwargs):
        post = self.get_object()
        comment_form = forms.CommentForm(data=request.POST)
        if comment_form.is_valid():
            new_comment = comment_form.save(commit=False)
            new_comment.car = post  
            new_comment.save()
        return self.get(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        post = self.object
        comments = post.comments.all()
        comment_form = forms.CommentForm()

        if not post.image:
            context['image'] = 'path/to/default-image.jpg'  # Provide a default image
        else:
            context['image'] = post.image.url

        context['comments'] = comments
        context['comment_form'] = comment_form
        return context
    

from django.shortcuts import get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages

@login_required
def purchased_cars(request, car_id):
    car = get_object_or_404(Car, pk=car_id)
    
    if request.method == 'POST':
        if car.quantity > 0:
            purchase = Purchase(user=request.user, car=car)
            purchase.save()
            car.quantity -= 1
            car.save()
            messages.success(request, 'Purchase successful.')
        else:
            messages.error(request, 'This car is out of stock.')
        return redirect('car_detail', id=car_id)

    return redirect('car_detail', id=car_id)
