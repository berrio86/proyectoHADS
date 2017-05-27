from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout

# Create your views here.
def signup(request):
    if request.method == 'POST':
        if request.POST['password1'] == request.POST['password2']:
            try:
                User.objects.get(username=request.POST['username'])
                return render(request, 'accounts/signup.html', {'error': 'El nombre de usuario seleccionado ya está siendo usado por otra persona'})
            except User.DoesNotExist:
                username= request.POST['username']
                if username[0].isupper():
                    user = User.objects.create_user(request.POST['username'], password=request.POST['password1'])
                    login(request, user)
                    return render(request, 'quizzes/home.html', {'ok': '¡Felicidades! Te has registrado con éxito'})
                else:
                    return render(request, 'accounts/signup.html', {'error': 'El nombre de usuario tiene que empezar por mayúscula.'})
        else:
            return render(request, 'accounts/signup.html', {'error':'Las contraseñas deben ser iguales'})
    else:
        return render(request, 'accounts/signup.html')


def loginview(request):
    if request.method == 'POST':
        user = authenticate(request, username=request.POST['username'], password=request.POST['password'])
        if user is not None:
            login(request, user)
            if 'next' in request.POST:
                return redirect(request.POST['next'])
            return render(request, 'quizzes/home.html' , {'ok': 'Te has logeado de forma correcta'})
        else:
            return render(request, 'accounts/login.html', {'error': 'Nombre de usuario o contraseña incorrecta'})
    else:
        return render(request, 'accounts/login.html' )


def logoutview(request):
    if request.method == 'POST':
        logout(request)
        return render(request, 'quizzes/home.html', {'ok': 'Has terminado la sesión de forma correcta'})

