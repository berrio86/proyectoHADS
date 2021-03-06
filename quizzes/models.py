from django.db import models
from django.contrib.auth.models import User


class Topic(models.Model):
    tema = models.TextField(default="SinTema")

    def __str__(self):
        return self.tema

class Quizz(models.Model):
    pregunta = models.TextField()
    tema = models.ForeignKey(Topic, on_delete=models.CASCADE)
    respuesta1 = models.TextField()
    respuesta2 = models.TextField()
    respuesta3 = models.TextField()
    fecha_pub = models.DateTimeField()
    autor = models.ForeignKey(User)
    respuesta_correcta = models.IntegerField(default=1)

    def fecha_formato(self):
        return self.fecha_pub.strftime('%e / %b / %Y')