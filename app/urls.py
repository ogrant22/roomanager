from django.urls import path
from app import views
 
app_name = 'app'

urlpatterns = [
    path('login/', views.loginView, name='login'),
    path('homepage/<slug:user_slug>/', views.homepage, name='homepage'),
    path('register/', views.register, name = 'register'),
    path('logout/', views.user_logout, name='logout'),
    path('', views.user_logout, name='default')
]