from django.shortcuts import render
from django.http import HttpResponse
from playground.models import *

# Create your views here.

# def say_hello(request):
#     return HttpResponse("Hello World")

# def cal():
#     x = 1
#     y = 2
#     return x

# def say_hello(request):
#     x = cal()
#     y = 2
#     return render(request, 'hello.html', {'name': "Durga Prasad"})

def form(request):
    if request.method == 'POST':
        a = request.POST.get('username')
        b = request.POST.get('surname')
        c = request.POST.get('email')
        list_display = FormModels(username = a, surname = b, email = c)
        list_display.save()
    return render(request, 'form.html')