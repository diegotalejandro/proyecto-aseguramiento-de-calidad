from django.urls import path
from .views import index, home, logout, news, news2, anuncio


urlpatterns = [
    path('', index, name="index"),
    path("home/", home, name="home"),
    path("logout", logout),
    path("news/", news, name="news"),
    path("news2/", news2, name="news2"),
    path("anuncio/", anuncio, name="anuncio"),
]
