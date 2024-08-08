#!/usr/bin/env python3
""" UserSession model for storing session IDs in the database. """

from models.base import Base


class UserSession(Base):
    """ Class for handling user sessions stored in the database. """

    def __init__(self, *args: list, **kwargs: dict):
        """ Initialize UserSession instance. """
        super().__init__(*args, **kwargs)
        self.user_id = kwargs.get('user_id')
        self.session_id = kwargs.get('session_id')
