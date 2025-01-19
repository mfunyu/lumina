from flask import request
from flask_restful import Resource

from lumina.api.entity.serializers import EntitiesRequestSerializer, EntityResponseSerializer, EntityCreateSerializer, EntityUpdateSerializer, EntityIdSerializer
from lumina.repositories.entities import get_entities, add_entity, update_entity, delete_entity


class EntitiesAPI(Resource):
    def get(self):
        request_serializer = EntitiesRequestSerializer()
        data = request_serializer.load(request.args)

        entities = get_entities(data)

        serializer = EntityResponseSerializer(many=True)
        return serializer.dump(entities), 200

    def post(self):
        create_serializer = EntityCreateSerializer()
        data = create_serializer.load(request.json)

        entity = add_entity(data)

        serializer = EntityResponseSerializer()
        return serializer.dump(entity), 200

    def put(self, entity_id=None):
        if not entity_id:
            return {"error": "Entity ID is required"}, 400
        id_serializer = EntityIdSerializer()
        entity_id = id_serializer.load({"id": entity_id})
        update_serializer = EntityUpdateSerializer()
        data = update_serializer.load(request.json)

        entity = update_entity(entity_id, data)

        serializer = EntityResponseSerializer()
        return serializer.dump(entity), 200

    def delete(self, entity_id):
        id_serializer = EntityIdSerializer()
        entity_id = id_serializer.load({"id": entity_id})

        delete_entity(entity_id)

        return {}, 204
