#!/usr/bin/env python3
""" Module of Index views """
from flask import Blueprint

app_views = Blueprint('app_views', __name__)

# Import the views after defining the blueprint to avoid circular imports
from api.v1.views.index import *  # noqa
