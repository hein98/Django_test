from django.db import models

# Create your models here.
class Destination(models.Model):
    name=models.CharField(max_length=50)
    description=models.TextField(max_length=100)
    img=models.ImageField(upload_to='pics')
    price=models.IntegerField()
    offer=models.BooleanField(default=False)
    
    
    def __str__(self):
        return self.name