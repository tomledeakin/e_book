import os
from django.db import models
from category.models import CategoryModel
from author.models import AuthorModel
from ckeditor.fields import RichTextField

# Create your models here.
class ProductModel(models.Model):
    
    category = models.ForeignKey(CategoryModel, on_delete=models.PROTECT, null=True)
    # author = models.CharField(max_length=100)
    author = models.ForeignKey(AuthorModel, on_delete=models.PROTECT, null=True)
    product_name = models.CharField(max_length=100)
    summary = models.CharField(max_length=500, null=True)
    price = models.IntegerField(null=True)
    quantity = models.IntegerField(default=0)

    # description = models.TextField(null=True)
    description = RichTextField(null=True)
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    delete_flg = models.BooleanField(null=True)
    image = models.ImageField(null=True, upload_to="images/")
    file = models.FileField(null=True, upload_to="files/")
    url = models.URLField(null=True)
    content = RichTextField(null=True)

    def __str__(self):
        return self.product_name
    
    @property
    def get_file_name(self):
        return os.path.basename(self.file.url) if self.file else ""
