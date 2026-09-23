from django.db import models
from django.contrib.auth.models import User 
#Used for bringing is data

class Blogs(models.Model):
    title = models.CharField(max_length=200)
    body=models.TextField()

    #Connects the posts to user. Posts are deleted with the actual user is deleted (CASCADE)
    author=models.ForeignKey(User,on_delete=models.CASCADE,related_name="blogs")

    def __str__(self):
        return self.title
    