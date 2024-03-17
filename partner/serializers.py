from rest_framework import serializers
from .models import PartnerModel

class PartnerSerializer(serializers.ModelSerializer):
    class Meta:
        model = PartnerModel
        # fields = ["name", "description"]
        fields = "__all__"
