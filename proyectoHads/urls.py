from django.conf.urls import url, include
from django.contrib import admin

from quizzes import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^accounts/', include('accounts.urls')),
    url(r'^quizzes/', include('quizzes.urls')),
    url(r'^game/', include('game.urls')),
    url(r'^$', views.home, name='home'),
]
