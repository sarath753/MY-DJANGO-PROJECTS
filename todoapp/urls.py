from django.urls import path
from . import views

urlpatterns = [
    path('todolist/', views.displaytodos, name="simpledisplay"),
    path('todolist/<int:todo>/', views.tododetaileddisplay, name="tododisplay"),
    path('todolistdelete/<int:id>/', views.tododelete, name="tododelete"),
    path('todolistedit/<int:id>/', views.todoedit, name="todoedit"),
    path('todoentry/', views.todoentry, name="todoentry"),
]
