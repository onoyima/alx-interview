#!/usr/bin/python3
"""
UTF-8 Validation Module
"""


def validUTF8(data):
    """
    Method that determines if a given data set represents
    a valid UTF-8 encoding.
    Args:
        data (List[int]): A list of integers where each integer
        represents 1 byte of data.
    Returns:
        bool: True if data is a valid UTF-8 encoding, else False.
    """
    n_bytes = 0

    for num in data:
        bin_rep = format(num, '#010b')[-8:]

        if n_bytes == 0:
            if bin_rep[0] == '0':
                continue
            elif bin_rep[:3] == '110':
                n_bytes = 1
            elif bin_rep[:4] == '1110':
                n_bytes = 2
            elif bin_rep[:5] == '11110':
                n_bytes = 3
            else:
                return False
        else:
            if bin_rep[:2] != '10':
                return False
        n_bytes -= 1

    return n_bytes == 0
