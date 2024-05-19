#!/usr/bin/env python3
"""
    Filtered Logger Module
"""
import re
from typing import List
import logging


class RedactingFormatter(logging.Formatter):
    """ Redacting Formatter class
        """

    REDACTION = "***"
    FORMAT = "[HOLBERTON] %(name)s %(levelname)s %(asctime)-15s: %(message)s"
    SEPARATOR = ";"

    def __init__(self, fields):
        super(RedactingFormatter, self).__init__(self.FORMAT)
        self.fields = fields

    def format(self, record: logging.LogRecord) -> str:
        original_message = super(RedactingFormatter, self).format(record)
        record_message = record.getMessage()
        filtered_message = filter_datum(self.fields,
                                        RedactingFormatter.REDACTION,
                                        record_message,
                                        RedactingFormatter.SEPARATOR)
        return original_message.replace(record_message, filtered_message)


def filter_datum(fields: List[str], redaction: str,
                 message: str, separator: str) -> str:
    """ Filter Datum Method """
    for field in fields:
        field_pattern = rf"({field}=)[^{separator}]*({separator})"
        message = re.sub(field_pattern, rf"\1{redaction}\2", message)

    return message
