#!/usr/bin/python3
"""A function that validates data if it is UTF-8 encoded"""


def validUTF8(data):
    """Validate if a list of integers are valid UTF-8 encoded

        Parameters
        ----------
        data: List[int]
            List of integers

        Returns
        -------
            True if `data` is valid UTF-8, False otherwise
    """
    BITS_IN_A_BYTE = 8
    index_position = 0
    data_len = len(data)
    while index_position < data_len:
        number_of_bytes = 0
        for bit in range(BITS_IN_A_BYTE):
            if data[bit] >> (7 - bit) & 1 == 1:
                number_of_bytes += 1
            else:
                break
        # If leading bits is 0, then it's single byte ASCII
        if number_of_bytes == 0:
            index_position += 1
            continue
        # For multi-byte, the format must be:
        # 110xxxxx, 1110xxxx or 11110xxx so 2, 3 or 4 bytes
        if number_of_bytes == 1 or number_of_bytes > 4:
            return False

        # Go to next byte
        index_position += 1
        # Check subsequent bytes start with format: 10xxxxxx
        for _ in range(1, number_of_bytes):
            # Right shifting by 6 ensures valid byte formats
            # have 10 at the end which is equal to 2
            if index_position >= data_len or data[index_position] >> 6 != 2:
                return False
            index_position += 1
    # Check incorrect byte sequence
    if index_position < data_len:
        return False
    return True
