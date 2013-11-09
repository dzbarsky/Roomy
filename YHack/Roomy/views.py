from django.http import HttpResponse
from django.shortcuts import render

from Roomy.models import *
import json

def index(request):
    return render(request, 'Roomy/index.html')

def createHouse(request):
    return render(request, 'Roomy/createHouse.html')

def newUser(request):
    name = request.POST['name']
    email = request.POST['email']
    phone = request.POST['phone']
    user = User(name=name, email=email, phone=phone)
    user.save()
    return HttpResponse()

def newHouse(request):
    data = json.loads(request.POST['houseData'])
    house = House(name=data['name'], \
		  number=data['stnumber'], \
		  street=data['street'], \
		  city=data['city'], \
		  state=data['state'], \
		  zipcode=data['zipcode'])
    house.save()
    users = request.POST['users']
    for ind in json.loads(users):
	user = json.loads(json.loads(users)[ind])
        newUser = User(name=user['username'],email=user['email'],phone=user['phone'])
        newUser.save()
        house.users.add(newUser)
    return HttpResponse()

def charge(request):
    users = User.objects.all()
    usersDict = []
    for user in users:
        usersDict.append(user)
    return render(request, 'Roomy/charge.html', {'users': users})
