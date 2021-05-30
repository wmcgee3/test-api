"""Runs the development web server."""
from test_api import create_app

app = create_app()

app.run(debug=True)
