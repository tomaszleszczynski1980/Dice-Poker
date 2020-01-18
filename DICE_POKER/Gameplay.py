'''module defines functions of DICE POKER game play'''

from random import randint
from game_pattern_5 import *


def sum_points(points_dict: dict):
    '''sums points in points dictionary.

    omitting figures that are stroke out (marked with 'X')
    in fact that are not integers.
    '''

    return sum([points for points in points_dict.values() if type(points) == int])


def dice_throw(number_of_dices: int, dice_size=6):
    '''Throws given number of dice_size dices.

    returns results as a list.
    '''

    result = []
    for i in range(number_of_dices):
        result.append(randint(1, dice_size))

    return result


def hand_throw(hand: list, choice_to_roll=None):
    '''Throws chosen dices from hand.

    input hand, choice_to_roll = index+1 of dices in hand list to be re-thrown
    if choice_to_roll is None throws whole hand
    returns changed hand.
    '''

    if choice_to_roll is None:
        choice_to_roll = range(len(hand))

    new_throw = dice_throw(len(choice_to_roll))

    dice_index_in_new_throw = 0
    for dice_number in choice_to_roll:
        hand[dice_number] = new_throw[dice_index_in_new_throw]
        dice_index_in_new_throw += 1

    return hand


def check_hand(hand: list, figures_pattern: dict):
    '''Checks avaiable figures in hand basing on figures pattern.

    figures_pattern is dict of {figure: name_of_function}
    imported form game_pattern module.
    calls functions from figures_pattern to check figures
    returns list of tuples (figure name, points for figure)
    '''

    results = []
    sorted_hand = sorted(hand)

    for function in figures_pattern.keys():
        results.extend(figures_pattern[function](sorted_hand))

    return results


def remove_figures_already_got(results: list, points: dict):
    '''Removes figures which were already scored or stroke out.

    in players points dict
    returns filtered results
    '''

    results_copy = results[:]
    for result in results_copy:
        if points[result[0]] != 0:
            results.remove(result)

    return results


def add_points_strike_figures(results: list, points: dict, to_add=0, to_strike =''):
    '''Adds points or strikes figures depending what is chosen by player.

    returns tuple of modified points dict (table) and message
    '''

    if 0 < to_add <= len(results):
        points[results[to_add - 1][0]] = results[to_add - 1][1]
        message = f'{results[to_add - 1][0]} for {results[to_add - 1][1]} added'

    elif to_add == 0:
            if to_strike in points.keys():
                if points[to_strike] == 0:
                    points[to_strike] = 'X'
                    message = f'{to_strike} removed'
                else:
                    for item in points.items():
                        if item[1] == 0:
                            message = f'you cannot remove {to_strike}, instead {item[0]} removed'
                            points[item[0]] = 'X'
                            break
            else:
                for item in points.items():
                    if item[1] == 0:
                        message = f'{item[0]} removed'
                        points[item[0]] = 'X'
                        break

    return points, message


def find_winner(players_dict: dict):
    '''Finds winner when game is finished.

    returns sorted list of tuples (players_name, sum_of_players_points).
    '''

    podium = []
    for player, points in players_dict.items():
        podium.append((player, sum_points(points)))

    podium.sort(key=lambda x: x[1], reverse=True)

    return podium
