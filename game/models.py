from django.db import models


class Player(models.Model):
    respuestas_correctas = models.IntegerField(default=0)
    respuestas_incorrectas = models.IntegerField(default=0)
    nick = models.TextField()


    def preguntasTotales(self):
        return self.respuestas_correctas + self.respuestas_incorrectas

    def porcentajeCorrecto(self):
        return round((100 * self.respuestas_correctas)/self.preguntasTotales(), 2)

    def porcentajeIncorrecto(self):
        return round((100 * self.respuestas_incorrectas)/self.preguntasTotales(),2)


