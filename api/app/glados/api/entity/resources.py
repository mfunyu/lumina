from flask import request
from flask_restful import Resource

from glados.api.entity.serializers import EntitiesRequestSerializer, EntityResponseSerializer, EntityUpdateSerializer
from glados.repositories.entities import get_entities, add_entity


class EntitiesAPI(Resource):
    def get(self):
        request_serializer = EntitiesRequestSerializer()
        data = request_serializer.load(request.args)

        entities = get_entities(data)

        serializer = EntityResponseSerializer(many=True)
        return serializer.dump(entities), 200

    def post(self):
        update_serializer = EntityUpdateSerializer()
        data = update_serializer.load(request.form)

        entity = add_entity(data)

        serializer = EntityResponseSerializer()
        return serializer.dump(entity), 200
