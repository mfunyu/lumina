from marshmallow import fields, validate

from glados import ma, constants
from glados.models import Entity


class EntitiesRequestSerializer(ma.Schema):
    type = fields.String(required=False, validate=validate.OneOf([x.name for x in constants.EntityType]))
    status = fields.String(required=False, validate=validate.OneOf([x.name for x in constants.EntityStatus]))
    room_id = fields.UUID(required=False, error_messages={"room_id": "Not a valid UUID."})


class EntityCreateSerializer(ma.Schema):
    name = fields.String(required=True, validate=validate.Length(min=1))
    type = fields.String(required=True, validate=validate.OneOf([x.name for x in constants.EntityType]))
    status = fields.String(required=True, validate=validate.OneOf([x.name for x in constants.EntityStatus]))
    value = fields.String(required=False)
    room_id = fields.UUID(required=True, error_messages={"room_id": "Not a valid UUID."})


class EntityUpdateSerializer(ma.Schema):
    name = fields.String(required=False, validate=validate.Length(min=1))
    type = fields.String(required=False, validate=validate.OneOf([x.name for x in constants.EntityType]))
    status = fields.String(required=False, validate=validate.OneOf([x.name for x in constants.EntityStatus]))
    value = fields.String(required=False)
    room_id = fields.UUID(required=False, error_messages={"room_id": "Not a valid UUID."})


class EntitySerializer(ma.Schema):
    created_at = fields.DateTime("%Y-%m-%dT%H:%M:%S")

    class Meta:
        model = Entity
        ordered = True
        fields = [
            "id",
            "name",
            "type",
            "status",
            "value",
            "created_at"
        ]


class EntityResponseSerializer(EntitySerializer):
    pass
