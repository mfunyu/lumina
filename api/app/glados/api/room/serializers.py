from marshmallow import fields, validate, validates

from glados import ma
from glados.models import Room


class RoomCreateSerializer(ma.Schema):
    name = fields.String(required=True, validate=validate.Length(min=1))


class RoomSerializer(ma.Schema):
    created_at = fields.DateTime("%Y-%m-%dT%H:%M:%S")

    class Meta:
        model = Room
        ordered = True
        fields = [
            "id",
            "name",
            "created_at"
        ]


class RoomResponseSerializer(RoomSerializer):
    pass


class RoomUpdateSerializer(ma.Schema):
    name = fields.String(required=True, validate=validate.Length(min=1))


class RoomIdSerializer(ma.Schema):
    id = fields.UUID(required=True, error_messages={"id": "Not a valid UUID."})

    @validates("id")
    def validate_id(self, value):
        Room.query.get_or_404(value, description="Room not found.")
