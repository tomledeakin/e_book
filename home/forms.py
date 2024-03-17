from django import forms
from .models import PromotionModel


class PromotionModelForm(forms.ModelForm):
    image = forms.ImageField(label="Image")
    class Meta:
        model = PromotionModel
        fields = '__all__'
