"""Endpoints for the API."""

import secrets

from flask import abort, Blueprint, request

from test_api.models import Message, db, Application

api = Blueprint('api', __name__)


@api.route('/apps/<app_name>', methods=['GET', 'POST'])
def home(app_name):
    """Route to generate and test API keys."""

    if request.method == 'GET':
        app = db.session.query(Application).filter_by(  # pylint: disable=no-member
            name=app_name).first_or_404()
        if request.headers.get('x-api-key') != app.api_key:
            abort(
                401,
                description='Missing or invalid app key.'
            )

        return {'success': True}

    if request.method == 'POST':
        app = Application.query.filter_by(name=app_name).first()
        api_key = secrets.token_hex(32)
        while Application.query.filter_by(api_key=api_key).first():
            api_key = secrets.token_hex(32)

        if not app:
            app = Application(
                name=app_name,
                api_key=api_key
            )
            db.session.add(app)  # pylint: disable=no-member

        else:
            app.api_key = api_key

        db.session.commit()  # pylint: disable=no-member
        return {'app-name': app.name, 'api-key': app.api_key}

    return None


@api.route('/messages')
def get_all_messages():
    """Route to get all messages in a list."""

    if not db.session.query(Application.id).filter_by(  # pylint: disable=no-member
            api_key=request.headers.get('X-Api-Key')).first():
        abort(401)

    return {
        'messages': [
            {
                'application': str(message.application),
                'title': message.title,
                'text': message.text
            } for message in db.session.query(Message).all()    # pylint: disable=no-member
        ]
    }


@api.route('/messages/<message_title>', methods=['GET', 'POST'])
def message(message_title: str):
    """Route to read or create a message."""

    application = db.session.query(Application).filter_by(  # pylint: disable=no-member
        api_key=request.headers.get('X-Api-Key')).first()
    if not application:
        abort(401)

    if request.method == 'GET':
        _message = db.session.query(Message).filter_by( # pylint: disable=no-member
            title=message_title).first_or_404()

    if request.method == 'POST':
        _message = Message(
            title=message_title,
            text=request.data.decode(),
            application=application
        )
        db.session.add(_message)    # pylint: disable=no-member
        db.session.commit() # pylint: disable=no-member

    data = {
        'application': str(_message.application),
        'title': _message.title,
        'text': _message.text
    }
    return data
