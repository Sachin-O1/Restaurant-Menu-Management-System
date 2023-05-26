from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.Menulist.as_view(), name='home')
]
