from django.urls import path
from app import views
 
app_name = 'app'

urlpatterns = [
    path('', views.loginView, name='login'),
    path('homepage/<slug:user_slug>/', views.homepage, name='homepage'),
    path('register/', views.register, name = 'register'),
]