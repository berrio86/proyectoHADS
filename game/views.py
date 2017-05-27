from django.shortcuts import render, redirect
from .models import Player
from quizzes.models import Quizz

def insertnick(request):
    return render(request, 'game/insertnick.html')

def userdata(request):
    if request.method == 'POST':
        if request.POST['nick']:
            # intentar recuperar todos los temas diferentes de los modelos Quizz y pasarlos como set
            try:
                player = Player.objects.get(nick=request.POST['nick'])
                return render(request, 'game/userdata.html', {'ok': 'Tu usuario ha sido cargado de forma correcta.', 'player': player})
            except Player.DoesNotExist:
                nick= request.POST['nick']
                player=Player()
                player.nick = nick
                player.respuestas_incorrectas = 0
                player.respuestas_correctas = 0
                player.save()
                return render(request, 'game/userdata.html', {'ok': 'Se ha creado un nuevo usuario con el nick proporcionado' , 'player': player})

            return render(request, 'game/userdata.html')
        else:
            return render(request, 'game/insertnick.html', {'error':'ERROR: Debe introducir un nick'})
    else:
        return render(request, 'game/insertnick.html')

def play(request):
    if request.method == 'POST':
        tema = request.POST['tema']
        nick = request.POST['nick']
        if tema == 'Todas':
            quizzes = Quizz.objects.all()
        else:
            quizzes = Quizz.objects.filter(tema=tema)
        return render(request, 'game/play.html', {'quizzes': quizzes, 'tema': tema, 'nick': nick })
    else:
        return render(request, 'game/insertnick.html')


def results(request):
    if request.method == 'POST':
        acertadas = 0
        falladas = 0
        tema = request.POST['tema']
        player = Player.objects.get(nick=request.POST['nick'])

        if tema == 'Todas':
            quizzes = Quizz.objects.all()
        else:
            quizzes = Quizz.objects.filter(tema=tema)

        total = len(quizzes)

        for quizz in quizzes:
            ru = request.POST[quizz.pregunta]
            rc = quizz.respuesta_correcta
            ru = int(ru)
            if rc == ru:
                acertadas = acertadas + 1
            else:
                falladas = falladas + 1

        player.respuestas_correctas = player.respuestas_correctas + acertadas
        player.respuestas_incorrectas = player.respuestas_incorrectas + falladas
        player.save()

        return render(request, 'game/results.html', {'total': total, 'player': player, 'falladas': falladas, 'acertadas':acertadas})
    else:
        return render(request, 'game/insertnick.html')