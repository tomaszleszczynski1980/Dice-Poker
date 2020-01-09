# this unit (file) defines functions of DICE POKER gameplay


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