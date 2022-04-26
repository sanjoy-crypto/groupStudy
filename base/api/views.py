from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import RoomSerializer
from base.models import Room


@api_view(['GET'])
def getRoutes(request):

    routes = [
        'GEt /api',
        'GET /api/rooms',
        'GET /api/rooms/:id',
    ]

    return Response(routes)


@api_view(['GET'])
def getRooms(request):
    rooms = Room.objects.all()
    serializers = RoomSerializer(rooms, many=True)
    return Response(serializers.data)


@api_view(['GET'])
def getRoom(request, pk):
    room = Room.objects.get(id=pk)
    serializers = RoomSerializer(room, many=False)
    return Response(serializers.data)
