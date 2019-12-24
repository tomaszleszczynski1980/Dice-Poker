from random import randint
from os import system
from copy import deepcopy


# zmienne

hand = [0, 0, 0, 0, 0]


points = {'Pair': 0,
           'Two Pairs': 0,
           'Three of a kind': 0,
           'Small Straight': 0,
           'Large Straight': 0,
           'Full House': 0,
           'Four of a kind': 0,
           'Five of a kind': 0,
           'Chance': 0
           }



# funkcje

def losowanie_kosci (ilosc_kosci: int):

    wynik = []

    if (1 <= ilosc_kosci <= 5):

        for i in range(ilosc_kosci):

            wynik.append(randint (1,6))

    else:
        print ('liczba kości musi być od 1 do 5')

    return wynik


def drugi_rzut (hand: list):

    choice = input('choose dices to re-roll? (sep with commas, empty = nothing to re-roll): ')

    if (choice == '' or choice[0] == ' ' or choice[0] == '0'):

        return hand

    else:

        choice = [(int(n) - 1) for n in choice.split(',')]

        wynik = losowanie_kosci (len(choice))

        j = 0
        for i in choice:

            hand[choice[j]] = wynik[j]
            j += 1

    return hand


# rozponawanie figur i dodawanie do listy


def check_hand (hand: list, points: dict):

    results = []

    temp = deepcopy(hand)
    temp.sort()

    if temp.count(hand[0]) == 5:
        results.append(('Five of a kind', 50 + sum(hand)))
        

    if (temp.count(temp[0]) >= 4):
        results.append(('Four of a kind', 20 + sum(temp[0:4])))

    elif (temp.count(temp[-1]) >= 4):
        results.append(('Four of a kind', 20 + sum(temp[1:5])))



    if ((temp.count(temp[0]) == 3) and (temp.count(temp[-1]) == 2)):
        results.append(('Full House', 10 + sum(hand)))

    elif ((temp.count(temp[0]) == 2) and (temp.count(temp[-1]) == 3)):
        results.append(('Full House', 10 + sum(hand)))


    if temp == [2, 3, 4, 5, 6]:
        results.append(('Large Straight', 20))


    if temp == [1, 2, 3, 4, 5]:
        results.append(('Small Straight', 15))


    if (temp.count(temp[0]) >= 3):
        results.append(('Three of a kind', sum(temp[0:3])))

    elif (temp.count(temp[-1]) >= 3):
        results.append(('Three of a kind', sum(temp[2:5])))

    elif (temp.count(temp[1]) >= 3):
        results.append(('Three of a kind', sum(temp[1:4])))


    if ((temp[0] == temp [1])):
        
        if ((temp[2] == temp[3])):
            results.append(('Two Pairs', sum(temp[0:4])))
            
        elif (temp[3] == temp[4]):
            results.append(('Two Pairs', sum(temp) - temp[2]))
            
    elif ((temp[1] == temp[2]) and (temp[3] == temp[4])):
        results.append(('Two Pairs', sum(temp[1:5])))


    for i in range(1, 7):
        if temp.count(i) >= 2:
           results.append(('Pair', i * 2))


    results.append(('Chance', sum(hand)))   

    results_temp = deepcopy(results)

    for z in results_temp:
        if points[z[0]] != 0:
            results.remove(z)

    return results


# mechanizm gry     

def prymitywna_wizualka (hand: list):

    pattern = (('     ','  •  ','     '),     #1
               ('•    ','     ','    •'),     #2
               ('•    ','  •  ','    •'),     #3
               ('•   •','     ','•   •'),     #4
               ('•   •','  •  ','•   •'),     #5
               ('•   •','•   •','•   •')      #6
               )
  

    print (' ')

    for x in range(3):

        for i in hand:

               print (pattern[i-1][x], end='    ')

        print (' ')

    print (' ')
    print (' 1  ', '  2  ', '  3  ', '  4  ', '  5  ')
    print (' ')


def adding_points (results: list, points: dict):

    for i in range(len(results)):
        print (str(i + 1) + '.', results[i][0], 'for', results[i][1], 'points', end=', ')


    choice = int(input('Choose figure (or 0 to strike out): '))

    if (0 < choice <= len(results)):

        points[results[choice - 1][0]] = results[choice - 1][1]


    elif (choice == 0):

        striking = True

        while striking == True:

            print (points)
            strike = input('which figure to strike out (give name): ')

            if ((strike in points.keys())):

                if (points[strike] == 0):

                    points.pop(strike)
                    print (strike, 'removed')
                    striking = False
                    

                else:
                    print ('you cannot strike out this figure')

            else:
                print ('given figure name is invalid')

    return points

  

# pętla gry

for loop in range(9):

    hand = losowanie_kosci(5)

    print (hand)
    print ('')

    prymitywna_wizualka(hand)

    print(check_hand(hand, points))

    hand = drugi_rzut(hand)

  
    # system ('clear')

    print (hand)
    print ('')

    prymitywna_wizualka(hand)

    res = check_hand(hand, points)

    print ('')
    print(res)

    points = adding_points (res, points)

    print ('')
    print (points)

    print ('you have in total: ', sum(points.values()))

    print ('')
    stop = input('press enter to next move, q then enter to quit:')

    if stop == 'q':
        break

print ('you have in total: ', sum(points.values()))


    

