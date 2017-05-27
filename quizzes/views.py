from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from .models import Quizz
from .models import Topic


@login_required
def create(request):
    if request.method == 'POST':
        if request.POST['pregunta'] and request.POST['tema'] and request.POST['respuesta1'] and request.POST['respuesta2'] and request.POST['respuesta3'] and request.POST['respuesta_correcta']:
            quizz = Quizz()
            quizz.pregunta = request.POST['pregunta']

            try:
                tema = Topic.objects.get(tema=request.POST['tema'])
                quizz.tema = request.POST['tema']
            except Topic.DoesNotExist:
                tema_obj = Topic()
                tema_obj.tema = request.POST['tema']
                tema_obj.save()
                quizz.tema = tema_obj

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

@login_required
def allquizzes(request):
    quizzes = Quizz.objects
    return render(request, 'quizzes/allquizzes.html', {'quizzes':quizzes})



