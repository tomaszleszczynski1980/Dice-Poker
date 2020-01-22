"""Below dictionary defines figure occurance probability in five dice throw,
   maximum figures points and remove coefficient.
   The lower coefficient is the figure is first in queue to be stroke out.
   
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
                                  'Chance': (1.000, 30, 30)
                                  }



def get_best_figure(results: list, points: dict,
                    FIGURES_PROBABILITY_MAX_POINTS):
    """Chooses best figure from hand"""

    add = 0
    remove = ''

    if results:
        choice = {}
        for result_index, result in enumerate(results):
            figure_points = result[1]
            figure_probability = FIGURES_PROBABILITY_MAX_POINTS[result[0]][0]
            figure_max_points = FIGURES_PROBABILITY_MAX_POINTS[result[0]][1]

            if figure_points > round(figure_probability * figure_max_points):
                coef = (figure_points / figure_probability) / figure_max_points
            else:
                coef = 0

            choice[result_index] = coef

        if sum(choice.values()):
            add = max(choice.items(), key=lambda x: x[1])[0] + 1

    if add == 0:
        choice = {}
        for figure, value in points.items():
            if value == 0:
                choice[figure] = FIGURES_PROBABILITY_MAX_POINTS[figure][2]

        remove = min(choice.items(), key=lambda x: x[1])[0]

    return add, remove

