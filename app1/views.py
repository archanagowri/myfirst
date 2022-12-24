from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def gracy(request):
    return HttpResponse('<h1><b><i><font color=green><marquee>Gracy Is Very Motivation Girl</marquee></font></i></b></h1>')

def anu(request):
    return HttpResponse('<h1><b><i><font color=red><marquee>Anu Is Special</marquee></font></i></b></h1>')