#!/usr/bin/env python3
"""
Module for filtering and logging PII fields
"""
import re
import logging
from typing import List

# List of PII fields
PII_FIELDS = ('name', 'email', 'phone', 'ssn', 'password')


def filter_datum(fields: List[str], redaction: str, message: str,
                 separator: str) -> str:
    """
    Returns the log message obfuscated:
    - fields: list of strings representing all fields to obfuscate
    - redaction: string representing by what the field will be obfuscated
    - message: string representing the log line
    - separator: string representing by which character is separating all field
    """
    for field in fields:
        message = re.sub(
            f'{field}=.*?{separator}',
            f'{field}={redaction}{separator}',
            message
        )
    return message


class RedactingFormatter(logging.Formatter):
    """
    Redacting Formatter class
    """

    def __init__(self, fields: List[str]):
        super(RedactingFormatter, self).__init__()
        self.fields = fields

    def format(self, record: logging.LogRecord) -> str:
        """
        Filters values in incoming log records using `filter_datum`
        """
        original_message = super(RedactingFormatter, self).format(record)
        return filter_datum(self.fields, '***', original_message, ';')


def get_logger() -> logging.Logger:
    """
    Returns a logging.Logger object named "user_data"
    """
    logger = logging.getLogger('user_data')
    logger.setLevel(logging.INFO)
    logger.propagate = False

    stream_handler = logging.StreamHandler()
    stream_handler.setLevel(logging.INFO)

    formatter = RedactingFormatter(fields=PII_FIELDS)
    stream_handler.setFormatter(formatter)

    logger.addHandler(stream_handler)

    return logger


if __name__ == '__main__':
    print(filter_datum(["password", "date_of_birth"],
                       '***',
                       "name=John;email=john.doe@example.com;"
                       "password=123456;date_of_birth=01/01/1970;",
                       ";"))
    logger = get_logger()
    logger.info("name=John;email=john.doe@example.com;password=123456;"
                "date_of_birth=01/01/1970;")
