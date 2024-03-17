from django.shortcuts import render
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework import status
from .models import PartnerModel
from .serializers import PartnerSerializer
import requests
from rest_framework.permissions import IsAuthenticated
# Create your views here.

def partner_list(request):

    url = "http://localhost:8000/doi-tac/api/"
    response = requests.get(url)
    partners = response.json()

    context = {
        "partners": partners
    }
    return render(request, "partner/partner.html", context)


@api_view(['GET', 'POST'])
@permission_classes([IsAuthenticated])
def partner_list_api(request):
    if request.method == "GET":
        model = PartnerModel.objects.all()
        serializer = PartnerSerializer(model, many=True)
        return Response(data=serializer.data)
    
    if request.method == "POST":
        serializer = PartnerSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response()
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def partner_detail_api(request, id):
    try:
        model = PartnerModel.objects.get(id=id)
    except PartnerModel.DoesNotExist:
        return Response(data={"error": "id invalid"}, status=status.HTTP_400_BAD_REQUEST)

    if request.method == "GET":
        serializer = PartnerSerializer(model)
        return Response(data=serializer.data)
    
    if request.method == "PUT":
        serializer = PartnerSerializer(model, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response()
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    if request.method == "DELETE":
        model.delete()
        return Response()
