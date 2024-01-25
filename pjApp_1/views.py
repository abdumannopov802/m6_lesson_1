from django.shortcuts import render
from django.http import HttpResponse



def sayhello(request):
    return render(request=request, template_name="index.html", context={})

def mainview(request):
    return HttpResponse ("Main View")

def uzbekistan(request):
    return HttpResponse ("O'zbekiston yangiliklari bo'limi")

def jahon(request):
    return HttpResponse ("Jahon Yangiliklari bo'limi")

def iqtisodiyot(request):
    return HttpResponse ("Iqtisodiyot yangiliklri bo'limi")

def jamiyat(request):
    return HttpResponse ("Jamiyat bo'limi")

def fan_texnika(request):
    return HttpResponse ("Fan va Texnika yangiliklari")

def sport(request):
    return HttpResponse ("Sport yangiliklari")

def nuqtainazar(request):
    return HttpResponse ("Nuqtai Nazar")

def audio(request):
    return HttpResponse ("Audio bo'limi")