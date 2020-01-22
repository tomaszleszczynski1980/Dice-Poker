Figures_probability = {'Pair': 0.4630,
                       'Two Pairs': 0.2315,
                       'Three of a kind': 0.1543,
                       'Small Straight': 0.0309,
                       'Large Straight': 0.0309,
                       'All even': 0.0313,
                       'All odd': 0.0313,
                       'Full House': 0.0386,
                       'Four of a kind': 0.0193,
                       'Five of a kind': 0.0008,
                       'Chance': 1.000
                       }

Figures_points = {'Pair': (12, 2, 6.0),
                  'Two Pairs': (24, 4, 14.0),
                  'Three of a kind': (18, 3, 10.5),
                  'Small Straight': (15, 15, 15.0),
                  'Large Straight': (20, 20, 20.0),
                  'All even': (30, 10, 20.0),
                  'All odd': (25, 5, 15.0),
                  'Full House': (40, 15, 27.5),
                  'Four of a kind': (44, 24, 34.0),
                  'Five of a kind': (80, 55, 67.5),
                  'Chance': (30, 5, 17.5)
                  }

def work_function():
    res = {}
    for figure, probability in Figures_probability.items():
        relation = Figures_points[figure][2] / probability
        res[figure] = relation

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
        if len(results) == 1:
            add = 1

        else:
            choice = {}
            for result_index, result in enumerate(results):
                coef = (result[1] / FIGURES_PROBABILITY_MAX_POINTS[result[0]][0]) / FIGURES_PROBABILITY_MAX_POINTS[result[0]][1]
                choice[result_index] = coef

            add = max(choice.items(), key=lambda x: x[1])[0] + 1

    return add, remove

    '''
    else:
        pass
        # WTF_to_strike_out()
    '''
