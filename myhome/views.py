from http.client import HTTPResponse
from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return render(request, 'pages/home.html')

def about(request):
    return render(request, 'pages/about.html')

def error(request, exception):
    return render(request, 'pages/error.html', {'message': exception})                       #



    # response = HttpResponse()
    # response.writelines('<h1> Hello </h1>')
    # response.write('This is app my home')
    # return response