# myapp/views.py
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from .models import Item, Consumption
from .forms import ConsumptionForm

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect('dashboard')
    else:
        form = UserCreationForm()
    return render(request, 'coffee_app/register.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        # handle login
        pass
    return render(request, 'coffee_app/login.html')

def update_consumption(request):
    if request.method == 'POST':
        form = ConsumptionForm(request.POST, user=request.user)
        if form.is_valid():
            form.save()
            return redirect('dashboard')
    else:
        form = ConsumptionForm(user=request.user)
    return render(request, 'coffee_app/update_consumption.html', {'form': form})

def dashboard(request):
    consumptions = Consumption.objects.filter(user=request.user)
    total_price = sum([c.total_price() for c in consumptions])
    return render(request, 'coffee_app/dashboard.html', {'consumptions': consumptions, 'total_price': total_price})
