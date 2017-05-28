from django.conf.urls import url
from django.conf.urls.static import static
from django.conf import settings

from . import views

app_name = 'accounts'

urlpatterns = [
    url(r'^signup/', views.signup, name='signup'),
    url(r'^login/', views.loginview, name='login'),
    url(r'^logout/', views.logoutview, name='logout'),
] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)