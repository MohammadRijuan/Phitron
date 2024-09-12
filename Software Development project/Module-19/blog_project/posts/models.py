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
    image = models.ImageField(upload_to ='posts/media/uploads/',blank=True,null=True)

 
    def __str__(self):
        return self.title
    


class Comment(models.Model):
    post = models.ForeignKey(posts, on_delete=models.CASCADE, related_name='comments')
    name = models.CharField(max_length=30)
    email = models.EmailField(max_length=254)
    body = models.TextField()
    created_on =models.DateTimeField( auto_now_add=True) # jokon ei class e obj craete hobe tokhon e sey time ta reke dibe

    def __str__(self):
        return f"comments by {self.name}"