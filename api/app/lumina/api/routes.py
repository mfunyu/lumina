from flask import Blueprint
from flask_restful import Api

from lumina.api.misc import resources as misc_resources
from lumina.api.entity import resources as entity_resources
from lumina.api.room import resources as room_resources

blueprint = Blueprint("api", __name__)
api = Api(blueprint)

# Misc endpoints
api.add_resource(misc_resources.VersionAPI, "/")

# Entities endpoints
api.add_resource(entity_resources.EntitiesAPI, "/entities", "/entities/<uuid:entity_id>")

# Rooms endpoints
api.add_resource(room_resources.RoomsAPI, "/rooms", "/rooms/<uuid:room_id>")
