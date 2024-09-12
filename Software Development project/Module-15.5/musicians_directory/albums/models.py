from django.db import models
from musicians.models import Musicians
# Create your models here.
class Albums(models.Model):
    name=models.CharField(max_length=50)
    release_date=models.DateTimeField()
    
    rate=[
        ('1','1'),
        ('2','2'),
        ('3','3'),
        ('4','4'),
        ('5','5')]

    rating=models.CharField(max_length=1, choices=rate)
    artist=models.ForeignKey(Musicians,on_delete=models.CASCADE, related_name='add_albums')

    def __str__(self):
        return self.name