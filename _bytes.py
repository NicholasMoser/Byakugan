'''
Utilities for working with bytes.
'''
def uint4(byte_list):
    ''' Returns the big endian integer for a list of four bytes.'''
    length = len(byte_list)
    if  length != 4:
        raise ValueError('Byte list should be size four. The size was: {}'.format(length))
    return int.from_bytes(byte_list, byteorder='big')
