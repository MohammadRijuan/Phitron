from django.db import models

# Create your models here.
class Musicians(models.Model):
    First_name=models.CharField( max_length=50)
    Last_name=models.CharField( max_length=50)
    email=models.EmailField()

    instr_choice= [
        ("guitar","Guitar"),
        ("cello","Cello"),
        ("flutes","Flutes"),
        ("piano","Piano")
    ]

    instrument_type=models.CharField(max_length=50,choices=instr_choice)

    def __str__(self):
        return self.First_name