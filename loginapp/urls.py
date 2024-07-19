from django.urls import path
from . import views


urlpatterns = [
    path('main/',views.loginfunc,name="login"),
    path('home/',views.home,name="home")
]