from django.urls import path 
from . import views 

# URL configuration
urlpatterns = [
    path('home/', views.index, name = "home"),
    path('about/', views.about, name = "about")
]

