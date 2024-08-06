#!/usr/bin/env python3
""" Initialize views module
"""
from flask import Blueprint
from api.v1.views.index import *

app_views = Blueprint("app_views", __name__, url_prefix="/api/v1")

# Delayed imports to avoid circular import issues
