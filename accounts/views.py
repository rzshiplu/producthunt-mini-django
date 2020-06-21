from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import auth


def signup(request):
    if request.method == 'POST':
        username = request.POST['username'].strip()
        password1 = request.POST['password1'].strip()
        password2 = request.POST['password2'].strip()
        context = {
            'username': username,
        }

        if username == '' or password1 == '' or password2 == '':
            context['error'] = 'Please Fillup username and both passwords.'
            return render(request, 'accounts/signup.html', context)
        elif password1 != password2:
            context['error'] = 'passwords do not match.'
            return render(request, 'accounts/signup.html', context)
        try:
            user = User.objects.get(username=username)
        except User.DoesNotExist:
            user = User.objects.create_user(username=username, password=password1)
            auth.login(request, user)
            return redirect('home')
        else:
            context['error'] = 'username has already been taken.'
            return render(request, 'accounts/signup.html', context)
    else:
        return render(request, 'accounts/signup.html')


def login(request):
    if request.method == 'POST':
        username = request.POST['username'].strip()
        password = request.POST['password'].strip()
        next_url = request.POST['next_url'].strip()
        context = {
            'username': username,
            'next_url': next_url,
        }

        if username == '' or password == '':
            context['error'] = 'Please Fillup both username and password.'
            return render(request, 'accounts/login.html', context)

        user = auth.authenticate(request, username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect(next_url)
        else:
            context['error'] = 'Invalid username or password.'
            return render(request, 'accounts/login.html', context)
    else:
        return render(request, 'accounts/login.html', {'next_url': request.GET.get('next', 'home')})


def logout(request):
    if request.method == 'POST':
        auth.logout(request)
        return redirect('home')

