from django.urls import path
from . import views

urlpatterns = [
    path('bloglist/', views.displayblogs, name="simpledisplayblog"),
    path('bloglist/<int:blog>/', views.blogdetaileddisplay, name="blogdisplay"),
    path('bloglistdelete/<int:id>/', views.blogdelete, name="blogdelete"),
    path('bloglistedit/<int:id>/', views.blogedit, name="blogedit"),
    path('blogentry/', views.blogentry, name="blogentry"),
]
