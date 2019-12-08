from app import create_app, db
from app.models import Message
from app.serialization import MessageSchema
from flask import request
from flask_cors import CORS
from sqlalchemy import desc

app = create_app()
session = db.session

message_serializer = MessageSchema()
messages_serializer = MessageSchema(many=True)

CORS(app, resources={r'/*': {'origins': 'http://localhost:8090'}})


@app.route('/messages', methods=['GET'])
def list_messages():
    searchString = request.args.get("search", "")
    query = Message.query.filter_by(deleted=False)\
        .filter(Message.text.contains(searchString) | Message.author_name.contains(searchString))\
        .order_by(desc(Message.created_date))\
        .limit(10)
    return messages_serializer.jsonify(query)


@app.route('/messages', methods=['POST'])
def add_message():
    data = request.get_json()
    m = Message(author_name=data["author"], text=data["text"])
    session.add(m)
    session.commit()
    return message_serializer.jsonify(m)


@app.route('/messages/<message_id>', methods=['GET', 'DELETE'])
def get_or_delete_message(message_id):
    m = Message.query.filter_by(deleted=False, id=message_id).first_or_404()
    if request.method == 'DELETE':
        m.deleted = True
        session.commit()
    return message_serializer.jsonify(m)

