def is_five(sorted_hand: list):
    bonus = 50

    if sorted_hand.count(sorted_hand[0]) == 5:
        return list(('Five of a kind', sum(sorted_hand) + bonus))


def is_four(sorted_hand: list):
    bonus = 20

    if (sorted_hand.count(sorted_hand[0]) >= 4):
        return list(('Four of a kind', bonus + sum(sorted_hand[0:4])))

    elif (sorted_hand.count(sorted_hand[-1]) >= 4):
        return list(('Four of a kind', bonus + sum(sorted_hand[1:5])))


def is_fullhouse(sorted_hand: list):
    bonus = 10

    if ((sorted_hand.count(sorted_hand[0]) == 3) and (sorted_hand.count(sorted_hand[-1]) == 2)):
        return list(('Full House', bonus + sum(sorted_hand)))

    elif ((sorted_hand.count(sorted_hand[0]) == 2) and (sorted_hand.count(sorted_hand[-1]) == 3)):
        return list(('Full House', bonus + sum(sorted_hand)))


def is_odd(sorted_hand: list):
    if all([dice_value for dice_value in sorted_hand if dice_value % 2 != 0]):
        return list(('All odd', sum(sorted_hand)))


def is_even(sorted_hand: list):
    if all([dice_value for dice_value in sorted_hand if dice_value % 2 == 0]):
        return list(('All even', sum(sorted_hand)))


def is_lstraight(sorted_hand: list):
    if sorted_hand == [2, 3, 4, 5, 6]:
        return list(('Large Straight', 20))  # large straight is always 20 points


def is_sstraight(sorted_hand: list):
    if sorted_hand == [1, 2, 3, 4, 5]:
        return list(('Small Straight', 15))  # small straight is always 15 points


def is_three(sorted_hand: list):
    if (sorted_hand.count(sorted_hand[0]) >= 3):
        return list(('Three of a kind', sum(sorted_hand[0:3])))

    elif (sorted_hand.count(sorted_hand[-1]) >= 3):
        return list(('Three of a kind', sum(sorted_hand[2:5])))

    elif (sorted_hand.count(sorted_hand[1]) >= 3):
        return list(('Three of a kind', sum(sorted_hand[1:4])))


def is_2pairs(sorted_hand: list):
    if ((sorted_hand[0] == sorted_hand[1])):

        if ((sorted_hand[2] == sorted_hand[3])):
            return list(('Two Pairs', sum(sorted_hand[0:4])))

        elif (sorted_hand[3] == sorted_hand[4]):
            return list(('Two Pairs', sum(sorted_hand) - sorted_hand[2]))

    elif ((sorted_hand[1] == sorted_hand[2]) and (sorted_hand[3] == sorted_hand[4])):
        return list(('Two Pairs', sum(sorted_hand[1:5])))


def is_pair(sorted_hand: list):
    pairs_list = []

    for dice_value in range(1, 6 + 1):
        if sorted_hand.count(dice_value) >= 2:
            pairs_list.append(('Pair', dice_value * 2))

    return pairs_list


def is_chance(sorted_hand: list):
    return list(('Chance', sum(sorted_hand)))


figures_pattern = {'Pair': is_pair,
                   'Two Pairs': is_2pairs,
                   'Three of a kind': is_three,
                   'Small Straight': is_sstraight,
                   'Large Straight': is_lstraight,
                   'All even': is_even,
                   'All odd': is_odd,
                   'Full House': is_fullhouse,
                   'Four of a kind': is_four,
                   'Five of a kind': is_five,
                   'Chance': is_chance
                   }


# following function calls all the functions defined above according to given figures pattern

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
