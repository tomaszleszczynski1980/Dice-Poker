# this unit (file) defines functions of DICE POKER game play
from random import randint
from game_pattern_5 import *


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


def check_hand(hand: list, figures_pattern: dict):
    '''this function checks avaiable figures in hand basing on figures pattern'''
    results = []
    sorted_hand = sorted(hand)

    for function in figures_pattern.keys():
        results.extend(figures_pattern[function](sorted_hand))

    return results


def remove_figures_already_got(results: list, points: dict):
    '''this function removes figures which were already scored or stroke out'''
    results_copy = results[:]

    for result in results_copy:
        if points[result[0]] != 0:
            results.remove(result)

    return results


def add_points_strike_figures(results: list, points: dict, to_add = 0, to_strike = ''):
    '''functions adds points or strikes figures depending what is chosen by player
    returns tuple of modified points dict (table) and message'''

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
    podium = []

    for player, points in players_dict.items():
        podium.append((player, sum_points(points)))

    podium.sort(key = lambda x: x[1], reverse = True)

    return podium
