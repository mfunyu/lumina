from glados.models import Room


def get_rooms():
    query = Room.query

    return query


def add_room(data):
    name = data.get("name")
    new_room = Room(name=name)
    new_room.save()

    return new_room
