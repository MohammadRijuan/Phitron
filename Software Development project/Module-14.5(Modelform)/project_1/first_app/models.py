from django.db import models

# Create your models here.
class Client_Data(models.Model):
    First_name=models.CharField( max_length=50)
    Last_name=models.CharField( max_length=50)
    email=models.EmailField()
    address=models.TextField( max_length=200)

    CHOICES= [
        ("teamwork","teamwork"),
        ("leader","leader"),
        ("management","management")
        
    ]

    Skills=models.CharField(max_length=50,choices=CHOICES)

    def __str__(self):
        return self.First_name
    
