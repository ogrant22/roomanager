from django.contrib import admin
from app.models import Household, UserProfile, Event, Bill, Resident

# Register your models here.
admin.site.register(Household)
admin.site.register(UserProfile)
admin.site.register(Event)
admin.site.register(Bill)
admin.site.register(Resident)
