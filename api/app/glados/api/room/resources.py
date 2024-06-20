from flask import request
from flask_restful import Resource

from glados.api.room.serializers import RoomCreateSerializer, RoomResponseSerializer
from glados.repositories.rooms import get_rooms, add_room


class RoomsAPI(Resource):
    def get(self):

        rooms = get_rooms()

        serializer = RoomResponseSerializer(many=True)
        return serializer.dump(rooms), 200

    def post(self):
        request_serializer = RoomCreateSerializer()
        data = request_serializer.load(request.form)
        room = add_room(data)

        serializer = RoomResponseSerializer()
        return serializer.dump(room), 200
