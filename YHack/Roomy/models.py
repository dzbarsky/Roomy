from django.db import models

class User(models.Model):
    name=models.CharField(max_length=100, unique=True)
    email=models.CharField(max_length=100)
    phone=models.CharField(max_length=40)

class House(models.Model):
    name=models.CharField(max_length=140)
    number=models.CharField(max_length=10)
    street=models.CharField(max_length=60)
    city=models.CharField(max_length=60)
    state=models.CharField(max_length=20)
    zipcode=models.CharField(max_length=5)
    users=models.ManyToManyField(User)

class Charge(models.Model):
    note=models.CharField(max_length=140)
    amount=models.DecimalField(max_digits=10, decimal_places=2)
    users=models.ManyToManyField(User)

class Chore(models.Model):
    name=models.CharField(max_length=140)
    users=models.ManyToManyField(User)
    frequency=models.CharField(max_length=20)
