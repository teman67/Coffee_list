# myapp/urls.py
from django.urls import path
from .views import register, login_view, update_consumption, dashboard

urlpatterns = [
    path('register/', register, name='register'),
    path('login/', login_view, name='login'),
    path('update/', update_consumption, name='update_consumption'),
    path('dashboard/', dashboard, name='dashboard'),
]

# myproject/urls.py
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('myapp/', include('myapp.urls')),
]
