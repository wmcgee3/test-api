"""Models for api persistent data."""

import json

import flask_sqlalchemy

db = flask_sqlalchemy.SQLAlchemy()


class Application(db.Model):
    """ORM object for Application."""
    # pylint: disable=no-member,too-few-public-methods

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(32), unique=True, nullable=False)
    api_key = db.Column(db.String(64))

    def __repr__(self):
        return json.dumps(
            {
                'name': self.name,
                'api_key': self.api_key
            },
            indent=4
        )
