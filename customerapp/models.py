from django.db import models
from mainapp.models import Customer
# Create your models here.
class Response(models.Model):
    user = models.ForeignKey(Customer,on_delete=models.CASCADE)
    responsetype = models.CharField(max_length=10)
    responsetext = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
