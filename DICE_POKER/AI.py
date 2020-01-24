"""Module defines AI for Dice Poker

   Dictionary FIGURES_PROBABILITY_MAX_POINTS defines
   figure hitting probability in five dice throw (first element)
   maximum figure points (second element) and remove coefficient (third).
   The lower coefficient the figure is first in queue to be stroke out.
   
   coefficient = figure_probability * figure_max_points
"""


# from itertools import product, permutations, compress

FIGURES_PROBABILITY_MAX_POINTS = {'Pair': (0.4630, 12, 5.556),
                                  'Two Pairs': (0.2315, 24, 5.556),
                                  'Three of a kind': (0.1543, 18, 2.7774),
                                  'Small Straight': (0.0309, 15, 0.4635),
                                  'Large Straight': (0.0309, 20, 0.618),
                                  'All even': (0.0313, 30, 0.939),
                                  'All odd': (0.0313, 25, 0.7825),
                                  'Full House': (0.0386, 40, 1.544),
                                  'Four of a kind': (0.0193, 44, 0.8492),
                                  'Five of a kind': (0.0008, 80, 0.0064),
                                  'Chance': (1.000, 30, 14.9999)
                                  }


def get_best_figure(results: list, points: dict,
                    rounds_number: int, rounds_left: int,
                    FIGURES_PROBABILITY_MAX_POINTS) -> tuple:
    """Chooses best figure from hand.

    Choice is based on figure_weight that is count:
    (figure_points / figure_probability) / figure_max_points
    if figure points are more than coefficient (to small points)
    function decides which figure to strike out
    also when results list is empty function strikes out one figure
    decision is based on coefficient (The lower coefficient
    the figure is first in queue to be stroke out).
    """

    add = 0
    remove = ''

    if results:
        choice = {}
        for result_index, result in enumerate(results):
            figure_points = result[1]
            figure_probability = FIGURES_PROBABILITY_MAX_POINTS[result[0]][0]
            figure_max_points = FIGURES_PROBABILITY_MAX_POINTS[result[0]][1]
            coefficient = FIGURES_PROBABILITY_MAX_POINTS[result[0]][2]

            if (figure_points / rounds_left) > round(coefficient / rounds_number):
                figure_weight = (figure_points/figure_probability)/figure_max_points
            else:
                figure_weight = 0

            choice[result_index] = figure_weight

        if sum(choice.values()):
            add = max(choice.items(), key=lambda x: x[1])[0] + 1

    if add == 0:
        choice = {}
        for figure, value in points.items():
            if value == 0:
                choice[figure] = FIGURES_PROBABILITY_MAX_POINTS[figure][2]

        remove = min(choice.items(), key=lambda x: x[1])[0]

    return add, remove


def throw_or_not_and_what(hand: list, results: list) -> list:
    """Re-roll or not to re-roll that is the question.

    Function checks figures available in results list
    and decides if it is worth to re-roll or not.
    """

    roll = []
    results_dict = {}
    [results_dict.update({figure: points}) for figure, points in results]
    NO_REROLL_LIST = ['Full House', 'All even',
                      'All odd', 'Large Straight', 'Small Straight']

    if 'Five of a kind' in results_dict.keys():
        return roll

    if 'Four of a kind' in results_dict.keys():
        for dice_value in hand:
            if hand.count(dice_value) == 1:
                roll.append(hand.index(dice_value))
        return roll

    for figure in NO_REROLL_LIST:
        if figure in results_dict.keys():
            return roll

    for figure in ['Three of a kind', 'Two Pairs']:
        if figure in results_dict.keys():
            for dice_value in hand:
                if hand.count(dice_value) == 1:
                    roll.append(hand.index(dice_value))
            return roll

    # what to re-roll if you have Pair in hand is still not ready.

    if 'Pair' in results_dict.keys():
        for dice_value in hand:
            if hand.count(dice_value) == 1:
                roll.append(hand.index(dice_value))
        return roll

    # and what to do else? if no figures in your hand?

    else:
        roll = [0, 1, 2, 3, 4]
        return roll


# function is not ready yet

all_combinations = {}

def combinations(hand: list, num_dices_to_check=1):

    for num_dices_to_check in range(1,5):

        combinations(hand, num_dices_to_check)
