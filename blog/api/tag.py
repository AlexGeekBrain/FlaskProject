from flask_combo_jsonapi.resource import ResourceList, ResourceDetail

from blog.schemas.tag import TagSchema
from blog.models.database import db
from blog.models import Tag


class TagList(ResourceList):
    schema = TagSchema
    data_layer = {
        'session': db.session,
        'model': Tag,
    }


class TagDetail(ResourceDetail):
    schema = TagSchema
    data_layer = {
        'session': db.session,
        'model': Tag,
    }
