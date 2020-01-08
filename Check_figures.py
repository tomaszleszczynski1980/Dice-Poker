def check_hand(hand: list, points: dict):
    '''this function checks avaiable figures in hand in five dice Poker'''

    results = []

    temp = hand[:]
    temp.sort()

    # checks if is poker (5 of a kind)

    if temp.count(hand[0]) == 5:
        results.append(('Five of a kind', sum(temp) + 50))

    # checks if is 4 of a kind

    if (temp.count(temp[0]) >= 4):
        results.append(('Four of a kind', 20 + sum(temp[0:4])))

    elif (temp.count(temp[-1]) >= 4):
        results.append(('Four of a kind', 20 + sum(temp[1:5])))

    # checks if is fullhouse

    if ((temp.count(temp[0]) == 3) and (temp.count(temp[-1]) == 2)):
        results.append(('Full House', 10 + sum(hand)))

    elif ((temp.count(temp[0]) == 2) and (temp.count(temp[-1]) == 3)):
        results.append(('Full House', 10 + sum(hand)))

    # checks if is large straight

    if temp == [2, 3, 4, 5, 6]:
        results.append(('Large Straight', 20))

    # checks if is small straight

    if temp == [1, 2, 3, 4, 5]:
        results.append(('Small Straight', 15))

    # checks if is all even

    if (temp[0] % 2 == 0) and (temp[1] % 2 == 0) and (temp[2] % 2 == 0) \
            and (temp[3] % 2 == 0) and (temp[4] % 2 == 0):
        results.append(('All even', sum(temp)))

    # checks if is all odd

    if (temp[0] % 2 == 1) and (temp[1] % 2 == 1) and (temp[2] % 2 == 1) \
            and (temp[3] % 2 == 1) and (temp[4] % 2 == 1):
        results.append(('All odd', sum(temp)))

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