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
def starting_account():
    return int(input("Please enter starting cash for all players: "))
    

def bank():
    s_acc = starting_account()
    for i in range(players_number):
        Players_account.update({players_list[i] : s_acc})

def entering_bet_value():
    try:
        bet_value = int(input("How much do you want to bet? "))
        return bet_value
    except:
        print("The bet value is invalid")
        entering_bet_value()



bank()
entering_bet_value()





