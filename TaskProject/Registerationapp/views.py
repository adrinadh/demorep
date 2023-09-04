from django.shortcuts import redirect, render
from django.contrib.auth.models import User
from django.contrib import messages, auth
from . models import Place
# Create your views here.


def login(request):
    if request.method == 'POST':
        username = request.POST['Username']
        password = request.POST['Password']

        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)
            return redirect('/')
        else:
            messages.info(request, 'Invalid username or password')
    return render(request, 'login.html')


def register(request):
    if request.method == 'POST':
        username = request.POST['Username']
        password = request.POST['Password']
        first_name = request.POST['First_name']
        last_name = request.POST['Last_name']
        email = request.POST['Email']
        conPassword = request.POST['CPassword']

        if conPassword == password:
            if User.objects.filter(username=username).exists():
                messages.info(request, 'Username already taken')
                return redirect('register')

            elif User.objects.filter(email=email).exists():
                messages.info(request, 'Email already taken')
                return redirect('register')

            else:
                messages.info(request, 'User Createdted')

                user = User.objects.create_user(
                    username=username, password=password, first_name=first_name, last_name=last_name, email=email)
                user.save()
                return redirect('login')

        else:
            print('password not matching')

    return render(request, 'register.html')


def logout(request):
    auth.logout(request)
    return redirect('/')
