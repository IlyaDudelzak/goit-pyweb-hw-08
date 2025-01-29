from bson.objectid import ObjectId
from datetime import datetime
import connect

from mongoengine import EmbeddedDocument, Document
from mongoengine.fields import BooleanField, ReferenceField, EmbeddedDocumentField, ListField, StringField

class Contact(Document):
    fullname = StringField()
    email = StringField()
    sent = BooleanField()