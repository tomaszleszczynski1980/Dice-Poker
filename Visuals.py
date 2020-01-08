class colors:
    '''variables used to get colored/bold/italic/u-lined/blinking text in Terminal'''
    WHITE = '\033[97m'
    AQUA = '\033[96m'
    PINK = '\033[95m'
    BLUE = '\033[94m'
    YELLOW = '\033[93m'
    GREEN = '\033[92m'
    RED = '\033[91m'
    GREY = '\033[90m'

    ENDC = '\033[0m'
    BOLD = '\033[1m'
    WEAK = '\033[2m'
    ITALIC = '\033[3m'
    UNDERLINE = '\033[4m'
    BLINK = '\033[5m'
    BACKGROUND = '\033[7m'


def dices_view(hand: list):
    '''this function visualizes five cube-dices in text-mode screen (terminal)'''

    pattern = (('│       │', '│   •   │', '│       │'),  # 1
               ('│ •     │', '│       │', '│     • │'),  # 2
               ('│ •     │', '│   •   │', '│     • │'),  # 3
               ('│ •   • │', '│       │', '│ •   • │'),  # 4
               ('│ •   • │', '│   •   │', '│ •   • │'),  # 5
               ('│ •   • │', '│ •   • │', '│ •   • │')   # 6
               )

    print(' ')

    for row in range(3):
        for dice_value in hand:
            print(pattern[dice_value - 1][row], end='   ')

        print(' ')

    print(' ')
    print('    1     ', '     2     ', '     3     ', '     4     ', '     5     ')
    print(' ')


def show_points_table(points_dict: dict):    # funkcja nie gotowa!!!!!
    '''this function prints table of points'''

    print('+--------------------+--------+')

    for i in points_dict.items():

        print('|', i[0].ljust(18), '|', str(i[1]).center(6), '|')

    print('+--------------------+--------+')
    print('|                    |        |')
    print('| TOTAL              |', str(sum_points(points_dict)).center(6), '|')
    print('|                    |        |')
    print('+--------------------+--------+')

