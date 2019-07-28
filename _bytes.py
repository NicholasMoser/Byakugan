'''
Utilities for working with bytes.
'''

def uint(byte_list):
    ''' Returns the big endian integer for a list of bytes.'''
    return int.from_bytes(byte_list, byteorder='big')
