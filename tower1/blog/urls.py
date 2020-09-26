from django.urls import path
from .views import index, home, logout


urlpatterns = [
    path('', index, name="index"),
    path("home/", home, name="home"),
    path("logout", logout),
]
