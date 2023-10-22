#!/usr/bin/env python3

"""A function named index_range that takes two integer
arguments page and page_size.

The function should return a tuple of size two containing
a start index and an end index corresponding to the range
of indexes to return in a list for those particular
pagination parameters.

Page numbers are 1-indexed, i.e. the first page is page 1.
"""

from typing import Tuple


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """A helpler function that helps with the range of index of pagination"""
    offset = (page - 1) * page_size
    limit = page * page_size
    return (offset, limit)
