'''
Byakugan will parse GNT4 seq files into a human-readable format.
'''
import os
import sys
import seq
import time
from seq_parser import SeqParser
from _bytes import uint

def main():
    ''' Run program. '''
    if len(sys.argv) == 3:
        read_action(sys.argv[1], int(sys.argv[2]))
    else:
        # For quicker debugging, will remove later
        read_action('files/iru0000.seq', seq.ACTION_5B)

def read_action(seq_path, action_id):
    ''' From a given seq path and action id, prints the details of that character's action. '''
    with open(seq_path, 'rb') as seq_file:
        seq_bytes = seq_file.read()
    for offset, action in seq.OFFSET_TO_ACTION.items():
        if action_id == action.id:
            print(action.description)
            flags_start = uint(seq_bytes[offset:offset+4])
            print('Offset: {:X}'.format(flags_start))
            seq_parser = SeqParser(seq_bytes)
            # Currently not able to figure out end of the action, so just do a fixed sized
            commands = seq_parser.read_action(flags_start, 334)
            for command in commands:
                print(command)
            return
    print('Error: Could not find action id {:08x} in {}'.format(action_id, seq_path))

def read_seq(seq_path):
    ''' Reads a specific seq file for info. '''
    print(seq_path)
    with open(seq_path, 'rb') as seq_file:
        seq_bytes = seq_file.read()
    all_starts = set()
    for offset, action in seq.OFFSET_TO_ACTION.items():
        flags_start = uint(seq_bytes[offset:offset+4])
        if flags_start == seq.CHR_ACT:
            print('{} {}'.format(offset, action.description))
        all_starts.add(flags_start)
        #seq_parser.read_action(seq, flags_start, end?)
    print(sorted(all_starts))

def get_seq_files(directory):
    ''' Return all seq files from a given directory. '''
    files = []
    for name in os.listdir(directory):
        if name.lower().endswith('.seq'):
            files.append(os.path.join(directory, name))
    return files

if __name__ == '__main__':
    main()
