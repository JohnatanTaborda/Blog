from django.shortcuts import render
from django.http import HttpResponse
from django.template import Template, loader


def home (request):
    return render (request, "home.html")

def acerca (request):
    return render (request, "acerca.html")

