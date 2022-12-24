from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def stalin(request):
    return HttpResponse('<h1><b><i><font color=blue><marquee>My Brother Is My Hero</marquee></font></i></b></h1>')
def ajith(request):
    return HttpResponse('<h1><b><i><font color=green><marquee>My Brother Is My Hero</marquee></font></i></b><h1>')