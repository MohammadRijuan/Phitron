from django.db import models
from categories.models import category
from   author.models import Author

# Create your models here.
class posts(models.Model):
    title=models.CharField(max_length=50)
    content=models.TextField()
    Category=models.ManyToManyField(category) # multiple post thakte pare
    author=models.ForeignKey(Author,on_delete=models.CASCADE) #jodi author delete hoy
 
    def __str__(self):
        return self.title