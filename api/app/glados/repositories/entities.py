from glados.models import Entity


def get_entities(filters):
    query = Entity.query

    type = filters.get("type")
    if type:
        query = query.filter(Entity.type == type)

    status = filters.get("status")
    if status:
        query = query.filter(Entity.status == status)

    room_id = filters.get("room_id")
    if room_id:
        query = query.filter(Entity.room_id == room_id)

    return query
