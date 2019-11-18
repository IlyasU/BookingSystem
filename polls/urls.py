from django.conf.urls import url, include
from polls.views import MyRegisterFormView
from . import views

from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
     url(r'^$', views.index, name='index'),
     url(r'^registration/$', views.register, name='register'),
     url(r'^signUp.html/$', views.register, name='registration'),

] + static(settings.STATIC_URL, document_root = settings.STATIC_ROOT)