"""Creates the Flask application."""

import flask


def create_app():
    """Create the Flask app."""
    # pylint: disable=import-outside-toplevel

    app = flask.Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'

    from test_api.models import db

    db.init_app(app)

    from test_api.api.routes import api

    app.register_blueprint(api)

    return app
