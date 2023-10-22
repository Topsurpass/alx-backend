#!/usr/bin/env python3
"""Hypermedia pagination"""

from typing import Tuple, Dict, Any
import csv
import math
from typing import List


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """A helpler function that helps with the range of index of pagination"""
    offset = (page - 1) * page_size
    limit = page * page_size
    return (offset, limit)


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
        """A function that helps find the correct indexes to paginate
        the dataset correctly and return the appropriate page of the datase
        """
        assert isinstance(page, int) and isinstance(page_size, int)
        assert page > 0 and page_size > 0
        data = self.dataset()
        idx = index_range(page, page_size)

        return [data[x] for x in range(idx[0], idx[1]) if idx[1] < len(data)]

    def get_hyper(self, page: int = 1, page_size: int = 10) -> Dict[str, Any]:
        """A hypermedia pagination function that takes the same arguments
        (and defaults) as get_page and returns a dictionary containing
        the key-value pairs.
        The 'total_pages' key helps us to know how many pages left to go
        to exhaust all the data retrieve from the database. This is calculated
        by dividing the total size of the data by page size"""
        data = self.get_page(page, page_size)
        hyper_dict = {
                'page_size': page_size if len(data) > 0 else 0,
                'page': page,
                'data': data,
                'next_page': page + 1 if len(data) > 0 else None,
                'prev_page': page - 1 if page > 1 else None,
                'total_pages': math.ceil(len(self.__dataset) / page_size)
                }
        return hyper_dict
