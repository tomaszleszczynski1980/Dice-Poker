"""Module defines preparation functions of Dice Poker Game.

    Functions defined in this module prepare the game:
    get number of players, import game patterns, generate points tables (dicts)
    show help file.
"""

from copy import copy


def make_points_dict(figures_pattern: dict) -> dict:
    """Makes points subdict to use the in players dict.

    import figures_pattern from game_pattern file.
    return single points dict
    """

    points = {}
    for key in figures_pattern.keys():
        points[key] = 0

    return points


def make_players_dict(players_list: list, points: dict) -> dict:
    """Makes players_dict main dictionary of the game.

    containing players names as keys and their points dictionaries as values.
    """

    players_dict = {}
    for name in players_list:
        players_dict.update({name: copy(points)})

    return players_dict


def read_help(helpfile='help.txt'):
    """Loads and shows help text from external file."""

    with open(helpfile, 'r', encoding='utf-8') as file:
        return file.read()
