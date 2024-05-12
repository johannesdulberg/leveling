from django.urls import path
from django.shortcuts import render, redirect

def index(request):

    return render(request, "standing/standing_skilltree.html")

