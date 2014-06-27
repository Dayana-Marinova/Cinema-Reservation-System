from django.shortcuts import render
from room.models import Room


def roomAll(request):
    rooms = Room.objects.all()

    return render(request, "roomsall.html", locals())


def informationRoom(request, roomnumber):
    room = Room.objects.get(number=roomnumber)

    return render(request, "singleroom.html", locals())
