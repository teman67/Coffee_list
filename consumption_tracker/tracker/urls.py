from django.urls import path
from .views import profile, delete_account


urlpatterns = [
    path('profile/', profile, name='profile'),
    path('delete-account/', delete_account, name='delete_account'),
]
