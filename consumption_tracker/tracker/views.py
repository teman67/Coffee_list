from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User

@login_required
def profile(request):
    profile, created = Profile.objects.get_or_create(user=request.user)
    consumption, created = Consumption.objects.get_or_create(user=request.user)
    if request.method == 'POST':
        if 'ice_cream' in request.POST:
            consumption.ice_cream += 1
        if 'coffee' in request.POST:
            consumption.coffee += 1
        consumption.update_total_price()
        return redirect('profile')
    return render(request, 'tracker/profile.html', {'profile': profile, 'consumption': consumption})

@login_required
def delete_account(request):
    if request.method == 'POST':
        user = request.user
        user.delete()
        messages.success(request, 'Your account has been deleted.')
        return redirect('home')  # Replace 'home' with your desired redirect page
    return render(request, 'tracker/delete_account.html')
