from django.db import models

# Create your models here.
class LoginInfo(models.Model):
    usertype =models.CharField(max_length=20)
    username =models.CharField(max_length=100)
    password =models.CharField(max_length=128)
    def __str__(self):
        return f"{self.username} -> {self.usertype}"
    
class Customer(models.Model):
    login =models.OneToOneField(LoginInfo, on_delete=models.CASCADE)
    name =models.CharField(max_length=100)
    gender =models.CharField(max_length=15)
    contactno =models.CharField(max_length=15)
    email =models.CharField(max_length=100)
    address =models.TextField()
    picture =models.ImageField(upload_to='profiles/')
    regdate =models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return f"{self.name} - {self.email}"