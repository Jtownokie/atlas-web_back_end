#!/usr/bin/env python3
""" Helper Function Module """


def index_range(page: int, page_size: int) -> tuple:
    """ Returns tuple with start/end indices """
    return ((page * page_size) - page_size, page * page_size)
