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


@api_view(['GET', 'PUT', 'DELETE'])
@permission_classes([IsAuthenticated]) # Ensures only registered users can edit/delete
def blog_detail(request, pk):
    try:
        blog = Blogs.objects.get(pk=pk)
    except Blogs.DoesNotExist:
        return Response({'error': 'Blog not found'}, status=status.HTTP_404_NOT_FOUND)

    #Check if the logged-in user is actually the author
    if request.method in ['PUT', 'DELETE'] and blog.author != request.user:
        return Response({'detail': 'You do not have permission to edit this blog.'}, status=status.HTTP_403_FORBIDDEN)

    # 1. READ individual blog
    if request.method == 'GET':
        serial = BlogSerializer(blog)
        return Response(serial.data)

    # 2. UPDATE individual blog
    elif request.method == 'PUT':
        serial = BlogSerializer(blog, data=request.data)
        if serial.is_valid():
            serial.save()
            return Response(serial.data)
        return Response(serial.errors, status=status.HTTP_400_BAD_REQUEST)

    # 3. DELETE individual blog
    elif request.method == 'DELETE':
        blog.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)