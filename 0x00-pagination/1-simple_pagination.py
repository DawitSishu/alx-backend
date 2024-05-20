#!/usr/bin/env python3
"""
pagination
"""
import csv
from typing import List, Tuple


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """
    index range retriver
    """
    start = (page - 1) * page_size
    end = start + page_size
    return (start, end)


class Server:
    """paginate babay names
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        """new server
        """
        self.__dataset = None

    def dataset(self) -> List[List]:
        """Cached data
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """page of data
        """
        assert type(page) == int and type(page_size) == int
        assert page > 0 and page_size > 0
        start, end = index_range(page, page_size)
        data = self.dataset()
        if start > len(data):
            return []
        return data[start:end]
