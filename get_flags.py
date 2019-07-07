from ordered_set import OrderedSet
import os
import seq
from pprint import pprint

def main():
    outputs = set()
    for seq_path in get_seq_files('files'):
        with open(seq_path, 'rb') as seq_file:
            seq_bytes = seq_file.read()
            index = 0
            while index < len(seq_bytes):
                word, index = get_word(seq_bytes, index)
                if word == 0x21040026:
                    index += 4
                    weird, index = get_word(seq_bytes, index)
                    if weird != 0:
                        print(weird)
    pprint(outputs)

def get_seq_files(directory):
    ''' Return all seq files from a given directory. '''
    files = []
    for name in os.listdir(directory):
        if name.lower().endswith('.seq'):
            files.append(os.path.join(directory, name))
    return files

def get_word(seq_bytes, index):
    ''' Reads, prints, and returns the next 4-byte word. '''
    word = int.from_bytes(seq_bytes[index:index+4], byteorder='big')
    index += 4
    #print_hex(word)
    return word, index

def print_hex(word):
    ''' Prints out the hex for a 4-byte word. '''
    print(get_hex(word))

def get_hex(word):
    ''' Gets the hex for a 4-byte word. '''
    return '{:08X}'.format(word)

def get_k2f_flags(flag_mask):
    ''' Given the bit mask for k2f flags, returns the flag displays.'''
    flags = []
    for key, value in seq.K2F_SPECIAL_ATTACK_FLAGS.items():
        if flag_mask & key == key:
            flags.append(value)
    return frozenset(flags)

if __name__ == '__main__':
    main()
