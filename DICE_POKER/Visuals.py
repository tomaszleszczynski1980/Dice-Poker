"""Defines visual interface for command line (terminal).

   Functions in this module have no return, just print some patterns.
"""

from Gameplay import sum_points


class colors:
    """variables used to get colored/bold/italic/blinking text in Terminal."""

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


class message:
    """Messages for human outputs.

    Defines for different functions to print different kinds of messages.
    """

    def warning(text: str):
        print(f'{colors.RED}{text}{colors.ENDC}')

    def prompt(text: str):
        print(f'{colors.GREEN}{text}{colors.ENDC}')

    def list(text: str):
        print(f'{colors.BLUE}{text}{colors.ENDC}')

    def headlist(text: str):
        print(f'{colors.GREEN}{colors.BOLD}{text}{colors.ENDC}')


def display_players(players_list: list):
    """Prints players names."""

    message.headlist('Players in the game:')
    for player in range(len(players_list)):
        message.list(f'Player number {player + 1}: {players_list[player]}')


def dices_view(hand: list):
    """Visualizes five six-sided dices in text-mode screen."""

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
    print(f'{colors.BOLD}{colors.RED}    1           2           3           4           5     {colors.ENDC}')
    print(' ')


def show_avaiable_figures(results_filtered: list):
    """Shows list of figures available in hand.

    basing on filtered results list
    if empty prints that there is no figures."""

    if len(results_filtered) > 0:
        message.headlist('Figures available in hand:')
        figure_number = 0
        for figure, points in results_filtered:
            print(f'{figure_number + 1}.{colors.BLUE} {figure} for {points} points {colors.ENDC}', end='')
            figure_number += 1

    else:
        message.headlist(f'No figures available in hand')

    print('')


def show_points_table(players_dict: dict):
    """Prints points table for all players."""

    players_names = list(players_dict.keys())
    players_number = len(players_names)
    figures_list = (list(players_dict.values())[0]).keys()

    def hr_line(players_number):
        hr_line = '--------+'
        print('+--------------------+' + hr_line * players_number)

    hr_line(players_number)
    print('|                    |', end='')

    for name in players_names:
        print(name[:6].center(8) + '|', end='')

    print('')
    hr_line(players_number)

    line = 0
    for figure in figures_list:
        print('|', figure.ljust(18), '|', end='')

        for player_points_table in players_dict.values():
            points = list(player_points_table.values())
            print(str(points[line]).center(7), '|', end='')

        print('')
        line += 1

    hr_line(players_number)
    print('| TOTAL              |', end='')

    for player in players_dict.values():
        print(str(sum_points(player)).center(7), '|', end='')

    print('')
    hr_line(players_number)
    print('')


def show_winner(podium: list):
    """Prints winner and other players results."""

    message.prompt(f'The winner is {podium[0][0]} with {podium[0][1]} points')

    if len(podium) > 1:
        message.headlist('Other players:')
        for player, points in podium[1:]:
            message.list(f'{player} with {points} points')

    print('')
    print(f'{colors.BLINK}{colors.RED}Congratulations!!!{colors.ENDC}')
