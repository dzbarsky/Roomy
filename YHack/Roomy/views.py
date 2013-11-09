from django.http import HttpResponse
from django.shortcuts import render

from Roomy.models import *
import json

def getCharges():
    return [charge for charge in Charge.objects.all()]

def getChargesDict():
    return {'charges': getCharges()}

def getUsers():
    return [user for user in User.objects.all()]

def index(request):
    return render(request, 'Roomy/index.html', getChargesDict())

def createHouse(request):
    return render(request, 'Roomy/createHouse.html', getChargesDict())

def createUser(request):
    return render(request, 'Roomy/newuser.html', getChargesDict())

def newUser(request):
    name = request.POST['name']
    email = request.POST['email']
    phone = request.POST['phone']
    user = User(name=name, email=email, phone=phone)
    user.save()
    return HttpResponse()

def chores(request):
    return render(request, 'Roomy/chores.html', {'users': getUsers(),
                                                 'charges': getCharges()})

def addChore(request):
    '''
    name = request.POST['name']
    email = request.POST['email']
    phone = request.POST['phone']
    user = User(name=name, email=email, phone=phone)
    user.save()
    '''
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
    return render(request, 'Roomy/charge.html', {'users': getUsers(),
                                                 'charges': getCharges()})

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
    return render(request, 'Roomy/lists.html', getChargesDict())

def notes(request):
    return render(request, 'Roomy/notes.html', getChargesDict())
