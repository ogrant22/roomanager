import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'roomanager.settings')
import django
django.setup()
from app.models import Household, UserProfile, Event, Bill, Resident
from django.contrib.auth.models import User
from app.app_logic import add_resident

def populate():
    users =[
        {"user": "ogrant453", "first": "Oran", "surname":"Grant", "email": "ogrant453@gmail.com", "password":"password123"},
        {"user": "engine24", "first": "Ayuub", "surname":"Ahmed", "email": "aayuub24@gmail.com", "password":"password123"},
        {"user": "humper", "first": "Humphrey", "surname":"Borsi", "email": "hbors1@gmail.com", "password":"password123"},
        {"user": "hawaii", "first": "Etienne", "surname":"Salle", "email": "moana15@gmail.com", "password":"password123"},
    ]

    h1 = Household.objects.get_or_create(name = "Snaffle", address = "24 kelvingrove road")[0]
    print(h1)
    for data in users:
        u = User.objects.get_or_create(username = data["user"], password = data["password"], email = data["email"])[0]
        add_resident(h1, u)
        u.save()
        p = UserProfile.objects.get_or_create(user = u)[0]
        p.save()
        print(u)

if __name__ == '__main__':
    print('Starting roomanager population script...')
    populate()

