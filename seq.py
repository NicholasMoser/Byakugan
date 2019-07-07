'''
SEQ File Constants
'''
from collections import OrderedDict, namedtuple

# 
Action = namedtuple('Action', ['id', 'description'])

# SEQ File Sections
CHR_TBL = 'chr_tbl'
CHR_ACT = 'chr_act'
CHR_CAM = 'chr_cam'
CHR_SUB02 = 'chr_sub02'
CHR_MODEL = 'chr_model'
CHR_MOT = 'chr_mot'
CHR_HIRA = 'chr_hira'
CHR_SEL = 'chr_sel'
CHR_SHOT = 'chr_shot'
CHR_FACE = 'chr_face'
CHR_DATA = 'chr_data'
CHR_VISUAL2D = 'chr_visual2d'

# Notable Action IDs
ACTION_5B = 0x0A0
ACTION_6B = 0x0A1
ACTION_4B = 0x0A2
ACTION_2B = 0x0A3
ACTION_RB = 0x0A5
ACTION_5A = 0x0B0
ACTION_6A = 0x0B1
ACTION_4A = 0x0B2
ACTION_2A = 0x0B3
ACTION_RA = 0x0B5
ACTION_RKNJ_GROUND = 0x0C0
ACTION_RKNJ_AIR = 0x0C1
ACTION_LKNJ = 0x0C2
ACTION_ZKNJ_INCOMING = 0x0C3
ACTION_5Z_OUTGOING = 0x0C6
ACTION_4Z_INCOMING = 0x0C7
ACTION_5Z_INCOMING = 0x0C8
ACTION_ZKNJ_OUTGOING = 0x0CB
ACTION_4Z_OUTGOING = 0x0CF
ACTION_JB = 0x0E0
ACTION_JA = 0x0E1
ACTION_8B = 0x0E2
ACTION_8A = 0x0E3
ACTION_5X = 0x121
ACTION_2X = 0x122
ACTION_COMBO_START = 0x130
ACTION_GROUND_THROW = 0x190
ACTION_BACK_GROUND_THROW = 0x191
ACTION_AIR_THROW = 0x192
ACTION_ACTIVATED_X = 0x193

ANIMATION_FLAG_ID = 0x0402023F
ANIMATION_FLAG_DESCRIPTION = 'Animation Flag'

X_MOVE_METER_REQ_ID = 0x227F2000
X_MOVE_METER_REQ_DESCRIPTION = 'Meter Requirement for X Moves'

HORIZ_MOBILITY_JUMP_MOVES_ID = 0x2414010B
HORIZ_MOBILITY_JUMP_MOVES_DESCRIPTION = 'Horizontal Mobility for Jump Moves'

VERT_MOBILITY_JUMP_MOVES_ID = 0x2414020B
VERT_MOBILITY_JUMP_MOVES_DESCRIPTION = 'Vertical Mobility for Jump Moves'

PROJ_DMG_STUN_GUARD_ID = 0x47040000
PROJ_DMG_STUN_GUARD_DESCRIPTION = 'Projectile damage, stun, guard damage, etc'

SOUND_EFFECT_ID = 0x24170000
SOUND_EFFECT_DESCRIPTION = 'Sound Effect'

CHR_ACT_ID = 0x013C0000
CHR_ACT_DESCRIPION = 'Character Action Offset'

HITBOX_ACTIVE_FRAMES_ID = 0x21070026
HITBOX_ACTIVE_FRAMES_DESCRIPTION = 'Hitbox Active Frames'

HITBOX_LOC_SIZE_ID = 0x21040026
HITBOX_LOC_SIZE_DESCRIPTION = 'Hitbox Locations and Sizes'

POW_DMG_GRD_ID = 0x21050026
POW_DMG_GRD_DESCRIPTION = 'POW, DMG, and GRD of a move'

ANG_DIR_ID = 0x21060026
ANG_DIR_DESCRIPTION = 'ANG and DIR of a move'

# KF Flags
KF_ATTACK_FLAG_ID = 0x241A1200
KF_ATTACK_FLAG_DESCRIPTION = 'KF Attack Flags'
KF_ATTACK_FLAG_PROJ_ID = 0x48040000
KF_ATTACK_FLAG_PROJ_DESCRIPTION = 'KF Attack Flags (Projectile)'
KF_ATTACK_FLAGS = {
    0x00000001: 'replay',      # No effect
    0x00000002: 'BDrive',      # Changes lighting, no sub or tech roll, generally on Ougi moves
    0x00000004: 'Shot',
    0x00000008: 'Pow_W',       # Weak hit. affects blockstun and hitstun
    0x00000010: 'Pow_M',       # Medium hit
    0x00000020: 'Pow_S',       # Strong hit
    0x00000040: 'Low',         # Attack hits low, and can be evaded by AF float flag
    0x00000080: 'Middle',      # Attack hits middle
    0x00000100: 'High',        # Attack hits high, and can be evaded by AF sit flag
    0x00000200: 'Punch',       # Attack is classified as a punch
    0x00000400: 'Kick',        # Attack is classified as a kick
    0x00000800: 'Throw',       # Attack is classified as a throw, no sub or tech roll
    0x00001000: 'Oiuchi',      # Hits later on OTG and during tech rolls (also called “Pursuit”)
    0x00002000: 'Special',     # Builds no chakra, generally seen on Ougi moves
    0x00004000: 'NoGuard',     # Unblockable
    0x00008000: 'TDown',
    0x00010000: 'SPTata',      # This is a large bounce. Ex: Naruto 4B
    0x00020000: 'Break',       # This combines with other KF flags to affect the opponents guard.
    0x00040000: 'Combo',       # Still not entirely understood
    0x00080000: 'Down',        # Spinout launcher. Launches higher than Uki flag
    0x00100000: 'Yoro',        # Stagger
    0x00200000: 'Butt',        # Flying Screen knockback
    0x00400000: 'Uki',         # Launch on hit
    0x00800000: 'Furi',        # Turns opponents around on hit. This is leftover from Bloody Roar and not used.
    0x01000000: 'Koro',        # Sweep: beats super armor, cannot be Y cancelled
    0x02000000: 'Reach_L',     # Unsure, but generally in attacks with a good deal of motion. Ex: Naruto 6B
    0x04000000: 'Tata',        # Small Ground Bounce. Ex: Naruto 6B
    0x08000000: 'NoSpeEp',
    0x10000000: 'Beast',       # Slash hit effect and chip damage
    0x20000000: 'Freeze',      # Opponent moves less during the attack, which allows moves to combo better
    0x40000000: 'Cancel',      # Cancel the move when you press Y like an any frame feint (not used)
    0x80000000: 'AtkCan'       # Super Cancel
}

# K2F Flags
K2F_SPECIAL_ATTACK_FLAG_ID = 0x241A4800
K2F_SPECIAL_ATTACK_FLAG_DESCRIPTION = 'K2F Special Attack Flags'
K2F_SPECIAL_ATTACK_PROJ_FLAG_ID = 0x48150000
K2F_SPECIAL_ATTACK_PROJ_FLAG_DESCRIPTION = 'K2F Special Attack Flags (Projectile)'
K2F_SPECIAL_ATTACK_FLAGS = {
    0x00000001: 'yoro2',       # Feet trapped. Ex: Kidomaru 5A1C
    0x00000002: 'hiki',        # Sink into the ground and pop out. Ex: Jiraya 2A
    0x00000004: 'hiki2',       # Sink into the ground and fall from above. Ex: Shika 2X
    0x00000008: 'mission',
    0x00000010: 'natemi',
    0x00000020: 'superarmor',  # Gives the move super armor, must be turned off. Ex: Chouji 5A
    0x00000040: 'mato2',       # Trapped. Ex: Shino 2A
    0x00000080: 'atkallcan',   # Can follow up with any other attack
    0x00000100: 'toji',
    0x00000200: 'hasa',        # Crumple. Ex: Jirobo stone clap crumple
    0x00000400: 'shave',       # For Kisame.
    0x00000800: 'nemu',        # Sleep. Ex: Kabuto 2X
    0x00001000: 'wing',        # ex: Kabuto 2X
    0x00002000: 'null1',       # Crumple. Ex: OTK 2X
    0x00004000: 'null2'
}

# NF Flags
NF_STATE_FLAG_ID = 0x241A0900
NF_STATE_FLAG_DESCRIPTION = 'NF State Flags'
NF_STATE_FLAGS = {
    0x00000001: 'kamae',
    0x00000002: 'disp',        # Disappears, can even walk through opponent while invisible.
    0x00000004: 'tdmg',        # Used in conjuction with tdown for intangibility.
    0x00000008: 'jump2',       # Flag that appears after doing your midair jump
    0x00000010: 'leverdir',
    0x00000020: 'getup',
    0x00000040: 'hiteft',
    0x00000080: 'nfog',
    0x00000100: 'takeon',
    0x00000200: '(blank)',
    0x00000400: 'bdrivesleep', # Makes BDrive not active.
    0x00000800: 'jump',
    0x00001000: 'fall',
    0x00002000: 'jspd',
    0x00004000: 'shotdef',     # Expected this to block projectiles. It didn't.
    0x00008000: 'move',
    0x00010000: 'attack',
    0x00020000: 'button',
    0x00040000: 'combo',
    0x00080000: 'disp_n',      # Disappears. Ends at the end of the action..?
    0x00100000: 'kabehit',
    0x00200000: 'bodytouch',   # Used for some throw attacks like Kisame. Disables sub.
    0x00400000: 'aguard',
    0x00800000: 'damage',
    0x01000000: 'guard',
    0x02000000: 'autodir',     # Determines if something has any tracking on it..?
    0x04000000: 'eneauto',
    0x08000000: 'njpturn',
    0x10000000: 'ringout',
    0x20000000: 'kabe',
    0x40000000: 'tdown',
    0x80000000: 'lever'
}

# AF Flags
AF_ACTION_STATE_FLAG_ID = 0x241A0000
AF_ACTION_STATE_FLAG_DESCRIPTION = 'AF Action State Flags'
AF_ACTION_STATE_FLAGS = {
    0x00000001: 'stand',
    0x00000002: 'forward',
    0x00000004: 'back',
    0x00000008: 'dash',
    0x00000010: 'sit',         # Immune to high attacks.
    0x00000020: 'fuse',
    0x00000040: 'ukemi',
    0x00000080: 'kiri',
    0x00000100: 'spmdmg',
    0x00000200: 'slant',
    0x00000400: 'quick',
    0x00000800: 'float',
    0x00001000: 'jump',
    0x00002000: 'fall',
    0x00004000: 'small',
    0x00008000: 'damage',
    0x00010000: 'downu',
    0x00020000: 'downo',
    0x00040000: 'getup',
    0x00080000: 'turn',
    0x00100000: 'tdown',
    0x00200000: 'cantact',
    0x00400000: 'sdef',        # Side defense.
    0x00800000: 'bdef',        # Back defense.
    0x01000000: 'beast',
    0x02000000: 'uki',         # Note: if this is added on an attacking move, that move can no longer Y cancel.
    0x04000000: 'butt',
    0x08000000: 'ndown',
    0x10000000: 'def',         # Defense from the front. Like 4B guard.
    0x20000000: 'tfail',       # Missed throw
    0x40000000: 'throw',
    0x80000000: 'attack',
}

# Mapping of a seq file offset to its associated action
OFFSET_TO_ACTION = OrderedDict([
    (0x030, Action(0x000, 'Do nothing (Freeze animations)')),
    (0x034, Action(0x001, 'Do nothing')),
    (0x038, Action(0x002, 'Walk forward')),
    (0x03C, Action(0x003, 'Walk backwards')),
    (0x040, Action(0x004, 'Dash')),
    (0x044, Action(0x005, 'Run forward')),
    (0x048, Action(0x006, 'Quick dash forward')),
    (0x04C, Action(0x007, 'Quick dash backward')),
    (0x050, Action(0x008, 'Freeze character (Can be thrown out)')),
    (0x054, Action(0x009, 'Do nothing')),
    (0x058, Action(0x00A, 'Do nothing')),
    (0x05C, Action(0x00B, 'Do nothing')),
    (0x060, Action(0x00C, 'Do nothing')),
    (0x064, Action(0x00D, 'Do nothing')),
    (0x068, Action(0x00E, 'Do nothing')),
    (0x06C, Action(0x00F, 'Do nothing')),
    (0x070, Action(0x010, 'Do nothing')),
    (0x074, Action(0x011, 'Do nothing')),
    (0x078, Action(0x012, 'Do nothing')),
    (0x07C, Action(0x013, '8B')),
    (0x080, Action(0x014, 'Jump')),
    (0x084, Action(0x015, 'Jump forward')),
    (0x088, Action(0x016, 'Jump backwards')),
    (0x08C, Action(0x017, 'Jump')),
    (0x090, Action(0x018, 'Jump forward')),
    (0x094, Action(0x019, 'Jump backwards')),
    (0x098, Action(0x01A, 'JB')),
    (0x09C, Action(0x01B, 'JB')),
    (0x0A0, Action(0x01C, 'JB')),
    (0x0A4, Action(0x01D, 'Land')),
    (0x0A8, Action(0x01E, 'L')),
    (0x0AC, Action(0x01F, 'R')),
    (0x0B0, Action(0x020, 'L (Dashing)')),
    (0x0B4, Action(0x021, 'R (Dashing)')),
    (0x0B8, Action(0x022, 'Land')),
    (0x0BC, Action(0x023, 'JB')),
    (0x0C0, Action(0x024, 'Freeze character (Can be thrown out)')),
    (0x0C4, Action(0x025, 'Transformation Y-cancel')),
    (0x0C8, Action(0x026, 'Hit out of air')),
    (0x0CC, Action(0x027, 'Freeze character (Can be thrown out)')),
    (0x0D0, Action(0x028, 'Intro Animation')),
    (0x0D4, Action(0x029, 'Disable all your attacks except throw')),
    (0x0D8, Action(0x02A, 'Win Animation (Disable all your attacks)')),
    (0x0DC, Action(0x02B, 'Win Animation (Including camera,  softlocks)')),
    (0x0E0, Action(0x02C, 'Win Animation (Including camera,  softlock')),
    (0x0E4, Action(0x02D, 'Missing animation? (softlock)')),
    (0x0E8, Action(0x02E, 'Lose round animation (softlock character)')),
    (0x0EC, Action(0x02F, 'Intro animation? (Can be thrown out,  only throws will work after)')),
    (0x0F0, Action(0x030, 'Crash')),
    (0x0F4, Action(0x031, 'Crash')),
    (0x0F8, Action(0x032, 'Crash')),
    (0x0FC, Action(0x033, 'Crash')),
    (0x100, Action(0x034, 'Crash')),
    (0x104, Action(0x035, 'Do nothing')),
    (0x108, Action(0x036, 'Crash')),
    (0x10C, Action(0x037, 'Crash')),
    (0x110, Action(0x038, 'Crash')),
    (0x114, Action(0x039, 'Getting hit animation')),
    (0x118, Action(0x03A, 'Getting hit animation')),
    (0x11C, Action(0x03B, 'Getting hit animation')),
    (0x120, Action(0x03C, 'Getting hit animation')),
    (0x124, Action(0x03D, 'Getting hit animation')),
    (0x128, Action(0x03E, 'Getting hit animation')),
    (0x12C, Action(0x03F, 'Getting hit animation')),
    (0x130, Action(0x040, 'Getting hit animation')),
    (0x134, Action(0x041, 'Getting hit animation')),
    (0x138, Action(0x042, 'Getting hit animation')),
    (0x13C, Action(0x043, 'Getting hit animation')),
    (0x140, Action(0x044, 'Getting hit animation')),
    (0x144, Action(0x045, 'Getting hit animation')),
    (0x148, Action(0x046, 'Hard knockdown animation')),
    (0x14C, Action(0x047, 'Hard knockdown animation')),
    (0x150, Action(0x048, 'Round loss animation')),
    (0x154, Action(0x049, 'Hard knockdown animation')),
    (0x158, Action(0x04A, 'Hard knockdown animation')),
    (0x15C, Action(0x04B, 'Hit with Special (lose all chakra)')),
    (0x160, Action(0x04C, 'Hit with hiki2 (Sink into the ground and fall from above. Ex, Shika 2X)')),
    (0x164, Action(0x04D, 'Hit with hiki (Sink into the ground and pop out. Ex, Jiraya 2A)')),
    (0x168, Action(0x04E, 'Hit with mato2 (Trapped. Ex, Shino 2A)')),
    (0x16C, Action(0x04F, 'Hit hard')),
    (0x170, Action(0x050, 'Hit and stuck in air (Can be hit out)')),
    (0x174, Action(0x051, 'Hit and stuck in air (Can be hit out)')),
    (0x178, Action(0x052, 'Hit with yoro2 (Feet trapped. Ex, Kidomaru 5A1C)')),
    (0x17C, Action(0x053, 'Hit hard')),
    (0x180, Action(0x054, 'Hit and stuck in air (Can be hit out)')),
    (0x184, Action(0x055, 'Hit and stuck in air (Can be hit out)')),
    (0x188, Action(0x056, 'Hit and stuck in air (Can be hit out)')),
    (0x18C, Action(0x057, 'Hit and stuck in air (Can be hit out)')),
    (0x190, Action(0x058, 'Hit and stuck in air (Can be hit out)')),
    (0x194, Action(0x059, 'Hit and stuck in air (Can be hit out)')),
    (0x198, Action(0x05A, 'Hit and stuck in ground (Can be hit out)')),
    (0x19C, Action(0x05B, 'Hit and stuck in air (Can be hit out)')),
    (0x1A0, Action(0x05C, 'Hit hard')),
    (0x1A4, Action(0x05D, 'Hard knockdown')),
    (0x1A8, Action(0x05E, 'Hit with Furi (Turns opponents around on hit. Leftover from Bloody Roar; not used.)')),
    (0x1AC, Action(0x05F, 'Hit with Furi (Turns opponents around on hit. Leftover from Bloody Roar; not used.)')),
    (0x1B0, Action(0x060, 'Hit and stuck in air (Can be hit out)')),
    (0x1B4, Action(0x061, 'Hard knockdown')),
    (0x1B8, Action(0x062, 'Do nothing')),
    (0x1BC, Action(0x063, 'Do nothing')),
    (0x1C0, Action(0x064, 'Crash')),
    (0x1C4, Action(0x065, 'Crash')),
    (0x1C8, Action(0x066, 'Hard knockdown')),
    (0x1CC, Action(0x067, 'Getting hit')),
    (0x1D0, Action(0x068, 'Getting hit')),
    (0x1D4, Action(0x069, 'Hard knockdown')),
    (0x1D8, Action(0x06A, 'Hard knockdown')),
    (0x1DC, Action(0x06B, 'Guard break')),
    (0x1E0, Action(0x06C, 'Hard knockdown')),
    (0x1E4, Action(0x06D, 'Getting hit')),
    (0x1E8, Action(0x06E, 'Getting hit')),
    (0x1EC, Action(0x06F, 'Hard knockdown')),
    (0x1F0, Action(0x070, 'Hard knockdown')),
    (0x1F4, Action(0x071, 'Getting hit')),
    (0x1F8, Action(0x072, 'Roll forward')),
    (0x1FC, Action(0x073, 'Roll forward')),
    (0x200, Action(0x074, 'Roll backwards')),
    (0x204, Action(0x075, 'Roll right')),
    (0x208, Action(0x076, 'Roll left')),
    (0x20C, Action(0x077, 'Get up')),
    (0x210, Action(0x078, 'Get up roll forward')),
    (0x214, Action(0x079, 'Get up roll forward')),
    (0x218, Action(0x07A, 'Get up roll backwards')),
    (0x21C, Action(0x07B, 'Get up roll right')),
    (0x220, Action(0x07C, 'Get up roll left')),
    (0x224, Action(0x07D, 'Throw break 1')),
    (0x228, Action(0x07E, 'Throw break 1')),
    (0x22C, Action(0x07F, 'Throw break 2')),
    (0x230, Action(0x080, 'Hit hard')),
    (0x234, Action(0x081, 'Hit hard')),
    (0x238, Action(0x082, 'Hit hard')),
    (0x23C, Action(0x083, 'Hit hard')),
    (0x240, Action(0x084, 'Hard knockdown to the left')),
    (0x244, Action(0x085, 'Hard knockdown to the right')),
    (0x248, Action(0x086, 'Getting hit')),
    (0x24C, Action(0x087, 'Getting hit')),
    (0x250, Action(0x088, 'Hard knockdown back')),
    (0x254, Action(0x089, 'Hard knockdown forward')),
    (0x258, Action(0x08A, 'Do nothing')),
    (0x25C, Action(0x08B, 'Do nothing')),
    (0x260, Action(0x08C, 'Hit hard')),
    (0x264, Action(0x08D, 'Tripping')),
    (0x268, Action(0x08E, 'Hard knockdown bounce')),
    (0x26C, Action(0x08F, 'Hard knockdown bounce')),
    (0x270, Action(0x090, 'Hit and stuck in air (Can be hit out)')),
    (0x274, Action(0x091, 'Hit and stuck in air (Can be hit out)')),
    (0x278, Action(0x092, 'Hard knockdown slow bounce')),
    (0x27C, Action(0x093, 'Hard knockdown slow bounce')),
    (0x280, Action(0x094, 'Crash')),
    (0x284, Action(0x095, 'Block low')),
    (0x288, Action(0x096, 'Get up')),
    (0x28C, Action(0x097, 'Guard break low')),
    (0x290, Action(0x098, 'Weird land')),
    (0x294, Action(0x099, 'Weird land')),
    (0x298, Action(0x09A, 'Weird land')),
    (0x29C, Action(0x09B, 'Weird land')),
    (0x2A0, Action(0x09C, 'Weird land')),
    (0x2A4, Action(0x09D, 'Weird land')),
    (0x2A8, Action(0x09E, 'Weird land')),
    (0x2AC, Action(0x09F, 'Weird land')),
    (0x2B0, Action(0x0A0, '5B')),
    (0x2B4, Action(0x0A1, '6B')),
    (0x2B8, Action(0x0A2, '4B')),
    (0x2BC, Action(0x0A3, '2B')),
    (0x2C0, Action(0x0A4, 'DB')),
    (0x2C4, Action(0x0A5, 'DB')),
    (0x2C8, Action(0x0A6, 'Do nothing')),
    (0x2CC, Action(0x0A7, 'Do nothing')),
    (0x2D0, Action(0x0A8, 'Do nothing')),
    (0x2D4, Action(0x0A9, 'Do nothing')),
    (0x2D8, Action(0x0AA, 'Do nothing')),
    (0x2DC, Action(0x0AB, 'Do nothing')),
    (0x2E0, Action(0x0AC, 'Do nothing')),
    (0x2E4, Action(0x0AD, 'Do nothing')),
    (0x2E8, Action(0x0AE, 'Do nothing')),
    (0x2EC, Action(0x0AF, 'Do nothing')),
    (0x2F0, Action(0x0B0, '5A')),
    (0x2F4, Action(0x0B1, '6A')),
    (0x2F8, Action(0x0B2, '4A')),
    (0x2FC, Action(0x0B3, '2A')),
    (0x300, Action(0x0B4, 'DA')),
    (0x304, Action(0x0B5, 'DA')),
    (0x308, Action(0x0B6, 'Do nothing')),
    (0x30C, Action(0x0B7, 'Do nothing')),
    (0x310, Action(0x0B8, 'Do nothing')),
    (0x314, Action(0x0B9, 'Do nothing')),
    (0x318, Action(0x0BA, 'Do nothing')),
    (0x31C, Action(0x0BB, 'Do nothing')),
    (0x320, Action(0x0BC, 'Do nothing')),
    (0x324, Action(0x0BD, 'Do nothing')),
    (0x328, Action(0x0BE, 'Weird land')),
    (0x32C, Action(0x0BF, 'Stuck in air (Can be hit out)')),
    (0x330, Action(0x0C0, 'RKnJ (Ground)')),
    (0x334, Action(0x0C1, 'RKnJ (Air)')),
    (0x338, Action(0x0C2, 'LKnJ')),
    (0x33C, Action(0x0C3, 'ZKnJ incoming')),
    (0x340, Action(0x0C4, 'Do nothing')),
    (0x344, Action(0x0C5, 'Do nothing')),
    (0x348, Action(0x0C6, '5Z outgoing')),
    (0x34C, Action(0x0C7, '4Z incoming')),
    (0x350, Action(0x0C8, '5Z incoming')),
    (0x354, Action(0x0C9, 'Become invisible (revert when hit)')),
    (0x358, Action(0x0CA, 'Z switch')),
    (0x35C, Action(0x0CB, 'ZKnJ outgoing')),
    (0x360, Action(0x0CC, 'Teleport behind opponent')),
    (0x364, Action(0x0CD, 'Do nothing')),
    (0x368, Action(0x0CE, 'Do nothing')),
    (0x36C, Action(0x0CF, '4Z outgoing')),
    (0x370, Action(0x0D0, 'Do nothing')),
    (0x374, Action(0x0D1, 'Do nothing')),
    (0x378, Action(0x0D2, 'Do nothing')),
    (0x37C, Action(0x0D3, 'Do nothing')),
    (0x380, Action(0x0D4, 'Do nothing')),
    (0x384, Action(0x0D5, 'Do nothing')),
    (0x388, Action(0x0D6, 'Do nothing')),
    (0x38C, Action(0x0D7, 'Do nothing')),
    (0x390, Action(0x0D8, 'Do nothing')),
    (0x394, Action(0x0D9, 'Do nothing')),
    (0x398, Action(0x0DA, 'Do nothing')),
    (0x39C, Action(0x0DB, 'Do nothing')),
    (0x3A0, Action(0x0DC, 'Do nothing')),
    (0x3A4, Action(0x0DD, 'Do nothing')),
    (0x3A8, Action(0x0DE, 'Do nothing')),
    (0x3AC, Action(0x0DF, 'Do nothing')),
    (0x3B0, Action(0x0E0, 'JB')),
    (0x3B4, Action(0x0E1, 'JA')),
    (0x3B8, Action(0x0E2, '8B')),
    (0x3BC, Action(0x0E3, '8A')),
    (0x3C0, Action(0x0E4, 'Hit with smoke')),
    (0x3C4, Action(0x0E5, 'Do nothing')),
    (0x3C8, Action(0x0E6, 'Do nothing')),
    (0x3CC, Action(0x0E7, 'Do nothing')),
    (0x3D0, Action(0x0E8, 'Do nothing')),
    (0x3D4, Action(0x0E9, 'Do nothing')),
    (0x3D8, Action(0x0EA, 'Do nothing')),
    (0x3DC, Action(0x0EB, 'Do nothing')),
    (0x3E0, Action(0x0EC, 'Do nothing')),
    (0x3E4, Action(0x0ED, 'Do nothing')),
    (0x3E8, Action(0x0EE, 'Do nothing')),
    (0x3EC, Action(0x0EF, 'Do nothing')),
    (0x3F0, Action(0x0F0, 'Do nothing')),
    (0x3F4, Action(0x0F1, 'Do nothing')),
    (0x3F8, Action(0x0F2, 'Do nothing')),
    (0x3FC, Action(0x0F3, 'Do nothing')),
    (0x400, Action(0x0F4, 'Do nothing')),
    (0x404, Action(0x0F5, 'Do nothing')),
    (0x408, Action(0x0F6, 'Do nothing')),
    (0x40C, Action(0x0F7, 'Do nothing')),
    (0x410, Action(0x0F8, 'Do nothing')),
    (0x414, Action(0x0F9, 'Do nothing')),
    (0x418, Action(0x0FA, 'Do nothing')),
    (0x41C, Action(0x0FB, 'Do nothing')),
    (0x420, Action(0x0FC, 'Do nothing')),
    (0x424, Action(0x0FD, 'Do nothing')),
    (0x428, Action(0x0FE, 'Stuck in air (Can be hit out)')),
    (0x42C, Action(0x0FF, 'Do nothing')),
    (0x430, Action(0x100, 'Do nothing')),
    (0x434, Action(0x101, 'Do nothing')),
    (0x438, Action(0x102, 'Do nothing')),
    (0x43C, Action(0x103, 'Do nothing')),
    (0x440, Action(0x104, 'Do nothing')),
    (0x444, Action(0x105, 'Do nothing')),
    (0x448, Action(0x106, 'Do nothing')),
    (0x44C, Action(0x107, 'Do nothing')),
    (0x450, Action(0x108, 'Do nothing')),
    (0x454, Action(0x109, 'Do nothing')),
    (0x458, Action(0x10A, 'Stuck in air (Can be hit out)')),
    (0x45C, Action(0x10B, 'Do nothing')),
    (0x460, Action(0x10C, 'Do nothing')),
    (0x464, Action(0x10D, 'Do nothing')),
    (0x468, Action(0x10E, 'Do nothing')),
    (0x46C, Action(0x10F, 'Do nothing')),
    (0x470, Action(0x110, 'Do nothing')),
    (0x474, Action(0x111, 'Do nothing')),
    (0x478, Action(0x112, 'Do nothing')),
    (0x47C, Action(0x113, 'Do nothing')),
    (0x480, Action(0x114, 'Do nothing')),
    (0x484, Action(0x115, 'Do nothing')),
    (0x488, Action(0x116, 'Stuck in air (Can be hit out)')),
    (0x48C, Action(0x117, 'Do nothing')),
    (0x490, Action(0x118, 'Do nothing')),
    (0x494, Action(0x119, 'Do nothing')),
    (0x498, Action(0x11A, 'Do nothing')),
    (0x49C, Action(0x11B, 'Do nothing')),
    (0x4A0, Action(0x11C, 'Do nothing')),
    (0x4A4, Action(0x11D, 'Do nothing')),
    (0x4A8, Action(0x11E, 'Do nothing')),
    (0x4AC, Action(0x11F, 'Do nothing')),
    (0x4B0, Action(0x120, 'Stuck in air (Can be hit out)')),
    (0x4B4, Action(0x121, '5X')),
    (0x4B8, Action(0x122, '2X')),
    (0x4BC, Action(0x123, '5X (Transformation)')),
    (0x4C0, Action(0x124, 'Transform')),
    (0x4C4, Action(0x125, '2X (Animation)')),
    (0x4C8, Action(0x126, 'Do nothing (head movement?)')),
    (0x4CC, Action(0x127, 'Do nothing (head movement?)')),
    (0x4D0, Action(0x128, 'Remove character from game')),
    (0x4D4, Action(0x129, '3-Man X #1')),
    (0x4D8, Action(0x12A, '3-Man X #2')),
    (0x4DC, Action(0x12B, '3-Man X #3')),
    (0x4E0, Action(0x12C, '3-Man X #4')),
    (0x4E4, Action(0x12D, '3-Man X #5')),
    (0x4E8, Action(0x12E, '3-Man X #6')),
    (0x4EC, Action(0x12F, '3-Man X #7')),
    (0x4F0, Action(0x130, 'Combo Moves (character-specific)')),
    (0x4F4, Action(0x131, 'Combo Moves (character-specific)')),
    (0x4F8, Action(0x132, 'Combo Moves (character-specific)')),
    (0x4FC, Action(0x133, 'Combo Moves (character-specific)')),
    (0x500, Action(0x134, 'Combo Moves (character-specific)')),
    (0x504, Action(0x135, 'Combo Moves (character-specific)')),
    (0x508, Action(0x136, 'Combo Moves (character-specific)')),
    (0x50C, Action(0x137, 'Combo Moves (character-specific)')),
    (0x510, Action(0x138, 'Combo Moves (character-specific)')),
    (0x514, Action(0x139, 'Combo Moves (character-specific)')),
    (0x518, Action(0x13A, 'Combo Moves (character-specific)')),
    (0x51C, Action(0x13B, 'Combo Moves (character-specific)')),
    (0x520, Action(0x13C, 'Combo Moves (character-specific)')),
    (0x524, Action(0x13D, 'Combo Moves (character-specific)')),
    (0x528, Action(0x13E, 'Combo Moves (character-specific)')),
    (0x52C, Action(0x13F, 'Combo Moves (character-specific)')),
    (0x530, Action(0x140, 'Combo Moves (character-specific)')),
    (0x534, Action(0x141, 'Combo Moves (character-specific)')),
    (0x538, Action(0x142, 'Combo Moves (character-specific)')),
    (0x53C, Action(0x143, 'Combo Moves (character-specific)')),
    (0x540, Action(0x144, 'Combo Moves (character-specific)')),
    (0x544, Action(0x145, 'Combo Moves (character-specific)')),
    (0x548, Action(0x146, 'Combo Moves (character-specific)')),
    (0x54C, Action(0x147, 'Combo Moves (character-specific)')),
    (0x550, Action(0x148, 'Combo Moves (character-specific)')),
    (0x554, Action(0x149, 'Combo Moves (character-specific)')),
    (0x558, Action(0x14A, 'Do nothing')),
    (0x55C, Action(0x14B, 'Do nothing')),
    (0x560, Action(0x14C, 'Do nothing')),
    (0x564, Action(0x14D, 'Do nothing')),
    (0x568, Action(0x14E, 'Do nothing')),
    (0x56C, Action(0x14F, 'Do nothing')),
    (0x570, Action(0x150, 'Do nothing')),
    (0x574, Action(0x151, 'Do nothing')),
    (0x578, Action(0x152, 'Do nothing')),
    (0x57C, Action(0x153, 'Do nothing')),
    (0x580, Action(0x154, 'Do nothing')),
    (0x584, Action(0x155, 'Do nothing')),
    (0x588, Action(0x156, 'Do nothing')),
    (0x58C, Action(0x157, 'Do nothing')),
    (0x590, Action(0x158, 'Do nothing')),
    (0x594, Action(0x159, 'Do nothing')),
    (0x598, Action(0x15A, 'Do nothing')),
    (0x59C, Action(0x15B, 'Do nothing')),
    (0x5A0, Action(0x15C, 'Do nothing')),
    (0x5A4, Action(0x15D, 'Do nothing')),
    (0x5A8, Action(0x15E, 'Do nothing')),
    (0x5AC, Action(0x15F, 'Do nothing')),
    (0x5B0, Action(0x160, 'Do nothing')),
    (0x5B4, Action(0x161, 'Do nothing')),
    (0x5B8, Action(0x162, 'Do nothing')),
    (0x5BC, Action(0x163, 'Do nothing')),
    (0x5C0, Action(0x164, 'Do nothing')),
    (0x5C4, Action(0x165, 'Do nothing')),
    (0x5C8, Action(0x166, 'Do nothing')),
    (0x5CC, Action(0x167, 'Do nothing')),
    (0x5D0, Action(0x168, 'Do nothing')),
    (0x5D4, Action(0x169, 'Do nothing')),
    (0x5D8, Action(0x16A, 'Do nothing')),
    (0x5DC, Action(0x16B, 'Do nothing')),
    (0x5E0, Action(0x16C, 'Do nothing')),
    (0x5E4, Action(0x16D, 'Do nothing')),
    (0x5E8, Action(0x16E, 'Do nothing')),
    (0x5EC, Action(0x16F, 'Do nothing')),
    (0x5F0, Action(0x170, 'Crash')),
    (0x5F4, Action(0x171, 'Crash')),
    (0x5F8, Action(0x172, 'Crash')),
    (0x5FC, Action(0x173, 'Crash')),
    (0x600, Action(0x174, 'Crash')),
    (0x604, Action(0x175, 'Crash')),
    (0x608, Action(0x176, 'Crash')),
    (0x60C, Action(0x177, 'Crash')),
    (0x610, Action(0x178, 'Crash')),
    (0x614, Action(0x179, 'Crash')),
    (0x618, Action(0x17A, 'Crash')),
    (0x61C, Action(0x17B, 'Crash')),
    (0x620, Action(0x17C, 'Crash')),
    (0x624, Action(0x17D, 'Crash')),
    (0x628, Action(0x17E, 'Crash')),
    (0x62C, Action(0x17F, 'Crash')),
    (0x630, Action(0x180, 'Crash')),
    (0x634, Action(0x181, 'Crash')),
    (0x638, Action(0x182, 'Crash')),
    (0x63C, Action(0x183, 'Crash')),
    (0x640, Action(0x184, 'Crash')),
    (0x644, Action(0x185, 'Crash')),
    (0x648, Action(0x186, 'Crash')),
    (0x64C, Action(0x187, 'Crash')),
    (0x650, Action(0x188, 'Crash')),
    (0x654, Action(0x189, 'Crash')),
    (0x658, Action(0x18A, 'Crash')),
    (0x65C, Action(0x18B, 'Crash')),
    (0x660, Action(0x18C, 'Crash')),
    (0x664, Action(0x18D, 'Crash')),
    (0x668, Action(0x18E, 'Crash')),
    (0x66C, Action(0x18F, 'Crash')),
    (0x670, Action(0x190, 'Ground Throw')),
    (0x674, Action(0x191, 'Back Ground Throw')),
    (0x678, Action(0x192, 'Air Throw')),
    (0x67C, Action(0x193, 'Activated X')),
    (0x680, Action(0x194, 'Crash')),
    (0x684, Action(0x195, 'Activated X (Transformation)')),
    (0x688, Action(0x196, 'Activated 2X')),
    (0x68C, Action(0x197, 'Crash')),
    (0x690, Action(0x198, 'Do nothing')),
    (0x694, Action(0x199, 'Do nothing')),
    (0x698, Action(0x19A, 'Do nothing')),
    (0x69C, Action(0x19B, 'Do nothing')),
    (0x6A0, Action(0x19C, 'Do nothing')),
    (0x6A4, Action(0x19D, 'Do nothing')),
    (0x6A8, Action(0x19E, 'Do nothing')),
    (0x6AC, Action(0x19F, 'Do nothing')),
    (0x6B0, Action(0x1A0, 'Do nothing')),
    (0x6B4, Action(0x1A1, 'Do nothing')),
    (0x6B8, Action(0x1A2, 'Do nothing')),
    (0x6BC, Action(0x1A3, 'Do nothing')),
    (0x6C0, Action(0x1A4, 'Do nothing')),
    (0x6C4, Action(0x1A5, 'Do nothing')),
    (0x6C8, Action(0x1A6, 'Do nothing')),
    (0x6CC, Action(0x1A7, 'Do nothing')),
    (0x6D0, Action(0x1A8, 'Do nothing')),
    (0x6D4, Action(0x1A9, 'Do nothing')),
    (0x6D8, Action(0x1AA, 'Do nothing')),
    (0x6DC, Action(0x1AB, 'Do nothing')),
    (0x6E0, Action(0x1AC, 'Do nothing')),
    (0x6E4, Action(0x1AD, 'Do nothing')),
    (0x6E8, Action(0x1AE, 'Do nothing')),
    (0x6EC, Action(0x1AF, 'Do nothing')),
    (0x6F0, Action(0x1B0, 'Do nothing')),
    (0x6F4, Action(0x1B1, 'Do nothing')),
    (0x6F8, Action(0x1B2, 'Do nothing')),
    (0x6FC, Action(0x1B3, 'Do nothing')),
    (0x700, Action(0x1B4, 'Do nothing')),
    (0x704, Action(0x1B5, 'Do nothing')),
    (0x708, Action(0x1B6, 'Do nothing')),
    (0x70C, Action(0x1B7, 'Do nothing')),
    (0x710, Action(0x1B8, 'Do nothing')),
    (0x714, Action(0x1B9, 'Do nothing')),
    (0x718, Action(0x1BA, 'Do nothing')),
    (0x71C, Action(0x1BB, 'Do nothing')),
    (0x720, Action(0x1BC, 'Do nothing')),
    (0x724, Action(0x1BD, 'Do nothing')),
    (0x728, Action(0x1BE, 'Do nothing')),
    (0x72C, Action(0x1BF, 'Do nothing')),
    (0x730, Action(0x1C0, 'Do nothing')),
    (0x734, Action(0x1C1, 'Do nothing')),
    (0x738, Action(0x1C2, 'Do nothing')),
    (0x73C, Action(0x1C3, 'Do nothing')),
    (0x740, Action(0x1C4, 'Do nothing')),
    (0x744, Action(0x1C5, 'Do nothing')),
    (0x748, Action(0x1C6, 'Do nothing')),
    (0x74C, Action(0x1C7, 'Do nothing')),
    (0x750, Action(0x1C8, 'Do nothing')),
    (0x754, Action(0x1C9, 'Do nothing')),
    (0x758, Action(0x1CA, 'Do nothing')),
    (0x75C, Action(0x1CB, 'Do nothing')),
    (0x760, Action(0x1CC, 'Do nothing')),
    (0x764, Action(0x1CD, 'Do nothing')),
    (0x768, Action(0x1CE, 'Do nothing')),
    (0x76C, Action(0x1CF, 'Do nothing')),
    (0x770, Action(0x1D0, 'Activated 3-Man X #1')),
    (0x774, Action(0x1D1, 'Activated 3-Man X #2')),
    (0x778, Action(0x1D2, 'Activated 3-Man X #3')),
    (0x77C, Action(0x1D3, 'Activated 3-Man X #4')),
    (0x780, Action(0x1D4, 'Do nothing')),
    (0x784, Action(0x1D5, 'Activated 3-Man X #5')),
    (0x788, Action(0x1D6, 'Do nothing')),
    (0x78C, Action(0x1D7, 'Do nothing')),
    (0x790, Action(0x1D8, 'Do nothing')),
    (0x794, Action(0x1D9, 'Do nothing')),
    (0x798, Action(0x1DA, 'Do nothing')),
    (0x79C, Action(0x1DB, 'Do nothing')),
    (0x7A0, Action(0x1DC, 'Do nothing')),
    (0x7A4, Action(0x1DD, 'Do nothing')),
    (0x7A8, Action(0x1DE, 'Do nothing')),
    (0x7AC, Action(0x1DF, 'Activated 3-Man X #6')),
    (0x7B0, Action(0x1E0, 'Getting thrown')),
    (0x7B4, Action(0x1E1, 'Getting thrown')),
    (0x7B8, Action(0x1E2, 'Thrown on the ground')),
    (0x7BC, Action(0x1E3, 'Hit by super')),
    (0x7C0, Action(0x1E4, 'Do nothing')),
    (0x7C4, Action(0x1E5, 'Hit by small attack')),
    (0x7C8, Action(0x1E6, 'Hit by super')),
    (0x7CC, Action(0x1E7, 'Do nothing')),
    (0x7D0, Action(0x1E8, 'Do nothing')),
    (0x7D4, Action(0x1E9, 'Do nothing')),
    (0x7D8, Action(0x1EA, 'Do nothing')),
    (0x7DC, Action(0x1EB, 'Do nothing')),
    (0x7E0, Action(0x1EC, 'Do nothing')),
    (0x7E4, Action(0x1ED, 'Do nothing')),
    (0x7E8, Action(0x1EE, 'Do nothing')),
    (0x7EC, Action(0x1EF, 'Do nothing')),
    (0x7F0, Action(0x1F0, 'Do nothing')),
    (0x7F4, Action(0x1F1, 'Do nothing')),
    (0x7F8, Action(0x1F2, 'Do nothing')),
    (0x7FC, Action(0x1F3, 'Do nothing')),
    (0x800, Action(0x1F4, 'Do nothing')),
    (0x804, Action(0x1F5, 'Do nothing')),
    (0x808, Action(0x1F6, 'Do nothing')),
    (0x80C, Action(0x1F7, 'Do nothing')),
    (0x810, Action(0x1F8, 'Do nothing')),
    (0x814, Action(0x1F9, 'Do nothing')),
    (0x818, Action(0x1FA, 'Do nothing')),
    (0x81C, Action(0x1FB, 'Do nothing')),
    (0x820, Action(0x1FC, 'Do nothing')),
    (0x824, Action(0x1FD, 'Do nothing')),
    (0x828, Action(0x1FE, 'Do nothing')),
    (0x82C, Action(0x1FF, 'Do nothing')),
    (0x830, Action(0x200, 'Do nothing')),
    (0x834, Action(0x201, 'Do nothing')),
    (0x838, Action(0x202, 'Do nothing')),
    (0x83C, Action(0x203, 'Do nothing')),
    (0x840, Action(0x204, 'Do nothing')),
    (0x844, Action(0x205, 'Do nothing')),
    (0x848, Action(0x206, 'Do nothing')),
    (0x84C, Action(0x207, 'Do nothing')),
    (0x850, Action(0x208, 'Do nothing')),
    (0x854, Action(0x209, 'Do nothing')),
    (0x858, Action(0x20A, 'Do nothing')),
    (0x85C, Action(0x20B, 'Do nothing')),
    (0x860, Action(0x20C, 'Do nothing')),
    (0x864, Action(0x20D, 'Do nothing')),
    (0x868, Action(0x20E, 'Do nothing')),
    (0x86C, Action(0x20F, 'Do nothing')),
    (0x870, Action(0x210, 'Do nothing')),
    (0x874, Action(0x211, 'Do nothing')),
    (0x878, Action(0x212, 'Do nothing')),
    (0x87C, Action(0x213, 'Do nothing')),
    (0x880, Action(0x214, 'Do nothing')),
    (0x884, Action(0x215, 'Do nothing')),
    (0x888, Action(0x216, 'Do nothing')),
    (0x88C, Action(0x217, 'Do nothing')),
    (0x890, Action(0x218, 'Do nothing')),
    (0x894, Action(0x219, 'Do nothing')),
    (0x898, Action(0x21A, 'Do nothing')),
    (0x89C, Action(0x21B, 'Do nothing')),
    (0x8A0, Action(0x21C, 'Do nothing')),
    (0x8A4, Action(0x21D, 'Do nothing')),
    (0x8A8, Action(0x21E, 'Do nothing')),
    (0x8AC, Action(0x21F, 'Do nothing')),
    (0x8B0, Action(0x220, 'Do nothing')),
    (0x8B4, Action(0x221, 'Do nothing')),
    (0x8B8, Action(0x222, 'Do nothing')),
    (0x8BC, Action(0x223, 'Getting hit by super')),
    (0x8C0, Action(0x224, 'Do nothing')),
    (0x8C4, Action(0x225, 'Getting hit by super')),
    (0x8C8, Action(0x226, 'Do nothing')),
    (0x8CC, Action(0x227, 'Do nothing')),
    (0x8D0, Action(0x228, 'Do nothing')),
    (0x8D4, Action(0x229, 'Do nothing')),
    (0x8D8, Action(0x22A, 'Do nothing')),
    (0x8DC, Action(0x22B, 'Do nothing')),
    (0x8E0, Action(0x22C, 'Do nothing')),
    (0x8E4, Action(0x22D, 'Do nothing')),
    (0x8E8, Action(0x22E, 'Do nothing')),
    (0x8EC, Action(0x22F, 'Do nothing')),
    (0x8F0, Action(0x230, 'Do nothing')),
    (0x8F4, Action(0x231, 'Do nothing')),
    (0x8F8, Action(0x232, 'Do nothing')),
    (0x8FC, Action(0x233, 'Do nothing')),
    (0x900, Action(0x234, 'Do nothing')),
    (0x904, Action(0x235, 'Do nothing')),
    (0x908, Action(0x236, 'Do nothing')),
    (0x90C, Action(0x237, 'Do nothing')),
    (0x910, Action(0x238, 'Do nothing')),
    (0x914, Action(0x239, 'Do nothing')),
    (0x918, Action(0x23A, 'Do nothing')),
    (0x91C, Action(0x23B, 'Do nothing')),
    (0x920, Action(0x23C, 'Do nothing')),
    (0x924, Action(0x23D, 'Do nothing')),
    (0x928, Action(0x23E, 'Do nothing')),
    (0x92C, Action(0x23F, 'Do nothing')),
    (0x930, Action(0x240, 'Do nothing')),
    (0x934, Action(0x241, 'Do nothing')),
    (0x938, Action(0x242, 'Do nothing')),
    (0x93C, Action(0x243, 'Do nothing')),
    (0x940, Action(0x244, 'Do nothing')),
    (0x944, Action(0x245, 'Do nothing')),
    (0x948, Action(0x246, 'Do nothing')),
    (0x94C, Action(0x247, 'Do nothing')),
    (0x950, Action(0x248, 'Do nothing')),
    (0x954, Action(0x249, 'Do nothing')),
    (0x958, Action(0x24A, 'Do nothing')),
    (0x95C, Action(0x24B, 'Do nothing')),
    (0x960, Action(0x24C, 'Do nothing')),
    (0x964, Action(0x24D, 'Do nothing')),
    (0x968, Action(0x24E, 'Do nothing')),
    (0x96C, Action(0x24F, 'Do nothing')),
    (0x970, Action(0x250, 'Do nothing')),
    (0x974, Action(0x251, 'Do nothing')),
    (0x978, Action(0x252, 'Do nothing')),
    (0x97C, Action(0x253, 'Do nothing')),
    (0x980, Action(0x254, 'Do nothing')),
    (0x984, Action(0x255, 'Do nothing')),
    (0x988, Action(0x256, 'Do nothing')),
    (0x98C, Action(0x257, 'Do nothing')),
    (0x990, Action(0x258, 'Do nothing')),
    (0x994, Action(0x259, 'Do nothing')),
    (0x998, Action(0x25A, 'Do nothing')),
    (0x99C, Action(0x25B, 'Do nothing')),
    (0x9A0, Action(0x25C, 'Do nothing')),
    (0x9A4, Action(0x25D, 'Do nothing')),
    (0x9A8, Action(0x25E, 'Do nothing')),
    (0x9AC, Action(0x25F, 'Do nothing'))
])
