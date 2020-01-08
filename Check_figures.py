def check_hand(hand: list, points: dict):
    '''this function checks avaiable figures in hand in five dice Poker'''

    results = []

    sorted_hand = sorted (hand)


    def is_poker (sorted_hand: list):

        bonus = 50

        if sorted_hand.count(sorted_hand[0]) == 5:
            return ('Five of a kind', sum(sorted_hand) + bonus)


    def is_four (sorted_hand: list):

        bonus = 20

        if (sorted_hand.count(sorted_hand[0]) >= 4):
            return ('Four of a kind', bonus + sum(sorted_hand[0:4]))

        elif (sorted_hand.count(sorted_hand[-1]) >= 4):
            return ('Four of a kind', bonus + sum(sorted_hand[1:5]))


    def is_fullhouse (sorted_hand: list):

        bonus = 10

        if ((sorted_hand.count(sorted_hand[0]) == 3) and (sorted_hand.count(sorted_hand[-1]) == 2)):
            return ('Full House', bonus + sum(sorted_hand))

        elif ((sorted_hand.count(sorted_hand[0]) == 2) and (sorted_hand.count(sorted_hand[-1]) == 3)):
            return ('Full House', bonus + sum(sorted_hand))


    def is_lstraight (sorted_hand: list):

    if sorted_hand == [2, 3, 4, 5, 6]:
        return ('Large Straight', 20)     # large straight is always 20 points


    def is_sstraight (sorted_hand: list):

    if sorted_hand == [1, 2, 3, 4, 5]:
        return ('Small Straight', 15)    # small straight is always 15 points


    def is_even (sorted_hand: list):

    if all([dice_value for dice_value in sorted_hand if dice_value % 2 == 0]):
        return ('All even', sum(sorted_hand))


    def is_odd (sorted_hand: list):

    if all([dice_value for dice_value in sorted_hand if dice_value % 2 != 0]):
        return ('All odd', sum(sorted_hand))

    # checks if is 3 of a kind

    if (temp.count(temp[0]) >= 3):
        results.append(('Three of a kind', sum(temp[0:3])))

    elif (temp.count(temp[-1]) >= 3):
        results.append(('Three of a kind', sum(temp[2:5])))

    elif (temp.count(temp[1]) >= 3):
        results.append(('Three of a kind', sum(temp[1:4])))

    # checks if there are two pairs

    if ((temp[0] == temp[1])):

        if ((temp[2] == temp[3])):
            results.append(('Two Pairs', sum(temp[0:4])))

        elif (temp[3] == temp[4]):
            results.append(('Two Pairs', sum(temp) - temp[2]))

    elif ((temp[1] == temp[2]) and (temp[3] == temp[4])):
        results.append(('Two Pairs', sum(temp[1:5])))

    # checks if is pair or pairs

    for i in range(1, 7):
        if temp.count(i) >= 2:
            results.append(('Pair', i * 2))

    # chance is always :), so adds it to the list results

    results.append(('Chance', sum(hand)))

    # removes from results figures that we already achieved or striked out
    # those figures that have value different than 0 in points dict

    results_temp = results[:]

    for z in results_temp:
        if points[z[0]] != 0:
            results.remove(z)

    return results