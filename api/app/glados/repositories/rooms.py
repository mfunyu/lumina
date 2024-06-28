from glados.models import Room
from sqlalchemy import asc


def get_rooms():
    query = Room.query

    return query.order_by(asc(Room.created_at))


def add_room(data):
    name = data.get("name")
    new_room = Room(name=name)
    new_room.save(commit=True)

    return new_room


def update_room(room_id, data):
    room = Room.query.get(room_id)

    name = data.get("name")
    room.name = name
    room.save(commit=True)

    return room


def delete_room(room_id):
    room = Room.query.get(room_id)
    if not room:
        raise Exception("Room not found")

    room.remove(commit=True)
