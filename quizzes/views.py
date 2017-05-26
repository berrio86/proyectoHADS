from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from django.contrib.auth.models import User
from .models import Quizz


@login_required
def create(request):
    if request.method == 'POST':
        if request.POST['pregunta'] and request.POST['respuesta1'] and request.POST['respuesta2'] and request.POST['respuesta3'] and request.POST['respuesta_correcta']:
            quizz = Quizz()
            quizz.pregunta = request.POST['pregunta']
            quizz.tema = request.POST['tema']
            quizz.respuesta1 = request.POST['respuesta1']
            quizz.respuesta2 = request.POST['respuesta2']
            quizz.respuesta3 = request.POST['respuesta3']
            quizz.autor = request.user
            quizz.respuesta_correcta = request.POST['respuesta_correcta']
            quizz.fecha_pub = timezone.datetime.now()
            quizz.save()
            return render(request, 'quizzes/create.html', {'ok': 'La pregunta ha sido introducida en la BD'})
        else:
            return render(request, 'quizzes/create.html', {'error': 'ERROR: Rellene los campos correctamente'})
    else:
        return render(request, 'quizzes/create.html')



def home(request):
    return render(request, 'quizzes/home.html')

def allquizzes(request):
    quizzes = Quizz.objects
    return render(request, 'quizzes/allquizzes.html', {'quizzes':quizzes})





