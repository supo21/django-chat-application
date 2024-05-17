from django.shortcuts import render
from .models import Room, Message

# Create your views here.
def all_rooms(request):
    rooms = Room.objects.all()
    context = {"rooms": rooms}
    return render(request, "all_rooms.html", context )

def room(request, slug):
    room_name = Room.objects.get(slug = slug).name
    messages = Message.objects.filter(room  = Room.objects.get(slug= slug))

    context = {"room_name": room_name, "slug":slug, "messages":messages}

    return render(request, "room.html", context)

