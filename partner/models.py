from django.db import models
from ckeditor.fields import RichTextField

# Create your models here.
class PartnerModel(models.Model):
    name = models.CharField(max_length=100)
    description = RichTextField(null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name