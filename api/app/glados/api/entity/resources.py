from flask import request
from flask_restful import Resource

from glados.api.entity.serializers import EntitiesRequestSerializer, EntityResponseSerializer, EntityCreateSerializer, EntityUpdateSerializer, EntityIdSerializer
from glados.repositories.entities import get_entities, add_entity, update_entity


class EntitiesAPI(Resource):
    def get(self):
        request_serializer = EntitiesRequestSerializer()
        data = request_serializer.load(request.args)

        entities = get_entities(data)

        serializer = EntityResponseSerializer(many=True)
        return serializer.dump(entities), 200

    def post(self):
        create_serializer = EntityCreateSerializer()
        data = create_serializer.load(request.form)

        entity = add_entity(data)

        serializer = EntityResponseSerializer()
        return serializer.dump(entity), 200

    def put(self, entity_id):
        id_serializer = EntityIdSerializer()
        entity_id = id_serializer.load({"id": entity_id})

        update_serializer = EntityUpdateSerializer()
        data = update_serializer.load(request.form)

        entity = update_entity(entity_id, data)

        serializer = EntityResponseSerializer()
        return serializer.dump(entity), 200
