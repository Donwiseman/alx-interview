#!/usr/bin/python3
"""this module contain the validUTF8 function that validate utf-8 binaries"""


def validUTF8(data):
    """Validates a integer array representing a single byte to be either
       a valid or invalid utf-8 encoding."""

    cont_byte = 0

    for byte_data in data:
        if byte_data > 255:
            return False
        if byte_data < 128 and cont_byte == 0:
            continue
        if byte_data > 127 and cont_byte == 0:
            byte_str = format(byte_data, 'b')
            header = (byte_str.split('0', 1))[0]
            if len(header) < 2 or len(header) > 4:
                return False
            cont_byte = len(header) - 1
            continue
        if byte_data > 127 and cont_byte > 0:
            byte_str = format(byte_data, 'b')
            header = (byte_str.split('0', 1))[0]
            if len(header) != 1:
                return False
            cont_byte -= 1
            continue
        return False
    return True
