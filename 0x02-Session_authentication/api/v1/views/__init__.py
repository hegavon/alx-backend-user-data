#!/usr/bin/env python3
""" Module of Index views """
from flask import Blueprint

app_views = Blueprint('app_views', __name__, url_prefix="/api/v1")

# Import the views after defining the blueprint to avoid circular imports
from api.v1.views.index import *  # noqa
from api.v1.views.users import *
from api.v1.views.session_auth import *

User.load_from_file()
