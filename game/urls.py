from django.conf.urls import url
from . import views

app_name = 'game'

urlpatterns = [
    url(r'^insertnick/', views.insertnick, name='insertnick'),
    url(r'^userdata/', views.userdata, name='userdata'),
    url(r'^play/', views.play, name='play'),
    url(r'^results/', views.results, name='results'),
]