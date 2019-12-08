from app import create_app, db
from app.models import Message
from app.serialization import MessageSchema
from flask import jsonify, request
from flask_cors import CORS

app = create_app()
session = db.session

message_serializer = MessageSchema()
messages_serializer = MessageSchema(many=True)

CORS(app, resources={r'/*': {'origins': 'http://localhost:8080'}})


@app.route('/messages', methods=['GET'])
def list_messages():
    return messages_serializer.jsonify(Message.query.all())


@app.route('/messages', methods=['POST'])
def add_message():
    data = request.get_json()
    m = Message(author_name=data["author"], text=data["text"])
    session.add(m)
    session.commit()
    return message_serializer.jsonify(m)