from random import randint
from copy import deepcopy
# from os import system


# zmienne globalne


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


# FUNKCJE

# rzuty kostkami


def losowanie_kosci (ilosc_kosci: int):

    wynik = []

    for i in range(ilosc_kosci):

        wynik.append(randint (1,6))

    return wynik


def kolejny_rzut (hand: list, choice: list):

    wynik = losowanie_kosci (len(choice))

    j = 0
    for i in choice:

        hand[choice[j]] = wynik[j]
        j += 1

    return hand


# rozponawanie figur i dodawanie do listy


def check_hand (hand: list, points: dict):
    
    '''this function checks avaiable figures in hand'''

    results = []

    temp = deepcopy(hand)
    temp.sort()

    # sprawdza czy jest poker

    if temp.count(hand[0]) == 5:
        results.append(('Three of a kind', sum(temp[0:3])))


    # sprawdza czy jest kareta

    if (temp.count(temp[0]) >= 4):
        results.append(('Four of a kind', 20 + sum(temp[0:4])))

    elif (temp.count(temp[-1]) >= 4):
        results.append(('Four of a kind', 20 + sum(temp[1:5])))


    # sprawdza czy jest full

    if ((temp.count(temp[0]) == 3) and (temp.count(temp[-1]) == 2)):
        results.append(('Full House', 10 + sum(hand)))

    elif ((temp.count(temp[0]) == 2) and (temp.count(temp[-1]) == 3)):
        results.append(('Full House', 10 + sum(hand)))


    # sprawdza czy jest duży straight

    if temp == [2, 3, 4, 5, 6]:
        results.append(('Large Straight', 20))


    # sprawdza czy jest mały straight

    if temp == [1, 2, 3, 4, 5]:
        results.append(('Small Straight', 15))


    # sprawdza czy wszystkie są parzyste

    if (temp[0] % 2 == 0) and (temp[1] % 2 == 0) and (temp[2] % 2 == 0) \
    and (temp[3] % 2 == 0) and (temp[4] % 2 == 0):
        results.append(('All even', sum(temp)))


    # sprawdza czy wszystkie są nieparzyste

    if (temp[0] % 2 == 1) and (temp[1] % 2 == 1) and (temp[2] % 2 == 1) \
    and (temp[3] % 2 == 1) and (temp[4] % 2 == 1):
        results.append(('All odd', sum(temp)))


    # sprawdza czy jest trójka

    if (temp.count(temp[0]) >= 3):
        results.append(('Three of a kind', sum(temp[0:3])))

    elif (temp.count(temp[-1]) >= 3):
        results.append(('Three of a kind', sum(temp[2:5])))

    elif (temp.count(temp[1]) >= 3):
        results.append(('Three of a kind', sum(temp[1:4])))


    # sprawdza czy są dwie pary

    if ((temp[0] == temp [1])):
        
        if ((temp[2] == temp[3])):
            results.append(('Two Pairs', sum(temp[0:4])))
            
        elif (temp[3] == temp[4]):
            results.append(('Two Pairs', sum(temp) - temp[2]))
            
    elif ((temp[1] == temp[2]) and (temp[3] == temp[4])):
        results.append(('Two Pairs', sum(temp[1:5])))


    # sprawdza czy jest/są pary

    for i in range(1, 7):
        if temp.count(i) >= 2:
           results.append(('Pair', i * 2))


    # szansa zawsze jest dopisuje jej wartość :)

    results.append(('Chance', sum(hand)))


    # wywala z listy rezultatów, te figury, które już zdobyliśmy (mają wartość punktową inną niż 0 w słowniku points

    results_temp = deepcopy(results)

    for z in results_temp:
        if points[z[0]] != 0:
            results.remove(z)

    return results


# dodawanie punktów, usuwanie figur


def adding_points_striking_figures (results: list, points: dict, to_add = 0, to_strike = ''):


    if (0 < to_add <= len(results)):

        points[results[to_add - 1][0]] = results[to_add - 1][1]

    elif (to_add == 0):

            if ((to_strike in points.keys())):

                if (points[to_strike] == 0):

                    points.pop(to_strike)
                    print (to_strike, 'removed')

                else:
                    print('you cannot remove this item!')

                    for item in points.items():
                        if (item[1] == 0):

                            print(item[0], 'removed')
                            points.pop(item[0])
                            break

            else:

                for item in points.items():
                    if (item[1] == 0):

                        print(item[0], 'removed')
                        points.pop(item[0])
                        break

    return points



# PRYMITYWNY INTERFEJS


def prymitywna_wizualka (hand: list):

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


# drukuje tabelę wyników

def tabelka (points_dict: dict):

    print ('+------------------+-------+')

    for i in points_dict.items():

        space_l = 15 - len(i[0])
        space =''

        for j in range(space_l):
            space += ' '


        if (len(str(i[1])) == 1):
            space2 = ' '
        elif (len(str(i[1])) == 2):
            space2 = ''


        if (len(str(sum(points.values()))) == 1):
            space3 = '   '
        elif (len(str(sum(points.values()))) == 2):
            space3 = '   '
        elif (len(str(sum(points.values()))) == 3):
            space3 = '     '

        

        print ('|', i[0], space, '|', i[1], space2, '  |')

    print ('+------------------+-------+')
    print ('|                  |       |')
    print ('| TOTAL            |', str(sum(points.values())) + space3, '|')
    print ('|                  |       |')
    print ('+------------------+-------+') 


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

        tabelka (points)

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
        tabelka (points)

        choice = input('Type figure from points list to delete: ')

        remove = choice
        add = 0


    return add, remove


# główna funkcja gry, na razie brzydka

def main (points: dict, rounds: int):

    hand = [0, 0, 0, 0, 0]

    for loop in range(rounds):

        hand = losowanie_kosci(5)

        print (hand)
        print ('')

        prymitywna_wizualka(hand)

        res = check_hand(hand, points)

        print(res)

        reroll = input_to_reroll()

        if (len(reroll) > 0 and len(reroll) < 6):

            hand = kolejny_rzut(hand, reroll)

            print(hand)
            print('')

            prymitywna_wizualka(hand)

            res = check_hand(hand, points)

            print(res)

        elif (len(reroll) > 0 and len(reroll) >= 6):

            reroll = reroll[0:5]

            hand = kolejny_rzut(hand, reroll)

            print(hand)
            print('')

            prymitywna_wizualka(hand)

            res = check_hand(hand, points)

            print(res)

        elif (len(reroll) == 0):
            pass

        addrem = add_remove_input (res, points)

        add = addrem[0]
        remove = addrem[1]

        points = adding_points_striking_figures (res, points, add, remove)

        print ('')

        tabelka (points)

        print ('')
        stop = input('Press enter to next move, q to quit:')

        if stop == 'q':
            break

    print ('Finished! You gain in total: ', sum(points.values()), 'points')

main (points, 11)
