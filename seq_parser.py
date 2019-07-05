'''
Parses a SEQ file.
'''
import seq
from command import Command

class SeqParser:
    ''' A seq file parser. '''
    def __init__(self, seq_bytes):
        self.seq_bytes = seq_bytes
        self.index = 0

    def read_action(self, start, length):
        ''' Reads an action in seq from the start index to the end index. '''
        commands = []
        self.index = start
        end = start + length
        while self.index <= end:
            word = self.get_word()
            if word == seq.KF_ATTACK_FLAG_ID:
                cmd_description = seq.KF_ATTACK_FLAG_DESCRIPTION
                flag_mask = self.get_word()
                val_description = self.get_kf_flags(flag_mask)
                commands.append(Command(word, cmd_description, flag_mask, val_description))
            elif word == seq.KF_ATTACK_FLAG_PROJ_ID:
                cmd_description = seq.KF_ATTACK_FLAG_PROJ_DESCRIPTION
                flag_mask = self.get_word()
                val_description = self.get_kf_flags(flag_mask)
                commands.append(Command(word, cmd_description, flag_mask, val_description))
            elif word == seq.K2F_SPECIAL_ATTACK_FLAG_ID:
                cmd_description = seq.K2F_SPECIAL_ATTACK_FLAG_DESCRIPTION
                flag_mask = self.get_word()
                val_description = self.get_k2f_flags(flag_mask)
                commands.append(Command(word, cmd_description, flag_mask, val_description))
            elif word == seq.K2F_SPECIAL_ATTACK_PROJ_FLAG_ID:
                cmd_description = seq.K2F_SPECIAL_ATTACK_PROJ_FLAG_DESCRIPTION
                flag_mask = self.get_word()
                val_description = self.get_k2f_flags(flag_mask)
                commands.append(Command(word, cmd_description, flag_mask, val_description))
            elif word == seq.NF_STATE_FLAG_ID:
                cmd_description = seq.NF_STATE_FLAG_DESCRIPTION
                flag_mask = self.get_word()
                val_description = self.get_nf_flags(flag_mask)
                commands.append(Command(word, cmd_description, flag_mask, val_description))
            elif word == seq.AF_ACTION_STATE_FLAG_ID:
                cmd_description = seq.AF_ACTION_STATE_FLAG_DESCRIPTION
                flag_mask = self.get_word()
                val_description = self.get_af_flags(flag_mask)
                commands.append(Command(word, cmd_description, flag_mask, val_description))
            elif word == seq.ANIMATION_FLAG_ID:
                cmd_description = seq.ANIMATION_FLAG_DESCRIPTION
                animation_id = self.get_word()
                val_description = 'ID {}'.format(self.get_hex(animation_id))
                commands.append(Command(word, cmd_description, animation_id, val_description))
            elif word == seq.X_MOVE_METER_REQ_ID:
                cmd_description = seq.X_MOVE_METER_REQ_DESCRIPTION
                meter_req = self.get_word()
                val_description = self.get_hex(meter_req)
                commands.append(Command(word, cmd_description, meter_req, val_description))
            elif word == seq.HORIZ_MOBILITY_JUMP_MOVES_ID:
                cmd_description = seq.HORIZ_MOBILITY_JUMP_MOVES_DESCRIPTION
                mobility = self.get_word()
                val_description = self.get_hex(mobility)
                commands.append(Command(word, cmd_description, mobility, val_description))
            elif word == seq.VERT_MOBILITY_JUMP_MOVES_ID:
                cmd_description = seq.VERT_MOBILITY_JUMP_MOVES_DESCRIPTION
                mobility = self.get_word()
                val_description = self.get_hex(mobility)
                commands.append(Command(word, cmd_description, mobility, val_description))
            elif word == seq.PROJ_DMG_STUN_GUARD_ID:
                cmd_description = seq.PROJ_DMG_STUN_GUARD_DESCRIPTION
                info = self.get_word()
                val_description = self.get_hex(info)
                commands.append(Command(word, cmd_description, info, val_description))
            elif word == seq.SOUND_EFFECT_ID:
                cmd_description = seq.SOUND_EFFECT_DESCRIPTION
                info = self.get_word()
                val_description = 'ID {}'.format(self.get_hex(info))
                commands.append(Command(word, cmd_description, info, val_description))
            elif word == seq.CHR_ACT_ID:
                cmd_description = seq.CHR_ACT_DESCRIPION
                info = self.get_word()
                val_description = 'Offset {}'.format(self.get_hex(info))
                commands.append(Command(word, cmd_description, info, val_description))
            elif word == seq.HITBOX_ACTIVE_FRAMES_ID:
                cmd_description = seq.HITBOX_ACTIVE_FRAMES_DESCRIPTION
                both_frames, start_frame, end_frame = self.get_half_words()
                val_description = 'Frames: {} - {}'.format(start_frame, end_frame)
                commands.append(Command(word, cmd_description, both_frames, val_description))
            else:
                unknown = self.get_word()
                commands.append(Command(word, '?', unknown, '?'))
        return commands

    def get_word(self):
        ''' Reads and returns the next 4-byte word. '''
        word = int.from_bytes(self.seq_bytes[self.index:self.index+4], byteorder='big')
        self.index += 4
        return word

    def get_half_words(self):
        ''' Reads and returns the next two 2-byte words. '''
        word = int.from_bytes(self.seq_bytes[self.index:self.index+4], byteorder='big')
        first = int.from_bytes(self.seq_bytes[self.index:self.index+2], byteorder='big')
        second = int.from_bytes(self.seq_bytes[self.index+2:self.index+4], byteorder='big')
        self.index += 4
        return word, first, second

    @staticmethod
    def get_hex(word):
        ''' Gets the hex for a 4-byte word. '''
        return '{:08X}'.format(word)

    @staticmethod
    def get_kf_flags(flag_mask):
        ''' Given the bit mask for kf flags, returns the flag displays.'''
        flags = []
        for key, value in seq.KF_ATTACK_FLAGS.items():
            if flag_mask & key == key:
                flags.append(value)
        return flags

    @staticmethod
    def get_k2f_flags(flag_mask):
        ''' Given the bit mask for k2f flags, returns the flag displays.'''
        flags = []
        for key, value in seq.K2F_SPECIAL_ATTACK_FLAGS.items():
            if flag_mask & key == key:
                flags.append(value)
        return flags

    @staticmethod
    def get_nf_flags(flag_mask):
        ''' Given the bit mask for nf flags, returns the flag displays.'''
        flags = []
        for key, value in seq.NF_STATE_FLAGS.items():
            if flag_mask & key == key:
                flags.append(value)
        return flags

    @staticmethod
    def get_af_flags(flag_mask):
        ''' Given the bit mask for af flags, returns the flag displays.'''
        flags = []
        for key, value in seq.AF_ACTION_STATE_FLAGS.items():
            if flag_mask & key == key:
                flags.append(value)
        return flags

    def print_end_section_size(self):
        ''' Prints the size of the end section referenced by offset 0x14 '''
        weird_number = int.from_bytes(self.seq_bytes[20:24], byteorder='big')
        diff = len(self.seq_bytes) - weird_number
        diff_hex = "0x%0.4X" % diff
        print('{} ({})'.format(diff, diff_hex))
