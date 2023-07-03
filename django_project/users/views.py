from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import UserRegisterForm, UserUpdateForm, ProfileUpdateForm


def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save() # save the user
            username = form.cleaned_data.get('username') # get the username from the form
            messages.success(request, f'Your account has been created! You are now able to log in') # flash message
            return redirect('login') # redirect to login page
    else:
        form = UserRegisterForm()
    return render(request, 'users/register.html', {'form': form})


@login_required # decorator to prevent access to profile page without logging in
def profile(request):
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.profile)
        if u_form.is_valid() and p_form.is_valid(): # check if the forms are valid
            u_form.save() # save the user
            p_form.save() # save the profile
            messages.success(request, f'Your account has been updated!') # flash message
            return redirect('profile') # redirect to profile page
    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)

    context = {
        'u_form': u_form,
        'p_form': p_form
    }

    return render(request, 'users/profile.html', context)
