#!/usr/bin/env python3
"""A function that validates data if it is UTF-8 encoded"""
from typing import List


def validUTF8(data: List[int]) -> bool:
    """Validate if a list of integers are valid UTF-8 encoded

        Parameters
        ----------
        data: List[int]
            List of integers

        Returns
        -------
            True if `data` is valid UTF-8, False otherwise
    """
    for number in data:
        # Shift bits and check UTF-8 adherance
        for i in range(8):
            # Shift the LSB and AND with 1 to check for byte order
            if number >> (7 - i) & 1 == 1:
                return False
            else:
                return True
    return False
