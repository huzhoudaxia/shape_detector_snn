from numpy import uint8

MODE_256 = '256'
MODE_128 = '128'
MODE_64  = '64'
MODE_32  = '32'
MODE_16  = '16'

UP_POLARITY     = 'UP'
DOWN_POLARITY   = 'DOWN'
MERGED_POLARITY = 'MERGED'
POLARITY_DICT   = {UP_POLARITY: uint8(0),
                   DOWN_POLARITY: uint8(1),
                   MERGED_POLARITY: uint8(2),
                   0: UP_POLARITY,
                   1: DOWN_POLARITY,
                   2: MERGED_POLARITY}

OUTPUT_RATE         = 'RATE'
OUTPUT_TIME         = 'TIME'
OUTPUT_TIME_BIN     = 'TIME_BIN'
OUTPUT_TIME_BIN_THR = 'TIME_BIN_THR'

BEHAVE_MICROSACCADE = 'SACCADE'
BEHAVE_ATTENTION    = 'ATTENTION'
BEHAVE_TRAVERSE     = 'TRAVERSE'
BEHAVE_FADE         = 'FADE'

RED   = 'RED'
GREEN = 'GREEN'
BLUE  = 'BLUE'
RGB   = 'RGB'

IMAGE_TYPES = ['png', 'jpeg', 'jpg']
