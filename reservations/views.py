# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse
from .models import Reservation
from IPython import embed

# Create your views here.
def index(request):
    if (request.method == 'POST'):
        guest_name = request.POST['guest_name']
        entry_date = request.POST['entry_date']
        leave_date = request.POST['leave_date']
        group_size = request.POST['group_size']

        reservation1 = Reservation(guest_name=guest_name, entry_date=entry_date, leave_date=leave_date, group_size=group_size)
        reservation1.save()

        return render(request, 'index.html')

    else:
        return render(request, 'index.html')

def form(request):
    if (request.method == 'POST'):
        guest_name = request.POST['guest_name']
        entry_date = request.POST['entry_date']
        leave_date = request.POST['leave_date']
        group_size = request.POST['group_size']

        reservation1 = Reservation(guest_name=guest_name, entry_date=entry_date, leave_date=leave_date, group_size=group_size)
        #reservation1.save()
        print (reservation1.entry_date)
        #print (reservation1.entry_date +1)
        return render(request, 'form.html')

    else:
        return render(request, 'form.html')
