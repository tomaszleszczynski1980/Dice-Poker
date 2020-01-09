# to jest własciwie nowy brudnopis

def is_in(argument):

    if 5 in argument:

        return (('poker', 5))

a = [('Trójka', 9), ('Para', 6), ('Trójka', 9)]

a.append(is_in([4, 5]))
print (a)

a.append(is_in([4, 4]))
print (a)

a = set(a)

if None in a:
    a.remove(None)

print (a)




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



