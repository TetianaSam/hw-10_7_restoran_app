from django.urls import path, re_path
from . import views

urlpatterns = [
    path('', views.home_page, name='home'),
    path('restorans', views.restorans_list, name='restorans'),

]