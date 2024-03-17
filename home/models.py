from django.db import models

class PromotionModel(models.Model):
    image = models.ImageField(null=True, upload_to="images/")
    created_at = models.DateTimeField(auto_now_add=True)