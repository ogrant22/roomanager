from django.urls import path
from app import views
 
app_name = 'rango'

urlpatterns = [
    path('', views.index, name='index'),
]