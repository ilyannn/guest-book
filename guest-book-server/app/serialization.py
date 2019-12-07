from flask_marshmallow import Schema
from marshmallow.fields import Float, Integer, String
from app.models import Message


class MessageSchema(Schema):

    class Meta:
        model = Message
        fields = ["id", "author_name", "created_date", "text"]