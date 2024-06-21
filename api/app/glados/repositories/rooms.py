from glados.models import Room
from glados import db


def get_rooms():
    query = Room.query

    return query


def add_room(data):
    name = data.get("name")
    new_room = Room(name=name)
    new_room.save()

    return new_room


def update_room(room_id, data):
    room = Room.query.get(room_id)

    name = data.get("name")
    room.name = name
    room.save()

    return room


def delete_room(room_id):
    room = Room.query.get(room_id)
    if not room:
        raise Exception("Room not found")

    db.session.delete(room)
    db.session.commit()
