"""Module defines preparation functions of Dice Poker Game.

Functions defined in this module prepare the game:
get number of players, import game patterns, generate points tables (dicts)
show help file.
"""

from copy import copy
from pprint import pprint


def make_points_dict(figures_pattern):
    """Makes points subdict to use the in players dict.

    import figures_pattern from game_pattern file.
    return single points dict
    """

    points = {}
    for key in figures_pattern.keys():
        points[key] = 0

    return points


def make_players_dict(players_list, points):
    """Makes players_dict main dictionary of the game.

    containing players names as keys and their points dictionaries as values.
    """

    players_dict = {}
    for name in players_list:
        players_dict.update({name: copy(points)})

    return players_dict


def show_help(helpfile='help.txt'):
    """Loads and shows help text from external file."""

    with open (helpfile, 'r', encoding='utf-8') as file:
        help_content = file.read()

    pprint(help_content)
