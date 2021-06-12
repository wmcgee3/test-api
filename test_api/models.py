"""Models for api persistent data."""
# pylint: disable=no-member,too-few-public-methods

from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class Application(db.Model):
    """ORM object for Application."""

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(32), unique=True, nullable=False)
    api_key = db.Column(db.String(64), unique=True, nullable=False)
    messages = db.relationship('Message', backref='application', lazy=True)

    def __repr__(self):
        return str(self.name)


class Message(db.Model):
    """ORM object for saving messages."""

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(32), nullable=False)
    text = db.Column(db.Text(), nullable=False)
    application_id = db.Column(db.Integer, db.ForeignKey('application.id'), nullable=False)

    def __repr__(self):
        return str(self.title)
