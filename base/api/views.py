from rest_framework.decorators import api_view
# from django.http import JsonResponse
from rest_framework.response import Response
from base.models import Room
from .serialarizers import RoomSerializer
from base.api import serialarizers



@api_view(['GET'])
def getRoutes(request):
    routes = [
        'GET /api', 
        'GET /api/rooms',
        'GET /api/rooms/:id'
    ]
    return Response(routes)
    # return JsonResponse(routes, safe=False)



@api_view(['GET'])
def getRooms(request):
    rooms = Room.objects.all()
    serialarizer = RoomSerializer(rooms, many=True)
    return Response(serialarizer.data)



@api_view(['GET'])
def getRoom(request,pk):
    room = Room.objects.get(id=pk)
    serialarizer = RoomSerializer(room, many=False)
    return Response(serialarizer.data)