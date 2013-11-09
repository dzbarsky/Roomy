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
        house = user.house
        request.session['houseName'] = house.name
        return render(request, 'Roomy/index.html', dict(getParams(request), **{'roomyUser': user.id}))
    else:
        return createUser(request)

def logout(request):
    try:
        del request.session['username']
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


def getUsers():
    return [user for user in User.objects.all()]

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
            'users': getUsers(),
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
    print user
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
    house = House.objects.get(name=request.session['houseName'])
    users = User.objects.filter(house=house.id)
    return render(request, 'Roomy/viewHouse.html', {'users':users})

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
    response = HttpResponse()
    title=request.POST['title']
    content=request.POST['content']

    
    existing = Note.objects.filter(title=title)
    if existing.count() > 0:
        note = Note.objects.get(title=title)
        note.content = content
        note.save()
        response['title'] = title
        response['id'] = note.id
        response['content'] = content
        print response

        data = json.dumps({'title': title, 'id': note.id, 'content': content})
        return HttpResponse(data, content_type="application/json")

    house=request.POST['house']

    house_object = House.objects.get(id=house)
    note = Note(title=title, content=content, house=house_object)
    note.save()
    response['title'] = title
    response['id'] = note.id
    response['content'] = content
    
    print response
 
    data = json.dumps({'title': title, 'id': note.id, 'content': content})
    return HttpResponse(data, content_type="application/json")

def getNotes(request):
    notes = []
    for note in Note.objects.all():
        notes.append(note)
    return notes

def notes(request):
    return render(request, 'Roomy/notes.html', dict(getParams(request), **{ 'notes': getNotes(request) }))

def channel(request):
    return render(request, 'Roomy/channel.html')
