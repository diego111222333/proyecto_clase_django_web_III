# inicio/urls.py
from django.urls import path
from . import views
urlpatterns = [
    path('',views.inicio,name="inicio"),
    path('perro',views.perro,name='inicio'),
    path('gato',views.gato,name='gato')
]