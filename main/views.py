from django.shortcuts import render
from django.http import HttpResponse
from .models import TableBase

# Create your views here.
def index(request):
    return render(request, "main/reg.html")

def vh(request):
    return render(request, "main/vh.html")

def landing(request):
    return render(request, "main/zer.html")

def lk(request):
    users = TableBase.objects.all()
    return render(request, "main/ww.html", {'title': 'Личный кабинет',  'data': users})
