from flask import request
from flask_restful import Resource

from glados.api.room.serializers import RoomCreateSerializer, RoomResponseSerializer, RoomUpdateSerializer, RoomIdSerializer
from glados.repositories.rooms import get_rooms, add_room, update_room, delete_room


class RoomsAPI(Resource):
    def get(self):

        rooms = get_rooms()

        serializer = RoomResponseSerializer(many=True)
        return serializer.dump(rooms), 200

    def post(self):
        create_serializer = RoomCreateSerializer()
        data = create_serializer.load(request.json)
        room = add_room(data)

        serializer = RoomResponseSerializer()
        return serializer.dump(room), 200

    def put(self, room_id=None):
        if not room_id:
            return {"error": "Room ID is required"}, 400
        id_serializer = RoomIdSerializer()
        room_id = id_serializer.load({"id": room_id})

        update_serializer = RoomUpdateSerializer()
        data = update_serializer.load(request.json)
        room = update_room(room_id, data)

        serializer = RoomResponseSerializer()
        return serializer.dump(room), 200

    def delete(self, room_id):
        id_serializer = RoomIdSerializer()
        room_id = id_serializer.load({"id": room_id})

        delete_room(room_id)

        return {}, 204
