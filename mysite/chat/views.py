# chat/views.py

from django.shortcuts import render
from django.utils.safestring import mark_safe
import json
from django.shortcuts import render

def index(request):
    return render(request, 'lobby.html', {})

def room(request, room_name):
    return render(request, 'room.html', {
        'room_name_json': mark_safe(json.dumps(room_name))
    })
