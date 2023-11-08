from django.shortcuts import render

from django.http import HttpResponse
# Create your views here.
def helo(request):
    return HttpResponse('<h1><marquee>Hi hello .. Successfully django running </marquee></h1>')
