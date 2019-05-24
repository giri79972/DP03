from django.shortcuts import render
from django.http.response import HttpResponse
# Create your views here.

def index(request):
    x="<h1>Welcome to First Django Program</h1>"
    return HttpResponse(x)