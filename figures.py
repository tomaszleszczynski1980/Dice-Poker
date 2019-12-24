def figures(hand):   # dodałem straihty, poprawiłem błąd bo za trójkę nie ma premii 10

    counts = [0] * 7

    for value in hand:
      counts[value] += 1

    print (counts)
      
    #po sprawdzieniu ile razy dane value się powtarza korzysta z tych warunków, nie wiem tylko jak zakodować małego i dużego straighta

    if 5 in counts:
        score = "Five of a kind", 50
    elif 4 in counts:
        score = "Four of a kind", 20
    elif (3 in counts) and (2 in counts):
        score = "Full House", 10
    elif 3 in counts:
        score = "Three of a kind", 0
    elif counts.count(2) == 2:
        score = "Two Pairs", 0
    elif counts.count(2) == 1:
        score = "Pair", 0
    elif counts == [0, 1, 1, 1, 1, 1, 0]:
        score = "Small Straight", 0
    elif counts == [0, 0, 1, 1, 1, 1, 1]:
        score = "Large Straight", 0
    
    else:
      score = "Chance means Nothing", 0
    return score
