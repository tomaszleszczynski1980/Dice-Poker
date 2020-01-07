from random import randint

# global variables


points = {'Pair': 0,
          'Two Pairs': 0,
          'Three of a kind': 0,
          'Small Straight': 0,
          'Large Straight': 0,
          'All even': 0,
          'All odd': 0,
          'Full House': 0,
          'Four of a kind': 0,
          'Five of a kind': 0,
          'Chance': 0
          }


class colors:
    
    WHITE = '\033[97m'
    AQUA = '\033[96m'
    PINK = '\033[95m'
    BLUE = '\033[94m'
    YELLOW = '\033[93m'
    GREEN = '\033[92m'  
    RED = '\033[91m'
    GREY = '\033[90m'

    ENDC = '\033[0m'
    BOLD = '\033[1m'
    WEAK = '\033[2m'
    ITALIC = '\033[3m'
    UNDERLINE = '\033[4m'
    BLINK = '\033[5m'
    BACKGROUND = '\033[7m'


# FUNCTIONS

# dices throwing


def dice_throw (number_of_dices: int): -> list

    result = []

    for i in range(number_of_dices):
        result.append(randint (1,6))

    return result


def another_throw (hand: list, choice = None: list):   # change the name

    # check choice human input
    if choice is None:
        choice = range(len(hand))

    result = dice_throw (len(choice))

    j = 0
    for dice_number in choice:
        hand[dice_number] = result[j]
        j += 1

    return hand


# figures recognation and adding them to list


def check_hand (hand: list, points: dict):
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

    if ((temp[0] == temp [1])):
        
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
        if not points[z[0]]:
            results.remove(z)

    return results


# adding points, deleting (striking) figures


def adding_points_striking_figures (results: list, points: dict, to_add = 0, to_strike = ''):
    '''
    explain how to play
    '''

    if (0 < to_add <= len(results)):

        points[results[to_add - 1][0]] = results[to_add - 1][1]

    elif (to_add == 0):

            if ((to_strike in points.keys())):

                if (points[to_strike] == 0):

                    points[to_strike] = 'X'
                    print (to_strike, 'removed')

                else:
                    print('you cannot remove this item!')

                    for item in points.items():
                        if (item[1] == 0):

                            print(item[0], 'removed')
                            points[item[0]] = 'X'
                            break

            else:

                for item in points.items():
                    if (item[1] == 0):

                        print(item[0], 'removed')
                        points[item[0]] = 'X'
                        break

    return points


# this functions sums points in points dictionary omitting figures that are stroke out (marked with 'X')

def sum_points(points_dict: dict):

    return sum([points for points in points_dict.values() if type(points) == int])

# UGLY USER INTERFACE


def dices_view (hand: list):

    pattern = (('│       │', '│   •   │', '│       │'),  # 1
               ('│ •     │', '│       │', '│     • │'),  # 2
               ('│ •     │', '│   •   │', '│     • │'),  # 3
               ('│ •   • │', '│       │', '│ •   • │'),  # 4
               ('│ •   • │', '│   •   │', '│ •   • │'),  # 5
               ('│ •   • │', '│ •   • │', '│ •   • │')   # 6
               )

    print(' ')

    for x in range(3):

        for i in hand:
            print(pattern[i - 1][x], end='   ')

        print(' ')

    print(' ')
    print('    1     ', '     2     ', '     3     ', '     4     ', '     5     ')
    print(' ')


# prints points table

def points_table (points_dict: dict):

    print ('+--------------------+--------+')

    for i in points_dict.items():

        print ('|', i[0].ljust(18), '|', str(i[1]).center(6), '|')

    print ('+--------------------+--------+')
    print ('|                    |        |')
    print ('| TOTAL              |', str(sum_points(points_dict)).center(6), '|')
    print ('|                    |        |')
    print ('+--------------------+--------+')


# wybór kostek do drugiego rzutu

def input_to_reroll():

    roll = input('choose dices to re-roll? (sep with commas, empty = nothing to re-roll): ')

    if ((roll == '' or roll[0] == ' ' or roll[0] == '0')):

        roll = []

    else:

        try:
            roll = [(int(n) - 1) for n in roll.split(',')]

        except ValueError:
            roll = []

    return roll


# wybór figury, którą zapisujemy do points, albo którą skreślamy z points

def add_remove_input (results: list, points: dict):

    if (len(results) > 0):

        for i in range(len(results)):
            print (str(i + 1) + '.', results[i][0], 'for', results[i][1], 'points', end=', ')

        print ('')

        points_table (points)

        choice = input('Choose figure to add (number) or name figure from points list to delete: ')

        try:
            choice = int(choice)
            if (choice <= len(results)):
                add = choice
            else:
                add = 1

            remove = ''

        except ValueError:
            if (choice in points.keys()):
                remove = choice
                add = 0

            else:
                remove = ''
                add = 1

    else:
        points_table (points)

        choice = input('Type figure from points list to delete: ')

        remove = choice
        add = 0


    return add, remove


# main function, VERY, VERY ... VERY UGLY

def main (points: dict, rounds: int):

    hand = [0, 0, 0, 0, 0]

    for loop in range(rounds):

        hand = dice_throw(5)

        print (hand)
        print ('')

        dices_view (hand)

        res = check_hand(hand, points)

        print(res)

        reroll = input_to_reroll()

        if (len(reroll) > 0 and len(reroll) < 6):

            hand = another_throw(hand, reroll)

            print(hand)
            print('')

            dices_view (hand)

            res = check_hand(hand, points)

            print(res)

        elif (len(reroll) > 0 and len(reroll) >= 6):

            reroll = reroll[0:5]

            hand = another_throw(hand, reroll)

            print(hand)
            print('')

            dices_view (hand)

            res = check_hand(hand, points)

            print(res)

        elif (len(reroll) == 0):
            pass

        addrem = add_remove_input (res, points)

        add = addrem[0]
        remove = addrem[1]

        points = adding_points_striking_figures (res, points, add, remove)

        print ('')

        points_table (points)

        print ('')
        stop = input('Press enter to next move, q to quit:')

        if stop == 'q':
            break

    print ('Finished! You gain in total: ', sum_points(points), 'points')

main (points, 11)
