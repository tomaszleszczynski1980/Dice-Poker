# musimy stworzyć listę paternów, którą kość przerzucamy, a którą nie.
# import Gameplay

from itertools import permutations, product


def make_key(number_of_dices=5):

    keys_list = []
    for bit in (bin(x) for x in range(0, 2 ** number_of_dices)):
        key = str(bit)[2:].zfill(number_of_dices)
        keys_list.append(tuple([int(char) for char in key]))

    return keys_list


# for key in keys_list:

def check_key_for_combinations(key: tuple, hand: list):

    vario_hand = hand[:]
    hands_combinations = []

    for dice_index, throw_or_not in enumerate(key):
        if throw_or_not:
            vario_hand[dice_index] = [dice_value for dice_value in range(1, 7)]  # if dice_value != hand[dice_index]]
        else:
            vario_hand[dice_index] = [vario_hand[dice_index]] * 6                # 5

