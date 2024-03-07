from django.shortcuts import render
from datetime import datetime


todays_date = datetime.now


def home(request):
    return render(request, "home.html", {'date': todays_date})