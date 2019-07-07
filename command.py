'''
A specific command in a sequence file.
The first 4-byte word is the command. A variable number of 4-byte words after are the values.
'''
class Command:
    ''' Initialize with the command and its values. '''
    def __init__(self, cmd_hex, cmd_description, values):
        self.cmd_hex = cmd_hex
        self.cmd_description = cmd_description
        self.values = values

    def __repr__(self):
        message = '{:08X} {}'.format(self.cmd_hex, self.cmd_description)
        for val_hex, val_description in self.values:
            message = '{}\n{:08X}     {}'.format(message, val_hex, val_description)
        return message
