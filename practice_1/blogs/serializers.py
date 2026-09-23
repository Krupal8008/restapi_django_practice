from rest_framework import serializers
from .models import Blogs

class BlogSerializer(serializers.ModelSerializer):
    author = serializers.ReadOnlyField(source="author.username")
    # reads the username of the login user.
    class Meta:
        model= Blogs
        fields=['id','title','body','author']