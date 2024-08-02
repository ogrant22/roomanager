from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    context_dict = {'boldmessage': 'Context dict message'}
    return render(request, 'app/index.html', context=context_dict)

