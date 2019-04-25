# chat/views.py

from django.shortcuts import render
from django.utils.safestring import mark_safe
import json
from django.shortcuts import render

def index(request):
    return render(request, 'lobby.html', {})

def room(request):
    return render(request, 'room.html', {})
