from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from .models import Routine
from django.urls import reverse
from django.contrib import messages
from django.contrib.messages import constants

# Create your views here.
def create_insulin_routine(request):
    if request.method == 'GET':
        return render(request, 'routine.html')
    
    elif request.method == 'POST':
        name = request.POST.get('username')
        peso = request.POST.get('peso')
        old = request.POST.get('old')
        disease = request.POST.get('disease')
       
        routine = Routine(
            name = name,
            peso = peso,
            old = old,
            disease = disease,   
        )

        routine.save()

        messages.add_message(request, constants.SUCCESS, 'Rotina cadastrado com sucesso')
        return redirect('/insulin_routine/new_routine/')
        # return redirect(reverse('insulin_routine'))