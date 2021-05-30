from test_api import create_app
from test_api.models import db


db.create_all(app=create_app())
