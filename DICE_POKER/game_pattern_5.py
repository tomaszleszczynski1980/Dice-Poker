"""module for Dice Poker Game that defines figgures patterns.

   defines functions that find figures in hands of five six-sided dices.
   each function returns a list of tuples (figure_name, figure_value)
   if figure(s) is present
   if not returns empty list.
   figures_pattern dictionary defines figures names (keys)
   and name of function (values) that checks if this figure is in hand.
   figures_pattern is also used to built points dicts.
"""


def is_five(sorted_hand: list):
    bonus = 50

    if sorted_hand.count(sorted_hand[0]) == 5:
        return [('Five of a kind', sum(sorted_hand) + bonus)]
    else:
        return []


def is_four(sorted_hand: list):
    bonus = 20

    if sorted_hand.count(sorted_hand[0]) >= 4:
        return [('Four of a kind', bonus + sum(sorted_hand[0:4]))]
    elif sorted_hand.count(sorted_hand[-1]) >= 4:
        return [('Four of a kind', bonus + sum(sorted_hand[1:5]))]
    else:
        return []


def is_full_house(sorted_hand: list):
    bonus = 10

    if (sorted_hand.count(sorted_hand[0]) == 3) and (sorted_hand.count(sorted_hand[-1]) == 2):
        return [('Full House', bonus + sum(sorted_hand))]
    elif (sorted_hand.count(sorted_hand[0]) == 2) and (sorted_hand.count(sorted_hand[-1]) == 3):
        return [('Full House', bonus + sum(sorted_hand))]
    else:
        return []


def is_odd(sorted_hand: list):
    if (sorted_hand[0] % 2 == 1) and (sorted_hand[1] % 2 == 1) and (sorted_hand[2] % 2 == 1) \
            and (sorted_hand[3] % 2 == 1) and (sorted_hand[4] % 2 == 1):
        return [('All odd', sum(sorted_hand))]
    else:
        return []


def is_even(sorted_hand: list):
    if (sorted_hand[0] % 2 == 0) and (sorted_hand[1] % 2 == 0) and (sorted_hand[2] % 2 == 0) \
            and (sorted_hand[3] % 2 == 0) and (sorted_hand[4] % 2 == 0):
        return [('All even', sum(sorted_hand))]
    else:
        return []


def is_l_straight(sorted_hand: list):
    if sorted_hand == [2, 3, 4, 5, 6]:
        return [('Large Straight', 20)]  # large straight is always 20 points
    else:
        return []


def is_s_straight(sorted_hand: list):
    if sorted_hand == [1, 2, 3, 4, 5]:
        return [('Small Straight', 15)]  # small straight is always 15 points
    else:
        return []


def is_three(sorted_hand: list):
    if sorted_hand.count(sorted_hand[0]) >= 3:
        return [('Three of a kind', sum(sorted_hand[0:3]))]
    elif sorted_hand.count(sorted_hand[-1]) >= 3:
        return [('Three of a kind', sum(sorted_hand[2:5]))]
    elif sorted_hand.count(sorted_hand[1]) >= 3:
        return [('Three of a kind', sum(sorted_hand[1:4]))]
    else:
        return []


def is_2pairs(sorted_hand: list):
    if sorted_hand[0] == sorted_hand[1]:
        if sorted_hand[2] == sorted_hand[3]:
            return [('Two Pairs', sum(sorted_hand[0:4]))]
        elif sorted_hand[3] == sorted_hand[4]:
            return [('Two Pairs', sum(sorted_hand) - sorted_hand[2])]
        else:
            return []
    elif (sorted_hand[1] == sorted_hand[2]) and (sorted_hand[3] == sorted_hand[4]):
        return [('Two Pairs', sum(sorted_hand[1:5]))]
    else:
        return []


def is_pair(sorted_hand: list):
    pairs_list = []

    for dice_value in range(1, 6 + 1):
        if sorted_hand.count(dice_value) >= 2:
            pairs_list.append(('Pair', dice_value * 2))

    return pairs_list


def is_chance(sorted_hand: list):
    return [('Chance', sum(sorted_hand))]


figures_pattern = {'Pair': is_pair,
                   'Two Pairs': is_2pairs,
                   'Three of a kind': is_three,
                   'Small Straight': is_s_straight,
                   'Large Straight': is_l_straight,
                   'All even': is_even,
                   'All odd': is_odd,
                   'Full House': is_full_house,
                   'Four of a kind': is_four,
                   'Five of a kind': is_five,
                   'Chance': is_chance
                   }
