from django.db import models


class Player(models.Model):
    respuestas_correctas = models.IntegerField(default=0)
    respuestas_incorrectas = models.IntegerField(default=0)
    nick = models.TextField()


    def preguntasTotales(self):
        return self.respuestas_correctas + self.respuestas_incorrectas