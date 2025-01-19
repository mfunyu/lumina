import uuid
import pytest

from lumina.models import Room


mimetype = 'application/json'
headers = {
    'Content-Type': mimetype,
    'Accept': mimetype
}


@pytest.fixture
def rooms():
    kitchen = Room(id=uuid.UUID(int=1), name="Kitchen")
    kitchen.save(commit=False)

    living_room = Room(id=uuid.UUID(int=2), name="Living Room")
    living_room.save(commit=False)


def test_get_rooms(client, rooms, mocker):
    response = client.get("/rooms")

    assert response.status_code == 200
    assert response.json == [
        {
            "id": "00000000-0000-0000-0000-000000000001",
            "name": "Kitchen",
            "created_at": mocker.ANY
        },
        {
            "id": "00000000-0000-0000-0000-000000000002",
            "name": "Living Room",
            "created_at": mocker.ANY
        }
    ]


def test_post_room(client, mocker):
    response = client.post("/rooms", headers=headers, json={"name": "Bedroom"})

    assert response.status_code == 200
    assert response.json == {
        "id": mocker.ANY,
        "name": "Bedroom",
        "created_at": mocker.ANY
    }


def test_post_room_empty(client):
    response = client.post("/rooms", headers=headers, json={"name": ""})

    assert response.status_code == 422
    assert response.json == {"errors": {
        "name": ["Shorter than minimum length 1."],
    }}


def test_post_room_missing_name(client, rooms):
    response = client.post("/rooms", headers=headers, json={})

    assert response.status_code == 422
    assert response.json == {"errors": {
        "name": ["Missing data for required field."]
    }}


def test_put_room(client, rooms, mocker):
    response = client.put("/rooms/00000000-0000-0000-0000-000000000001", headers=headers, json={"name": "Kitchen 2"})

    assert response.status_code == 200
    assert response.json == {
        "id": "00000000-0000-0000-0000-000000000001",
        "name": "Kitchen 2",
        "created_at": mocker.ANY
    }


def test_put_room_empty(client, rooms):
    response = client.put("/rooms/00000000-0000-0000-0000-000000000001", headers=headers, json={"name": ""})

    assert response.status_code == 422
    assert response.json == {"errors": {
        "name": ["Shorter than minimum length 1."],
    }}


def test_put_room_missing_name(client, rooms):
    response = client.put("/rooms", headers=headers, json={})

    assert response.status_code == 400
    assert response.json == {"error": "Room ID is required"}


def test_put_room_not_found(client, rooms):
    response = client.put("/rooms/00000000-0000-0000-0000-000000000012", headers=headers, json={"name": "Bedroom"})

    assert response.status_code == 404
    assert response.json == {"message": "Room not found."}


def test_delete_room(client, rooms):
    response = client.delete("/rooms/00000000-0000-0000-0000-000000000001")

    assert response.status_code == 204
    assert response.data == b""
    assert Room.query.get(uuid.UUID(int=1)) is None


def test_delete_room_not_found(client):
    response = client.delete("/rooms/00000000-0000-0000-0000-000000000012")

    assert response.status_code == 404
    assert response.json == {"message": "Room not found."}
