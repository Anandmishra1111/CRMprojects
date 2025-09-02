from django.db import models

# Create your models here.
class Product(models.Model):
    pid = models.AutoField(primary_key=True)
    name= models.CharField(max_length=200)
    description =models.TextField()
    price = models.DecimalField(decimal_places=2,max_digits=10)
    mfgdate =models.DateField()
    expdate =models.DateField()
    picture =models.ImageField(upload_to='products/')
    created_at =models.DateTimeField(auto_now_add=True)