from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, "index.html")


def secondPage(request):
    return render(request, "secondPage.html")