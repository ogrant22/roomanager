from django.contrib import admin
from app.models import Household, UserProfile, Event, Bill, Resident
from django.contrib.auth.models import User

# Register your models here.
class HouseholdAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':('name',)}

class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('slug','picture')

admin.site.register(Household, HouseholdAdmin)
admin.site.register(UserProfile, UserProfileAdmin)
admin.site.register(Event)
admin.site.register(Bill)
admin.site.register(Resident)
