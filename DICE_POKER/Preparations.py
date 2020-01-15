# this file (unit) defines function that prepare game
from copy import copy
from pprint import pprint


def make_points_dict(figures_pattern: dict):
    '''this function makes points subdict to use the in players dict
    import figures_path from game_pattern file, return as points dict'''
    points = {}
    for key in figures_pattern.keys():
        points[key] = 0

    return points


def make_players_dict(players_list: list, points: dict):
    '''makes players_dict main dictionary of the game containing players names and their points dictionaries (tables)'''
    players_dict = {}
    for name in players_list:
        players_dict.update({name: copy(points)})

    return players_dict


def show_help(helpfile = 'help.txt'):
    '''functions loads and shows help text from external file'''
    with open (helpfile, 'r', encoding = 'utf-8') as file:
        help_content = file.read()

    pprint(help_content)
