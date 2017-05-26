from django.conf.urls import url
from . import views

app_name = 'quizzes'

urlpatterns = [
    url(r'^create/', views.create, name='create'),
    url(r'^allquizzes/', views.allquizzes, name='allquizzes'),

]