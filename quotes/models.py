from datetime import datetime
import connect

from mongoengine import EmbeddedDocument, Document
from mongoengine.fields import BooleanField, ReferenceField, EmbeddedDocumentField, ListField, StringField


class Tag(EmbeddedDocument):
    name = StringField(primary_key=True)

class Author(Document):
    fullname = StringField(primary_key=True)
    born_date = StringField()
    born_location = StringField()
    description = StringField()

class Quote(Document):
    tags = ListField(EmbeddedDocumentField(Tag))
    author = ReferenceField('Author')
    quote = StringField()