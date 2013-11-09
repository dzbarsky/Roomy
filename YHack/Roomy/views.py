from django.http import HttpResponse
from django.shortcuts import render

from Roomy.models import *
import json

def index(request):
    return render(request, 'Roomy/index.html')

def createHouse(request):
    return render(request, 'Roomy/createHouse.html')

def createUser(request):
    return render(request, 'Roomy/newuser.html')

def newUser(request):
    name = request.POST['name']
    email = request.POST['email']
    phone = request.POST['phone']
    user = User(name=name, email=email, phone=phone)
    user.save()
    return HttpResponse()

def chores(request):
    return render(request, 'Roomy/chores.html')

def newHouse(request):
    name = request.POST['name']
    number = request.POST['number']
    street = request.POST['street']
    city = request.POST['city']
    state= request.POST['state']
    zipcode= request.POST['zipcode']
    roomies = json.dumps(request.POST['roomies'])
    print roomies
    house = House(name=name, number=number, street=street, city=city, state=state, zipcode=zipcode)
    house.save()
    return HttpResponse()

def charge(request):
    users = User.objects.all()
    usersDict = []
    for user in users:
        usersDict.append(user)
    return render(request, 'Roomy/charge.html', {'users': users})

def doCharge(request):
    note = request.POST['note']
    amount = request.POST['amount']
    users = request.POST['users']
    users = [user for user in User.objects.all() if str(user.id) in users]
    charge = Charge(note=note, amount=amount)
    charge.save()
    for user in users:
      charge.users.add(user)
    charge.save()
    print "SAVED"
    return HttpResponse()

def lists(request):
    return render(request, 'Roomy/lists.html')

def notes(request):
    return render(request, 'Roomy/notes.html')
