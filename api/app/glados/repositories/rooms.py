from glados.models import Room
from glados import db


def get_rooms():
    query = Room.query

    return query


def add_room(data):
    name = data.get("name")
    new_room = Room(name=name)

    try:
        db.session.add(new_room)
        db.session.commit()
    except Exception as e:
        db.session.rollback()
        raise e

    return new_room
