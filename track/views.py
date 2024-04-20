from django.shortcuts import render, redirect
from datetime import datetime
from .models import pto_request
from .forms import pto_requestForm
from django.http import HttpResponseRedirect

todays_date = datetime.now


def home(request):
    return render(request, "track/home.html", {'date': todays_date})

def req(request):

    request_list = pto_request.objects.all()
    return render(request, "track/request_list.html", {'request_list' : request_list})

def new_req(request):

    if request.method != 'POST':
        form = pto_requestForm()
    else:
        form = pto_requestForm(data=request.POST)
        if form.is_valid():
            form.save()
            # return redirect('track:new_req')
            return HttpResponseRedirect('/req')

        
    context = {'form': form}
    return render(request, "track/new_req.html", context)

    # request_sent = False
    # if request.method == 'POST':
    #     form = pto_requestForm(request.POST)
    #     if form.is_valid():
    #         form.save()
    #         return HttpResponseRedirect('/new_req?request_sent=True')
    #     else:
    #         form = pto_requestForm
    #         if 'request_sent' in request.GET:
    #             request_sent = True
    # return render(request, "track/new_req.html", {'form': form, 'request_sent': request_sent })

def list_request(request):

    request_list = pto_request.objects.all()
    return render(request, "track/list_request.html", {'request_list': request_list})

def show_request(request, request_id):

    submit_req = pto_request.objects.get(pk = request_id)
    return render(request, "track/show_request.html", {'submit_req': submit_req})






    