from django.db import models

class User(models.Model):
    name=models.CharField(max_length=100)
    phone=models.CharField(max_length=40, null=True)
    house=models.ForeignKey('House', null=True)

class House(models.Model):
    name=models.CharField(max_length=140)
    number=models.CharField(max_length=10)
    street=models.CharField(max_length=60)
    city=models.CharField(max_length=60)
    state=models.CharField(max_length=20)
    zipcode=models.CharField(max_length=5)

class Charge(models.Model):
    note=models.CharField(max_length=140)
    amount=models.DecimalField(max_digits=10, decimal_places=2)
    users=models.ManyToManyField(User)

class Day(models.Model):
    short=models.CharField(max_length=3)
    full=models.CharField(max_length=10)

class Chore(models.Model):
    name=models.CharField(max_length=140)
    users=models.ManyToManyField(User)
    frequency=models.CharField(max_length=20) 
    day=models.ForeignKey('Day', null=True)

class Note(models.Model):
    title=models.CharField(max_length=100)
    content=models.CharField(max_length=2500)
    house=models.ForeignKey(House)
