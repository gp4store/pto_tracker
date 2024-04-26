
from django.urls import path
from . import views

urlpatterns = [
    
    path('', views.home, name = 'home'),
    path('home', views.home, name = "home"),
    path('req', views.req, name = 'req'),
    path('new_req', views.new_req, name = 'new_req'),
    path('list_request', views.list_request, name = 'list_request'),
    path('show_request/<request_id>', views.show_request, name = 'show_request'),
    path('update_request/<request_id>', views.update_request, name = 'update_request'),
    path('delete_request/<request_id>', views.delete_request, name = 'delete_request'),
    
]
