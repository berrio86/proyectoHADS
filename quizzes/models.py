from django.db import models
from django.contrib.auth.models import User


class Quizz(models.Model):
    pregunta = models.TextField()
    tema = models.TextField(default="Sin tema")
    respuesta1 = models.TextField()
    respuesta2 = models.TextField()
    respuesta3 = models.TextField()
    fecha_pub = models.DateTimeField()
    autor = models.ForeignKey(User)
    respuesta_correcta = models.IntegerField(default=1)

    def fecha_formato(self):
        return self.fecha_pub.strftime('%e / %b / %Y')