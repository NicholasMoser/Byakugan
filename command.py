'''
A specific 8-byte command in a sequence file.
The first 4-byte word is the command. The second 4-byte word is the value.
'''
class Command:
    ''' Initialize with the command and its value. '''
    def __init__(self, cmd_hex, cmd_description, val_hex, val_description):
        self.cmd_hex = cmd_hex
        self.cmd_description = cmd_description
        self.val_hex = val_hex
        self.val_description = val_description

    def __repr__(self):
        return '{:08X} {}\n{:08X}     {}'.format(
            self.cmd_hex, self.cmd_description, self.val_hex, self.val_description
            )
