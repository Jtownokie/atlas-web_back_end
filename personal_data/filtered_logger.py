#!/usr/bin/env python3
"""
    Filtered Logger Module
"""
# import logging
import re


def filter_datum(fields, redaction, message, separator):
    """ Filter Datum Method """
    for field in fields:
        field_pattern = rf"({field}=)[^{separator}]*({separator})"
        message = re.sub(field_pattern, rf"\1{redaction}\2", message)

    return message
