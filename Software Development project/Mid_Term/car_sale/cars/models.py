from django.db import models
from brands.models import Brand
from django.contrib.auth.models import User

# Create your models here.

# car section
class Car(models.Model):
    name= models.CharField(max_length=50)
    description = models.TextField()
    price=models.DecimalField(max_digits=12, decimal_places=2)
    quantity = models.PositiveIntegerField(default=0)
    image = models.ImageField(upload_to='cars/media/uploads/', blank=True, null=True)
    brand = models.ManyToManyField(Brand)
    purchase_history = models.ManyToManyField(User, through='purchase')

    def __str__(self):
        return self.name



# comment section
class Comment(models.Model):
    car = models.ForeignKey(Car, on_delete=models.CASCADE, related_name='comments')
    name = models.CharField(max_length=50)
    email= models.EmailField(max_length=254)
    body=models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'comment by {self.name}'
    
# purchase Section
class Purchase(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    car = models.ForeignKey(Car,on_delete=models.CASCADE)
    purchase_date = models.DateTimeField(auto_now_add=True)
