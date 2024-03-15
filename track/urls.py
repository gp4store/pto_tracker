
from django.urls import path
from . import views

urlpatterns = [
    
    path('', views.home, name = "home"),
    path('req', views.req, name = 'requests'),

]
