from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return HttpResponse("Olá... Bem vindo ao Juisse.")

def sobre(request):
    return HttpResponse("Este é um app de enquete!")        
# Create your views here.



