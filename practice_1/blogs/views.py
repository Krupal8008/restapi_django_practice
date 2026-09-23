from django.shortcuts import render
from rest_framework.decorators import api_view,permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
from .models import Blogs
from .serializers import BlogSerializer

@api_view(['GET'])
def get_blogs(request):
    blogs= Blogs.objects.all()
    serial=BlogSerializer(blogs,many=True)
    return Response(serial.data)

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def make_post(request):
    serial= BlogSerializer(data=request.data)
    if serial.is_valid():
        serial.save(author=request.user)
        return Response(serial.data, status=status.HTTP_201_CREATED)
    return Response(serial.errors, status=status.HTTP_400_BAD_REQUEST)