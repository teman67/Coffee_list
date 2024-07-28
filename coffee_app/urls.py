# myapp/urls.py
from django.urls import path
from .views import register, login_view, update_consumption, dashboard

urlpatterns = [
    path('register/', register, name='register'),
    path('login/', login_view, name='login'),
    path('update/', update_consumption, name='update_consumption'),
    path('dashboard/', dashboard, name='dashboard'),
]


