from django.http import HttpResponse
from django.shortcuts import render

from Roomy.models import *

def index(request):
    return render(request, 'Roomy/index.html')

def newUser(request):
    name = request.POST['name']
    email = request.POST['email']
    phone = request.POST['phone']
    user = User(name=name, email=email, phone=phone)
    user.save()
    return HttpResponse()

def charge(request):
    users = User.objects.all()
    usersDict = []
    for user in users:
        usersDict.append(user)
    return render(request, 'Roomy/charge.html', {'users': users})

def lists(request):
    return render(request, 'Roomy/lists.html') 
