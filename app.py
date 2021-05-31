"""Runs the development web server."""

import waitress

from test_api import create_app

waitress.serve(create_app(), host='127.0.0.1', port=5050, url_scheme='https')

# comment for testing
