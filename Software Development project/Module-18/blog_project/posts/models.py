from django.db import models
from categories.models import Category

from django.contrib.auth.models import User

# Create your models here.
class posts(models.Model):
    title=models.CharField(max_length=50)
    content=models.TextField()
    category=models.ManyToManyField(Category) # multiple post thakte pare
    # author=models.ForeignKey(Author,on_delete=models.CASCADE) #jodi author delete hoy
    
    author = models.ForeignKey(User, on_delete=models.CASCADE, default=1)

 
    def __str__(self):
        return self.title