from ordered_set import OrderedSet
import os
import seq
from pprint import pprint
from _bytes import uint

def main():
    for seq_path in get_seq_files('files'):
        get_list_of(seq_path, seq.ANIMATION_FLAG_ID)
    #get_action_sizes('files/iru0000.seq')
    #get_instruction_from_action_offset('files/iru0000.seq', 8)
    #check_bytes()
    
def get_list_of(seq_path, instruction):
    print(seq_path)
    ids = set()
    with open(seq_path, 'rb') as seq_file:
        seq_bytes = seq_file.read()
    index = 0
    while index < len(seq_bytes):
        word, index = get_word(seq_bytes, index)
        if word == instruction:
            weird, index = get_word(seq_bytes, index)
            ids.add(weird)
    print(sorted(ids))

def check_byte(seq_bytes):
    outputs = set()
    index = 0
    while index < len(seq_bytes):
        word, index = get_word(seq_bytes, index)
        if word == 0x04026600:
            weird, index = get_word(seq_bytes, index)
            weird, index = get_word(seq_bytes, index)
            outputs.add('{:X}'.format(weird))
    return outputs

def get_instruction_from_action_offset(seq_path, offset):
    ''' Finds the instruction at a given offset in all actions moving backwards. '''
    with open(seq_path, 'rb') as seq_file:
        seq_bytes = seq_file.read()
        action_offsets = get_action_offsets(seq_bytes)
        for index, action_offset in enumerate(action_offsets):
            if index == 0:
                print(get_hex(action_offset))
            else:
                new_offset = action_offset - offset
                print(get_hex(action_offset) + ' ' + get_hex(uint(seq_bytes[new_offset:new_offset+4])) + ' ' + get_hex(uint(seq_bytes[new_offset+4:new_offset+8])))

def get_action_sizes(seq_path):
    ''' Finds the size of each action based on the difference between them each. '''
    with open(seq_path, 'rb') as seq_file:
        seq_bytes = seq_file.read()
        action_offsets = get_action_offsets(seq_bytes)
        for index, action_offset in enumerate(action_offsets):
            if index == 0 or index == len(action_offsets) - 1:
                print(get_hex(action_offset))
            else:
                print(get_hex(action_offset) + ' ' + get_hex(action_offsets[index + 1] - action_offset))

def get_action_offsets(seq_bytes):
    ''' Returns all action offsets for a given byte array. '''
    actions = set()
    for offset in seq.OFFSET_TO_ACTION.keys():
        action = uint(seq_bytes[offset:offset+4])
        actions.add(action)
    return sorted(actions)

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
    return word, index

def get_hex(word):
    ''' Gets the hex for a 4-byte word. '''
    return '{:08X}'.format(word)

if __name__ == '__main__':
    main()
