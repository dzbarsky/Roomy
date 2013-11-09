from django.http import HttpResponse
from django.shortcuts import render

from Roomy.models import *
import json

def signin(request):
    name = request.GET['name']
    existing = User.objects.filter(name=name)
    if existing.count() > 0:
        user = User.objects.get(name=name)
        request.session['username'] = name
        return render(request, 'Roomy/index.html', dict(getParams(), **{'roomyUser': user.id}))
    else:
        return createUser(request)

def logout(request):
    try:
        del request.session['username']
    except KeyError:
        pass
    return render(request, 'Roomy/index.html')

def getCharges():
    return [charge for charge in Charge.objects.all()]

def getUsers():
    return [user for user in User.objects.all()]

def getChores():
    return [chore for chore in Chore.objects.all()]

def getParams():
    return {'charges': getCharges(), 'users': getUsers(), 'chores': getChores()}

def index(request):
    return render(request, 'Roomy/index.html', getParams())

def createHouse(request):
    return render(request, 'Roomy/createHouse.html', getParams())

def createUser(request):
    return render(request, 'Roomy/newuser.html', getParams())

def newUser(request):
    name = request.POST['name']
    email = request.POST['email']
    phone = request.POST['phone']
    user = User(name=name, email=email, phone=phone)
    user.save()
    return HttpResponse()

def chores(request):
    return render(request, 'Roomy/chores.html', getParams())

def addChore(request):
    name = request.POST['name']
    frequency = request.POST['frequency']
    users = request.POST['users']
    users = [user for user in User.objects.all() if str(user.id) in users]
    chore = Chore(name=name, frequency=frequency)
    chore.save()
    for user in users:
      chore.users.add(user)
    chore.save()
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
    return render(request, 'Roomy/charge.html', getParams())

def doCharge(request):
    note = request.POST['note']
    amount = request.POST['amount']
    users = request.POST['users']
    users = [user for user in User.objects.all() if str(user.id) in users]
    charge = Charge(note=note, amount=amount)
    charge.save()
    for user in users:
      charge.users.add(user)
    print "SAVED"
    return HttpResponse()

def lists(request):
    return render(request, 'Roomy/lists.html', getParams())

def notes(request):
    return render(request, 'Roomy/notes.html', getParams())

def savedNotes(request):
    title=request.POST['title']
    content=request.POST['content']
    house=request.POST['house']

    house_object = House.objects.get(id=house)
    note = Note(title=title, content=content, house=house_object)
    note.save()
    return HttpResponse()
