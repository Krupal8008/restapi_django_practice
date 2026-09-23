from django.urls import path
from . import views

urlpatterns = [
    path('post/', views.get_blogs , name='getpost'),
    path('make/',views.make_post,name="makepost")
]