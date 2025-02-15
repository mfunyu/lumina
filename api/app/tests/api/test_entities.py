import uuid
import pytest

from lumina import constants
from lumina.models import Entity, Room

mimetype = 'application/json'
headers = {
    'Content-Type': mimetype,
    'Accept': mimetype
}


@pytest.fixture
def entities():
    kitchen = Room(id=uuid.UUID(int=1), name="Kitchen")
    kitchen.save(commit=False)

    living_room = Room(id=uuid.UUID(int=2), name="Living Room")
    living_room.save(commit=False)

    entity = Entity(
        id=uuid.UUID(int=1),
        name="Ceiling Light",
        type=constants.EntityType.light.name,
        status=constants.EntityStatus.off.name,
        value=None,
        room_id=kitchen.id)
    entity.save(commit=False)

    entity = Entity(
        id=uuid.UUID(int=2),
        name="Lamp",
        type=constants.EntityType.light.name,
        status=constants.EntityStatus.on.name,
        value=200,
        room_id=living_room.id)
    entity.save(commit=False)

    entity = Entity(
        id=uuid.UUID(int=3),
        name="Thermometer",
        type=constants.EntityType.sensor.name,
        status=constants.EntityStatus.on.name,
        value=28,
        room_id=living_room.id)
    entity.save(commit=False)


def test_get_entities(client, entities, mocker):
    response = client.get("/entities")

    assert response.status_code == 200
    assert response.json == [
        {
            "id": "00000000-0000-0000-0000-000000000001",
            "name": "Ceiling Light",
            "type": "light",
            "status": "off",
            "value": None,
            "created_at": mocker.ANY
        },
        {
            "id": "00000000-0000-0000-0000-000000000002",
            "name": "Lamp",
            "type": "light",
            "status": "on",
            "value": "200",
            "created_at": mocker.ANY
        },
        {
            "id": "00000000-0000-0000-0000-000000000003",
            "name": "Thermometer",
            "type": "sensor",
            "status": "on",
            "value": "28",
            "created_at": mocker.ANY
        }
    ]


def test_get_entities_with_invalid_type_filter(client):
    response = client.get("/entities?type=invalid")

    assert response.status_code == 422
    assert response.json == {"errors": {
        "type": ["Must be one of: sensor, light, switch, multimedia, air_conditioner."]
    }}


def test_get_entities_with_type_filter(client, entities, mocker):
    response = client.get("/entities?type=sensor")

    assert response.status_code == 200
    assert response.json == [
        {
            "id": "00000000-0000-0000-0000-000000000003",
            "name": "Thermometer",
            "type": "sensor",
            "status": "on",
            "value": "28",
            "created_at": mocker.ANY
        }
    ]


def test_get_entities_with_invalid_status_filter(client):
    response = client.get("/entities?status=invalid")

    assert response.status_code == 422
    assert response.json == {"errors": {
        "status": ["Must be one of: on, off, unavailable."]
    }}


def test_get_entities_with_status_filter(client, entities, mocker):
    response = client.get("/entities?status=on")

    assert response.status_code == 200
    assert response.json == [
        {
            "id": "00000000-0000-0000-0000-000000000002",
            "name": "Lamp",
            "type": "light",
            "status": "on",
            "value": "200",
            "created_at": mocker.ANY
        },
        {
            "id": "00000000-0000-0000-0000-000000000003",
            "name": "Thermometer",
            "type": "sensor",
            "status": "on",
            "value": "28",
            "created_at": mocker.ANY
        }
    ]


def test_get_entities_with_type_and_status_filter(client, entities, mocker):
    response = client.get("/entities?type=light&status=on")

    assert response.status_code == 200
    assert response.json == [
        {
            "id": "00000000-0000-0000-0000-000000000002",
            "name": "Lamp",
            "type": "light",
            "status": "on",
            "value": "200",
            "created_at": mocker.ANY
        }
    ]


def test_get_entities_with_invalid_room_filter(client):
    response = client.get("/entities?room_id=invalid")

    assert response.status_code == 422
    assert response.json == {"errors": {
        "room_id": ["Not a valid UUID."]
    }}


def test_get_entities_with_room_filter(client, entities, mocker):
    response = client.get("/entities?room_id=00000000-0000-0000-0000-000000000002")

    assert response.status_code == 200
    assert response.json == [
        {
            "id": "00000000-0000-0000-0000-000000000002",
            "name": "Lamp",
            "type": "light",
            "status": "on",
            "value": "200",
            "created_at": mocker.ANY
        },
        {
            "id": "00000000-0000-0000-0000-000000000003",
            "name": "Thermometer",
            "type": "sensor",
            "status": "on",
            "value": "28",
            "created_at": mocker.ANY
        }
    ]


def test_post_entity(client, entities, mocker):
    data = {
        "name": "Air Conditioner",
        "type": "air_conditioner",
        "status": "on",
        "value": "22",
        "room_id": "00000000-0000-0000-0000-000000000002"
    }
    response = client.post("/entities", json=data, headers=headers)

    assert response.status_code == 200
    assert response.json == {
        "id": mocker.ANY,
        "name": "Air Conditioner",
        "type": "air_conditioner",
        "status": "on",
        "value": "22",
        "created_at": mocker.ANY
    }


def test_post_entity_empty(client):
    response = client.post("/entities", headers=headers, json={
        "name": "",
        "type": "",
        "status": "",
        "value": "",
        "room_id": ""
    })

    assert response.status_code == 422
    assert response.json == {"errors": {
        "name": ["Shorter than minimum length 1."],
        "room_id": ["Not a valid UUID."],
        "type": ["Must be one of: sensor, light, switch, multimedia, air_conditioner."],
        "status": ["Must be one of: on, off, unavailable."],
    }}


def test_post_entity_missing_name(client, entities):
    response = client.post("/entities", headers=headers, json={
        "type": "light",
        "status": "on",
        "value": "200",
        "room_id": "00000000-0000-0000-0000-000000000002"
    })

    assert response.status_code == 422
    assert response.json == {"errors": {
        "name": ["Missing data for required field."]
    }}


def test_put_entity(client, entities, mocker):
    response = client.put("/entities/00000000-0000-0000-0000-000000000001", headers=headers, json={
        "name": "Ceiling Light 2",
        "type": "light",
        "status": "on",
        "value": "100",
        "room_id": "00000000-0000-0000-0000-000000000001"
    })

    assert response.status_code == 200
    assert response.json == {
        "id": "00000000-0000-0000-0000-000000000001",
        "name": "Ceiling Light 2",
        "type": "light",
        "status": "on",
        "value": "100",
        "created_at": mocker.ANY
    }


def test_put_entity_name(client, entities, mocker):
    response = client.put("/entities/00000000-0000-0000-0000-000000000002", headers=headers, json={
        "name": "Lamp 2"
    })

    assert response.status_code == 200
    assert response.json == {
        "id": "00000000-0000-0000-0000-000000000002",
        "name": "Lamp 2",
        "type": "light",
        "status": "on",
        "value": "200",
        "created_at": mocker.ANY
    }


def test_put_entity_status(client, entities, mocker):
    response = client.put("/entities/00000000-0000-0000-0000-000000000003", headers=headers, json={
        "status": "off"
    })

    assert response.status_code == 200
    assert response.json == {
        "id": "00000000-0000-0000-0000-000000000003",
        "name": "Thermometer",
        "type": "sensor",
        "status": "off",
        "value": "28",
        "created_at": mocker.ANY
    }


def test_put_entity_room_id(client, entities, mocker):
    response = client.put("/entities/00000000-0000-0000-0000-000000000003", headers=headers, json={
        "room_id": "00000000-0000-0000-0000-000000000001"
    })

    assert response.status_code == 200
    assert response.json == {
        "id": "00000000-0000-0000-0000-000000000003",
        "name": "Thermometer",
        "type": "sensor",
        "status": "on",
        "value": "28",
        "created_at": mocker.ANY
    }


def test_put_entity_empty(client, entities):
    response = client.put("/entities/00000000-0000-0000-0000-000000000001", headers=headers, json={
        "name": "",
        "type": "",
        "status": "",
        "room_id": ""
    })

    assert response.status_code == 422
    assert response.json == {"errors": {
        "name": ["Shorter than minimum length 1."],
        "room_id": ["Not a valid UUID."],
        "type": ["Must be one of: sensor, light, switch, multimedia, air_conditioner."],
        "status": ["Must be one of: on, off, unavailable."],
    }}


def test_put_entity_id_not_found(client):
    response = client.put("/entities/00000000-0000-0000-0000-000000000001", headers=headers, json={
        "name": "Invalid"
    })

    assert response.status_code == 404
    assert response.json == {"message": "Entity not found."}


def test_put_entity_invalid_id(client):
    response = client.put("/entities/invalid", headers=headers, json={
        "name": "Invalid"
    })

    assert response.status_code == 404
    assert response.json == {
        "error": "not_found",
        "message": "Resource not found."
    }


def test_put_entity_invalid_room_id(client, entities):
    response = client.put("/entities/00000000-0000-0000-0000-000000000001", headers=headers, json={
        "room_id": "00000000-0000-0000-0000-000000000012"
    })

    assert response.status_code == 422
    assert response.json == {"errors": {
        "room_id": ["Room not found."]
    }}


def test_put_entity_missing_name(client, entities):
    response = client.put("/entities", headers=headers, json={
        "type": "light",
        "status": "on",
        "value": "100",
        "room_id": "00000000-0000-0000-0000-000000000001"
    })

    assert response.status_code == 400
    assert response.json == {"error": "Entity ID is required"}


def test_delete_entity(client, entities):
    response = client.delete("/entities/00000000-0000-0000-0000-000000000001")

    assert response.status_code == 204
    assert response.data == b""
    assert Entity.query.get(uuid.UUID(int=1)) is None


def test_delete_entity_not_found(client):
    response = client.delete("/entities/00000000-0000-0000-0000-000000000001")

    assert response.status_code == 404
    assert response.json == {"message": "Entity not found."}
