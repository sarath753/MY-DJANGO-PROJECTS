from django.urls import path, re_path
from . import views

urlpatterns = [
    path('enquiry/', views.saveform, name='enquiryform'),
    path('enquirylist/', views.displayform, name='displayform'),
    re_path(r'^enquiry/(?P<id>\d+)/$', views.editenquiry, name='editform'),
    re_path(r'^deleteenquiry/(?P<id>\d+)/$', views.deleteenquiry, name='deleteenquiry'),
]
