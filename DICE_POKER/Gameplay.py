# this unit (file) defines functions of DICE POKER gameplay
from random import randint
from copy import copy


def make_points_dict(figures_pattern: dict):
    '''this function makes points subdict to use the in players dict
    import figures_path from game_pattern file, return as points dict'''
    for key in figures_pattern.keys():
        figures_pattern[key] = 0

    return figures_pattern


def make_players_dict(players_list: list, points: dict):
    players_dict = {}

    for i in range(len(players_list)):
        players_dict.update({players_list[i]: copy(points)})

    return players_dict


def check_hand(hand: list, figures_pattern: dict):
    '''this function checks avaiable figures in hand basing on figures pattern'''
    results = []
    sorted_hand = sorted(hand)

    for function in figures_pattern.values():
        results.extend(function(sorted_hand))

    return results


def remove_figures_already_got(results: list, points: dict):
    '''this function removes figures which were already scored or stroke out'''
    results_copy = results[:]

    for result in results_copy:
        if points[result[0]] != 0:
            results.remove(result)

    return results


def sum_points(points_dict: dict):
    '''this functions sums points in points dictionary omitting figures that are stroke out (marked with 'X')'''
    return sum([points for points in points_dict.values() if type(points) == int])


def dice_throw(number_of_dices: int, dice_size = 6):
    '''this function throws given number of dice_size dices and returns results as a list, default 6-side dice is set'''
    result = []

    for i in range(number_of_dices):
        result.append(randint (1, dice_size))

    return result


def hand_throw(hand: list, choice_to_roll = None):
    '''this function throws chosen dices from hand if choice_to_roll is None throws whole hand'''

    if choice_to_roll is None:
        choice_to_roll = range(len(hand))

    result = dice_throw(len(choice_to_roll))

    j = 0
    for dice_number in choice_to_roll:
        hand[dice_number] = result[j]
        j += 1

    return hand
