from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse


def home(request):
    return HttpResponse("Hello, world. You're at the home index.")

def polls(request):
    return HttpResponse("Hello, world. You're at the polls index.")
