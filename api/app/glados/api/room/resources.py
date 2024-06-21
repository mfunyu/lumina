from flask import request
from flask_restful import Resource

from glados.api.room.serializers import RoomCreateSerializer, RoomResponseSerializer, RoomUpdateSerializer, RoomIdSerializer
from glados.repositories.rooms import get_rooms, add_room, update_room


class RoomsAPI(Resource):
    def get(self):

        rooms = get_rooms()

        serializer = RoomResponseSerializer(many=True)
        return serializer.dump(rooms), 200

    def post(self):
        create_serializer = RoomCreateSerializer()
        data = create_serializer.load(request.form)
        room = add_room(data)

        serializer = RoomResponseSerializer()
        return serializer.dump(room), 200

    def put(self, room_id):
        update_serializer = RoomUpdateSerializer()
        data = update_serializer.load(request.form)
        room = update_room(room_id, data)

        serializer = RoomResponseSerializer()
        return serializer.dump(room), 200
