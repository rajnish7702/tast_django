from django.urls import path
from .views import user_signup, login



urlpatterns = [
    path('signup/',user_signup, name='signup'),
    path('login/',login, name='login'),
    
]