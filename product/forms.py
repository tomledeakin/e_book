from django import forms
from .models import ProductModel
from ckeditor.widgets import CKEditorWidget
from ckeditor_uploader.widgets import CKEditorUploadingWidget

class ProductForm(forms.Form):
    product_name = forms.CharField(label="Ten san pham", max_length=100, required=True)
    summary = forms.CharField(label="Tom tat", max_length=500)
    # description = forms.CharField(label="Mo ta chi tiet", widget=forms.Textarea)
    description = forms.CharField(widget=CKEditorUploadingWidget())
    content = forms.CharField(widget=CKEditorUploadingWidget())
    price = forms.IntegerField(label="Gia")
    quantity = forms.IntegerField(label="So luong")
    url = forms.URLField(label="Link")

    def save(self):
        model = ProductModel(
            product_name = self.cleaned_data["product_name"],
            summary = self.cleaned_data["summary"],
            description = self.cleaned_data["description"],
            content = self.cleaned_data["content"],
            price = self.cleaned_data["price"],
            quantity = self.cleaned_data["quantity"],
        )
        model.save()

class ProductModelForm(forms.ModelForm):
    description = forms.CharField(widget=CKEditorUploadingWidget())
    content = forms.CharField(widget=CKEditorUploadingWidget())
    class Meta:
        model = ProductModel
        fields = '__all__'
