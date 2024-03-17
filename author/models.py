from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class AuthorModel(models.Model):
    user = models.OneToOneField(User, on_delete=models.PROTECT, null=True)
    full_name = models.CharField(max_length=100)
    description = models.TextField(null=True)
    phone_number = models.CharField(max_length=20, null=True)
    country = models.CharField(max_length=100)

    def __str__(self):
        return self.full_name
    
    
    
# class CustomerModel(models.Model):
#     user = models.OneToOneField(User, on_delete=models.PROTECT)
#     full_name = models.CharField(max_length=100)
#     phone_number = models.CharField(max_length=20)
#     address = models.CharField(max_length=500)

#     def __str__(self):
#         return self.full_name