from django.shortcuts import render, HttpResponseRedirect, reverse, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required

def register(request):
    if request.user.is_authenticated:
        return redirect('index')
    form = UserCreationForm()

    if request.method == 'POST':
        form = UserCreationForm(data=request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('login'))
    
    return render(request, 'users/register.html', {
        'form':form
    })

def login_user(request):
    if request.user.is_authenticated:
        return redirect('index')

    form = AuthenticationForm()

    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return HttpResponseRedirect(reverse('index'))

    return render(request, 'users/login.html', {
        'form':form
    })

@login_required
def logout_user(request):
    logout(request)
    return redirect('index')

