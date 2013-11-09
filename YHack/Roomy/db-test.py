from django.db import models

from Roomy.models import *

def add_test_data():
    oliver = User(name='Oliver', email='omanheim@sas.upenn.edu', phone='847.708.9465')
    oliver.save()
    josh = User(name='Josh', email='jisenstein@gmail.com', phone='847.864.1314')
    josh.save()
    dave = User(name='Dave', email='dave@internet.com', phone='312.153.2465')
    dave.save()
    baltimore = House(name='3913', number='3913', street='Baltimore', city='Philadelphia', state='PA', zipcode='19104')
    baltimore.save()
    baltimore.users.add(oliver)
    baltimore.users.add(josh)
    baltimore.users.add(dave)

def main():
    add_test_data()

if __name__ == "__main__":
    main()
