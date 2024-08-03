from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout 
from django.http import HttpResponse
from django.urls import reverse
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from app.models import UserProfile, Resident
from app.forms import UserForm,UserProfileForm

# Create your views here.
def index(request):
    context_dict = {'boldmessage': 'Context dict message'}
    return render(request, 'app/index.html', context=context_dict)

def loginView(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username, password=password)

        if user:
            profile = UserProfile.objects.filter(user = user)[0]
            if user.is_active:
                login(request, user)
                return redirect(reverse('app:homepage', kwargs= {'user_slug' : profile.slug}))
            else:
                return HttpResponse("Your Rango account is disabled.")
        
        else:
            print(f"Invalid login details: {username}, {password}")
            context_dict = {'message': 'Incorrect details'}
            return render(request, 'app/login.html', context= context_dict)
            
    else:
        context_dict = {'message': ''}
        return render(request, 'app/login.html', context=context_dict)

def register(request):
    registered = False
    if request.method == 'POST':
        user_form =UserForm(request.POST)
        profile_form=UserProfileForm(request.POST)

        if user_form.is_valid() and profile_form.is_valid():
            user =user_form.save()
            user.set_password(user.password)
            user.save()

            profile =profile_form.save(commit=False)
            profile.user =user

            if 'picture' in request.FILES:
                profile.picture =request.FILES['picture']

            profile.save()
            registered = True
        
        else:
            print(user_form.errors,profile_form.errors)
    
    else:
        user_form =UserForm()
        profile_form=UserProfileForm()

    return render(request, 'app/register.html', context={'user_form': user_form, 'profile_form':profile_form, 'registered':registered})

@login_required
def homepage(request, user_slug):
    currentProfile = UserProfile.objects.filter(slug = user_slug)[0]
    currentUser = currentProfile.user
    residents = Resident.objects.filter(user = currentUser)
    households = []
    for r in residents:
        households.append(r.household)
    context_dict = {'profile': currentProfile,
                    'user': currentUser,
                    'households' : households}
    return render(request, 'app/homepage.html', context=context_dict)

@login_required
def user_logout(request):
    logout(request)
    return redirect(reverse('app:login'))


