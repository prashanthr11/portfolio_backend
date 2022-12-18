from . import views
from django.urls import path


urlpatterns = [
    path('', views.welcome, name='welcome'),
    path('ref/', views.tst, name='tst'),
    path('home/', views.tst, name='tst'),
]