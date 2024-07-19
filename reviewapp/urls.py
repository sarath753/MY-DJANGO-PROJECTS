from django.urls import path
from . import views

urlpatterns = [
    path('movielist/', views.listmovies, name="simpledisplaymovies"),
    path('movielist/<int:id>/', views.detailedmovie, name="detailed"),
    path('movieadd/',views.addmovie,name="addmovie")
]
