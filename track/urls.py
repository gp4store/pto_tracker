
from django.urls import path
from . import views

urlpatterns = [
    
    path('', views.home, name = 'home'),
    path('home', views.home, name = "home"),
    path('req', views.req, name = 'req'),
    path('new_req', views.new_req, name = 'new_req'),
    

]
