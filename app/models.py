from django.db import models
from django.contrib.auth.models import User

#Password1
# Create your models here.
class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    picture = models.ImageField(upload_to='profile_images', blank=True)

    def __str__(self):
        return self.user.username

class Household(models.Model):
    name = models.CharField(max_length=128, unique=False, null=False)
    address = models.CharField(max_length=128, unique=False, null = True)
    max_residents = models.IntegerField(default= 100)
    lead_resident = models.ForeignKey(User, on_delete=models.SET_NULL, null= True) #change later to set new lead tenant

    def __str__(self):
        return self.name
    
class Resident(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=False)
    household = models.ForeignKey(Household, on_delete=models.CASCADE, null=False)
    active = models.BooleanField(default=True)

    def __str__(self):
        return self.user + "/" + self.household + "/" + self.active
    
class Bill(models.Model):
    name = models.CharField(max_length = 128)
    reciever = models.CharField(max_length=256)
    due_date = models.IntegerField()
    period_type = models.CharField(max_length = 128)
    period_covered = models.IntegerField()
    household = models.ForeignKey(Household, on_delete=models.CASCADE)

    def __str__(self):
        return self.name + " for " + self.household
    
class Chore(models.Model):
    name = models.CharField(max_length = 128)
    period_type = models.CharField(max_length = 128)
    frequency = models.IntegerField()
    household = models.ForeignKey(Household, on_delete=models.CASCADE)
    next = models.ForeignKey(User, on_delete = models.SET_NULL, null=True)

    def __str__(self):
        return self.name + " for " + self.household

    
class Event(models.Model):
    type = models.CharField(max_length=128)
    description =  models.CharField(max_length=256)
    household = models.ForeignKey(Household, on_delete=models.CASCADE)
    visible = models.ForeignKey(User, on_delete = models.SET_NULL, null=True) #who is the event visible to? null == all
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()
    bill = models.ForeignKey(Bill, on_delete=models.CASCADE, null= True)
    chore = models.ForeignKey(Chore, on_delete=models.CASCADE, null= True)

    def __str__(self):
        return self.description
