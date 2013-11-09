from django.db import models

class User(models.Model):
    name=models.CharField(max_length=100, unique=True)
    email=models.CharField(max_length=100)
    phone=models.CharField(max_length=40)

class Houses(models.Model):
    name=models.CharField(max_length=140)
    number=models.CharField(max_length=10)
    street=models.CharField(max_length=60)
    city=models.CharField(max_length=60)
    state=models.CharField(max_length=20)
    zipcode=models.CharField(max_length=5)
    users=models.ManyToManyField(User)

class Charge(models.Model):
    note=models.CharField(max_length=140)
    amount=models.DecimalField()
    users=models.ManyToManyField(User)
