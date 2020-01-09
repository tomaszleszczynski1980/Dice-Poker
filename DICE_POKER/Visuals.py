# from Gameplay import sum_points

def sum_points(points_dict: dict):
    '''this functions sums points in points dictionary omitting figures that are stroke out (marked with 'X')'''
    return sum([points for points in points_dict.values() if type(points) == int])

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


def display_players(players_list: list):

    print('Players in the game:')
    for player in range(len(players_list)):
        print(f'Player number {player + 1}:', players_list[player])


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


def show_points_table(players_dict: dict, figures_pattern: dict):

    players_names = list(players_dict.keys())
    players_number = len(players_names)

    def hr_line(players_number):
        hr_line = '--------+'
        print('+--------------------+' + hr_line * players_number)

    hr_line(players_number)
    print('|                    |', end ='')

    for name in players_names:
        print(name[:6].center(8) + '|', end = '')

    print('')
    hr_line(players_number)

    line = 0
    for figure in figures_pattern.keys():
        print('|', figure.ljust(18), '|', end ='')

        for player_points_table in players_dict.values():
            points = list(player_points_table.values())
            print(str(points[line]).center(7), '|', end ='')

        print('')
        line += 1

    hr_line(players_number)
    print('| TOTAL              |', end='')

    for player in players_dict.values():
        print(str(sum_points(player)).center(7), '|', end = '')

    print('')
    hr_line(players_number)
