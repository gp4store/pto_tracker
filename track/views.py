from django.shortcuts import render
from datetime import datetime
from .models import pto_request


todays_date = datetime.now


def home(request):
    return render(request, "track/home.html", {'date': todays_date})

def req(request):

    request_list = pto_request.objects.all()
    return render(request, "track/request_list.html", {'request_list' : request_list})

def new_req(request):

    return render(request, "track/new_req.html", {'date': todays_date})


    