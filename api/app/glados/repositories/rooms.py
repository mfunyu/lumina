from glados.models import Room
from glados import db


def get_rooms():
    query = Room.query

    return query

def add_room(data):
    new_room = Room(name=data)

    try:
        db.session.add(new_room)
        db.session.commit()
        print(f"Room '{name}' added successfully!")
    except Exception as e:
        db.session.rollback()
        print(f"Error adding room '{data}': {e}")

    return new_room