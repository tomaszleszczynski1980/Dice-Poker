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


points2 = {'Pair': 0,
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

points3 = {'Pair': 0,
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

print('number of players?:')
players_number = int(input())
players_list = []
for x in range(players_number):
    players_list.append (input(f'podaj imie {x+1} gracza: '))

print('\n')
for i in range(players_number):
    print(f'player number {i+1}:', players_list[i])
    
players_dic = {}
for i in range(players_number):
    players_dic.update({players_list[i]: i+1})


Players_account = {}
def starting_bet_value():
    return int(input("Please enter starting cash for all players: "))
    

def bank():
    sbv = starting_bet_value()
    for i in range(players_number):
        Players_account.update({players_list[i] : sbv})
    print(Players_account)

bank()






