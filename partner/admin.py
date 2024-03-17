from django.contrib import admin
from .models import PartnerModel
from ckeditor.widgets import CKEditorWidget
from django import forms

# Register your models here.
class PartnerAdminForm(forms.ModelForm):
    description = forms.CharField(widget=CKEditorWidget())
    class Meta:
        model = PartnerModel
        fields = "__all__"

class PartnerAdmin(admin.ModelAdmin):
    form = PartnerAdminForm


admin.site.register(PartnerModel, PartnerAdmin)
