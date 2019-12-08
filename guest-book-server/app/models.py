from app import db
from datetime import datetime
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Boolean, Column, DateTime, Integer, String


class Message(db.Model):
    id = Column(Integer, primary_key=True)
    author_name = Column(String(100), nullable=False)
    created_date = Column(DateTime, default=datetime.utcnow)
    text = Column(String(1000), nullable=False)
    deleted = Column(Boolean, default=False)

    def __repr__(self):
        return 'Message %i by %r' % (self.id, self.author)
