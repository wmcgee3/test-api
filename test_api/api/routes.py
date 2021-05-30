"""Endpoints for the API."""

import json
import secrets

import flask

from test_api.models import db, Application

api = flask.Blueprint('api', __name__)


@api.route('/<app_name>', methods=['GET', 'POST'])
def home(app_name):
    """Home route of API."""

    response = None

    if flask.request.method == 'GET':
        app = Application.query.filter_by(name=app_name).first_or_404()
        if app.api_key and flask.request.headers.get('x-api-key') == app.api_key:
            response = {'success': True}
        else:
            flask.abort(
                401,
                description='Missing or invalid app key.'
            )

    elif flask.request.method == 'POST':
        app = Application.query.filter_by(name=app_name).first()
        api_key = secrets.token_hex(32)
        while Application.query.filter_by(api_key=api_key).first():
            api_key = secrets.token_hex(32)
        if not app:
            app = Application(
                name=app_name,
                api_key=api_key
            )
            db.session.add(app) # pylint: disable=no-member
        else:
            app.api_key = api_key
        db.session.commit() # pylint: disable=no-member
        response = json.loads(str(app))

    return response
