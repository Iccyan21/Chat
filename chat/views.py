from django.shortcuts import render, get_object_or_404
from django.utils.safestring import mark_safe
import json
from django.urls import reverse
from django.http import HttpResponseRedirect
from .models import ChatRoom,Message

def index(request):
    return render(request, 'chat/index.html')

def room(request, room_name):
    room = get_object_or_404(ChatRoom, name=room_name)
    messages = Message.objects.filter(room=room).order_by('timestamp')
    if request.method == 'POST':
        message = request.POST.get('message')
        sender = request.POST.get('sender')
        new_message = Message.objects.create(sender=request.user,room=room, context=message)
        return HttpResponseRedirect(reverse('room', args=[room_name]))
    return render(request, 'chat/room.html', {
        'room_name_json': mark_safe(json.dumps(room_name)),
        'messages': messages,
        'chat': room,
    })
