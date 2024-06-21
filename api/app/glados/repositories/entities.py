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


def add_entity(data):
    name = data.get("name")
    type = data.get("type")
    status = data.get("status")
    value = data.get("value")
    room_id = data.get("room_id")

    new_entity = Entity(
        name=name,
        type=type,
        status=status,
        value=value,
        room_id=room_id)
    new_entity.save()

    return new_entity


def update_entity(entity_id, data):
    entity = Entity.query.get(entity_id)
    if not entity:
        raise Exception("Entity not found")

    name = data.get("name")
    if name:
        entity.name = name

    type = data.get("type")
    if type:
        entity.type = type

    status = data.get("status")
    if status:
        entity.status = status

    value = data.get("value")
    if value:
        entity.value = value

    room_id = data.get("room_id")
    if room_id:
        entity.room_id = room_id

    entity.save()

    return entity
