"""Module defines AI for Dice Poker

   Dictionary FIGURES_PROBABILITY_MAX_POINTS defines
   figure hitting probability in five dice throw (first element)
   maximum figure points (second element) and remove coefficient (third).
   The lower coefficient the figure is first in queue to be stroke out.
   
   coefficient = figure_probability * figure_max_points
"""


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
                    FIGURES_PROBABILITY_MAX_POINTS):
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


def throw_or_not_and_what(hand: list, results: list, points: dict):

    results_dict = {}
    [results_dict.update({figure: points}) for figure, points in results]
    roll = []

    if 'Five of a kind' in results_dict.keys():
        to_throw = False
        return to_throw, roll

    if 'Four of a kind' in results_dict.keys():
        to_throw = True
        for dice_value in hand:
            if hand.count(dice_value) == 1:
                roll.append(hand.index(dice_value) + 1)

        return to_throw, roll

    if 'Full House' in results_dict.keys():
        to_throw = False
        return to_throw, roll

    if 'All even' in results_dict.keys():
        to_throw = False
        return to_throw, roll

    if 'All odd' in results_dict.keys():
        to_throw = False
        return to_throw, roll

    if 'Large Straight' in results_dict.keys():
        to_throw = False
        return to_throw, roll

    if 'Small Straight' in results_dict.keys():
        to_throw = False
        return to_throw, roll

    if 'Three of a kind' in results_dict.keys():
        to_throw = True
        for dice_value in hand:
            if hand.count(dice_value) == 1:
                roll.append(hand.index(dice_value) + 1)
        return to_throw, roll

    if 'Two Pairs' in results_dict.keys():
        to_throw = True
        for dice_value in hand:
            if hand.count(dice_value) == 1:
                roll.append(hand.index(dice_value) + 1)
        return to_throw, roll

    if 'Pair' in results_dict.keys():
        to_throw = True
        for dice_value in hand:
            if hand.count(dice_value) == 1:
                roll.append(hand.index(dice_value) + 1)
        return to_throw, roll

    else:
        return combinations(hand)

# functions not ready yed
def combinations(hand: list):

    all_combinations = {}

    for num_dices_to_check in range(1,5):

        while num_dices_to_check:

            for dice in range(1, num_dices_to_check):

                pass

