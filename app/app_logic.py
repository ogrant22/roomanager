from app.models import Household, UserProfile, Resident
from django.contrib.auth.models import User


def add_resident(h, u): #takes a reference to a household object and a user object, returns a resident object containing a reference to both
    residents = Resident.objects.filter(household = h)
    if residents.__len__ == h.max_residents:
        print("max residents already reached")
        return
    elif residents.__len__ == 0:
        r = Resident.objects.get_or_create(user = u, household = h, active = True)[0]
        h.lead_tenant = u
        h.save()
        r.save()
        return r
    else:
        r = Resident.objects.get_or_create(user = u, household = h, active = True)[0]
        r.save()
        return r


