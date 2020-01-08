# moduł sprawdzający figury pokera

figures_in_hand = {'pair': 0,
           'two_pairs': 0,
           'three': 0,
           'small_st': 0,
           'large_st': 0,
           'full_house:': 0,
           'four': 0,
           'poker': 0,
           'chance': 0
           }



results = [('pair', 8), ('pair', 6), ('two_pairs', 14)]
results = [('pair', 8), ('pair', 6), ('three', 9), ('full_house', 27)]

def pair (hand: list):

    hand.sort()

    if ((hand[0] == hand [1])) or  



def two_pairs (hand: list):

    hand.sort()

    if ((hand[0] == hand [1])):
        if ((hand[2] == hand[3])):
            results.append(('two_pairs', hand[0] + hand[1] + hand[2] + hand[3]))
        elif (hand[3] == hand[4]):
            results.append(('two_pairs', hand[0] + hand[1] + hand[3] + hand[4]))
    elif ((hand[1] == hand [2]) and (hand[3] == hand[4])):
        results.append(('two_pairs', hand[1] + hand[2] + hand[3] + hand[4]))


def hand_set(hand: list):
    temp = hand
    pair = ([x for x in temp if temp.count(x) > 1 and y.count(x) < 3])
    triple = ([x for x in temp if temp.count(x) == 3])
    four = ([x for x in temp if temp.count(x) == 4])
    str1 = [1, 2, 3, 4, 5]
    str2 = [2, 3, 4, 5, 6]

    if len(pair) == 2:
        print("You have one pair of ", pair[0], ".")
    elif len(pair) == 4:
        pair.sort()
        print("You have two pair of ", pair[0], " and", pair[2], ".")
    elif len(triple) == 3 and len(pair) == 2:
        triple.sort()
        print("You have Full House.", "Three of", triple[0], "and one pair of ", pair[0], ".")
    elif len(triple) == 3 and len(pair) != 2:
        print("You have three kind of", triple[0], ".")
    elif len(four) == 4:
        print("You have four kind of", four[0], ".")
    elif y == str1 or y == str2:
        print("You have a straight", y)
    else:
        print("You have no hand")

from random import randint

# zmienne

hand = [0, 0, 0, 0, 0]

points = {'pair': 0,
           'two_pairs': 0,
           'three': 0,
           'small_st': 0,
           'large_st': 0,
           'full_house:': 0,
           'four': 0,
           'poker': 0,
           'chance': 0
           }

bonus_points = {'pair': 0,
           'two_pairs': 0,
           'three': 0,
           'small_st': 0,
           'large_st': 0,
           'full_house:': 10,
           'four': 20,
           'poker': 50,
           'chance': 0
           }

total = sum(points.values())       # wynik całkowity, suma słownika results

dice = range (1, 7)


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

    choice = input('które kości przerzucamy? (pusty - bez rzutu): ')

    if (choice == '' or choice[0] == ' ' or choice[0] == '0'):

        return hand

    else:

        choice = [(int(n) - 1) for n in choice.split(',')]   # to jest niebezpieczne miejsce w programie
                                                         # jak użytkownik wpisze złe numery kości, to program się sypie
        wynik = losowanie_kosci (len(choice))

        j = 0
        for i in choice:
            hand[choice[j]] = wynik[j]
            j += 1

    return hand

results = []

def two_pairs (hand: list):

    hand.sort()

    if ((hand[0] == hand [1])):
        if ((hand[2] == hand[3])):
            results.append(('two_pairs', hand[0] + hand[1] + hand[2] + hand[3]))
        elif (hand[3] == hand[4]):
            results.append(('two_pairs', hand[0] + hand[1] + hand[3] + hand[4]))
    elif ((hand[1] == hand [2]) and (hand[3] == hand[4])):
        results.append(('two_pairs', hand[1] + hand[2] + hand[3] + hand[4]))


def hand_set(hand):
    temp = hand
    temp.sort()
    pair = ([x for x in temp if temp.count(x) > 1 and hand.count(x) < 3])
    triple = ([x for x in temp if temp.count(x) == 3])
    four = ([x for x in temp if temp.count(x) == 4])
    str1 = [1, 2, 3, 4, 5]
    str2 = [2, 3, 4, 5, 6]
    if len(pair) == 2:
        print("You have one pair of ", pair[0], ".")
    elif len(pair) == 4:
        pair.sort()
        print("You have two pair of ", pair[0], " and", pair[2], ".")
    elif len(triple) == 3 and len(pair) == 2:
        triple.sort()
        print("You have Full House.", "Three of", triple[0], "and one pair of ", pair[3], ".")
    elif len(triple) == 3 and len(pair) != 2:
        print("You have three kind of", triple[0], ".")
    elif len(four) == 4:
        print("You have four kind of", four[0], ".")
    elif hand == str1 or hand == str2:
        print("You have a straight", hand)
    else:
        print("You have no hand")

def figures(hand):

    counts = [0] * 7 #zrobiłem licznik, który tworzy 7 zer, który będzie ściągał value z handa czyli nasze kości, ale w tym liczniku pierwszym argumentem jest 0 dlatego 7, a nie 6
    for value in hand:
      counts[value] += 1
      # counts[value] + 1
#po sprawdzieniu ile razy dane value się powtarza korzysta z tych warunków, nie wiem tylko jak zakodować małego i dużego straighta
    if 5 in counts:
      score = "Five of a kind", 50
    elif 4 in counts:
      score = "Four of a kind", 20
    elif (3 in counts) and (2 in counts):
      score = "Full House", 10
    elif 3 in counts:
      score = "Three of a kind", 10
    elif counts.count(2) == 2:
      score = "Two Pairs", 0
    else:
      score = "Nothing", 0
    return score



hand = losowanie_kosci(5)
print (hand)
hand2 = drugi_rzut(hand)
print (hand2)
print(figures(hand))


