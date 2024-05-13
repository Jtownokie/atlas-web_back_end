#!/usr/bin/env python3
""" Simple Pagination Module """
import csv
import math
from typing import List


def index_range(page: int, page_size: int) -> tuple:
    """ Returns tuple with start/end indices """
    return ((page * page_size) - page_size, page * page_size)


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        assert isinstance(page, int) and page > 0
        assert isinstance(page_size, int) and page_size > 0
        pagination_index = index_range(page, page_size)

        with open('Popular_Baby_Names.csv', 'r', encoding='utf-8') as f:
            reader = csv.reader(f)
            results = [row for idx, row in enumerate(reader)
                       if idx > pagination_index[0]
                       and idx <= pagination_index[1]]

        return results
