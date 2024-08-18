#!/usr/bin/env python3
"""
pagination 1
"""
import csv
import math
from typing import List, Tuple


def index_range(page: int, page_size: int) -> Tuple:
    """
    return a tuple of a start index and an end index
    """
    start_index: int = (page - 1) * page_size
    end_index: int = start_index + page_size
    return (start_index, end_index)


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
        """
        return a pagination
        """
        assert isinstance(page, type(1)) and isinstance(page, type(page_size))
        assert page > 0 and page_size > 0
        tup: Tuple = index_range(page, page_size)
        data = self.dataset()
        if page_size > len(data):
            return []
        return data[tup[0]:tup[1]]
