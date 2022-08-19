from django.urls import path 
from . import views 

# URL configuration
urlpatterns = [
    path('', views.list, name="blog"),
    path('<int:pid>/', views.post, name="post"), #browser will base on name to take the corresponding path
]



