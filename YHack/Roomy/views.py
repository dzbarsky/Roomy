from django.http import HttpResponse
from django.shortcuts import render
from twilio.rest import TwilioRestClient

from Roomy.models import *
import json

def signin(request):
    name = request.GET['name']
    existing = User.objects.filter(name=name)
    if existing.count() > 0:
        user = User.objects.get(name=name)
        request.session['username'] = name
        if user.house:
            house = user.house
            request.session['houseName'] = house.name
        return render(request, 'Roomy/index.html', dict(getParams(request), **{'roomyUser': user.id}))
    else:
        return createUser(request)

def logout(request):
    try:
        del request.session['username']
        del request.session['houseName']
    except KeyError:
        pass
    return render(request, 'Roomy/index.html')

def getCharges(request):
    charges = []
    if 'username' not in request.session:
        return charges

    for charge in Charge.objects.all():
        for user in charge.users.all():
            if user.name == request.session['username']:
                charges.append(charge)
                continue
    return charges


def getUsers(request):
    house = House.objects.get(name=request.session['houseName'])
    return [user for user in User.objects.filter(house=house.id)]

def getChores(request):
    chores = []
    if 'username' not in request.session:
        return chores

    for chore in Chore.objects.all():
        for user in chore.users.all():
            if user.name == request.session['username']:
                chores.append(chore)
                continue
    return chores

def getParams(request):
    return {'charges': getCharges(request),
            'users': getUsers(request),
            'chores': getChores(request),
            'notes': getNotes(request)}

def index(request):
    return render(request, 'Roomy/index.html', getParams(request))

def view404(request):
    return render(request, '404.html', getParams(request))

def createHouse(request):
    return render(request, 'Roomy/createHouse.html', getParams(request))

def createUser(request):
    name = request.GET['name']
    return render(request, 'Roomy/newuser.html', dict(getParams(request), **{"name": name}))

def newUser(request):
    name = request.POST['name']
    phone = request.POST['phone']
    user = User(name=name, phone=phone)
    user.save()
    request.session['username'] = name
    return render(request, 'Roomy/createHouse.html')

def chores(request):
    return render(request, 'Roomy/chores.html', getParams(request))

def addChore(request):
    name = request.POST['name']
    frequency = request.POST['frequency']
    day = request.POST['day']
    users = request.POST['users']
    users = [user for user in User.objects.all() if str(user.id) in users]
    chore = Chore(name=name, frequency=frequency, day=day)
    chore.save()
    for user in users:
      chore.users.add(user)
    chore.save()
    return HttpResponse()

def newHouse(request):
    user = User.objects.get(name=request.session['username'])
    data = json.loads(request.POST['houseData'])
    house = House(name=data['name'], \
        number=data['stnumber'], \
        street=data['street'], \
        city=data['city'], \
        state=data['state'], \
        zipcode=data['zipcode'])
    house.save()
    user.house = house
    user.save()
    users = request.POST['users']
    for ind in json.loads(users):
        user = json.loads(json.loads(users)[ind])
        newUser = User(name=user['username'],phone=user['phone'],house=house)
        newUser.save()
    request.session['houseName'] = data['name']
    return render(request, 'Roomy/index.html')

def viewHouse(request):
    return render(request, 'Roomy/viewHouse.html', getParams(request))

def charge(request):
    return render(request, 'Roomy/charge.html', getParams(request))

def doCharge(request):
    note = request.POST['note']
    amount = request.POST['amount']
    users = request.POST['users']
    users = [user for user in User.objects.all() if str(user.id) in users]
    charge = Charge(note=note, amount=amount)
    charge.save()
    for user in users:
      charge.users.add(user)
    return HttpResponse()

def lists(request):
    return render(request, 'Roomy/lists.html', getParams(request))

def savedNotes(request):
    title=request.POST['title']
    content=request.POST['content']
    house=request.POST['house']

    house_object = House.objects.get(id=house)
    note = Note(title=title, content=content, house=house_object)
    note.save()
    return HttpResponse()

def getNotes(request):
    notes = []
    for note in Note.objects.all():
        notes.append(note)
    return notes

def notes(request):
    return render(request, 'Roomy/notes.html', dict(getParams(request), **{ 'notes': getNotes(request) }))

def textReminder(request):
    recipient = request.POST['recipient']
    message = request.POST['message']
    account_sid = "AC0e0571d94d5d6dba4ac914247086bde1"
    auth_token = "1048a4e4a412d86677011b93d0300995"
    client = TwilioRestClient(account_sid, auth_token)
    message = client.messages.create(body=message,
       to=recipient, from_="+19292274747")
    return HttpResponse()

