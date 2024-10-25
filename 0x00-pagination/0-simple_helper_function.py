#!/usr/bin/env python3
'''0. Simple helper function'''
from typing import Tuple


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    '''return a tuple of size two containing a start index and an end index'''
    end_index: int = page * page_size
    start_index: int = 0 if page == 1 else end_index - page_size
    return (start_index, end_index)
