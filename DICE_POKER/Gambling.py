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
    
players_dict = {}
for i in range(players_number):
    players_dict.update({players_list[i]: i+1})



Players_account = {}
def starting_account():
    return int(input("Please enter starting cash for all players: "))
    

def bank():
    s_acc = starting_account()
    for i in range(players_number):
        Players_account.update({players_list[i] : s_acc})
    print(Players_account)

def entering_bet_value():
    try:
        bet_value = int(input("How much do you want to bet?: "))
        return bet_value
    except:
        print("The bet value is invalid")
        entering_bet_value()

def betting(Stakes: int):
    bet_value = entering_bet_value()
    for i in Players_account:
        Players_account[i] -= bet_value
        Stakes += bet_value
    return Stakes


def raise_bet(Stakes):
    for k in Players_account:
        raise_bet_input = input("Do you wish to raise the bet? (yes/no): ")
        if raise_bet_input == 'yes':
            raising(Stakes)
            break

def call_input():
    call = input("Do you want to call the bet?: ")
    return call
        
def raising(Stakes: int):
    raise_bet_value = input("By how much you want to raise the stakes?: ")
    for f in Players_account:
        print(f) 
        call = input("Do you want to call the bet?: ")
        if call == 'yes':   
            Players_account[f] -= int(raise_bet_value)
            Stakes += int(raise_bet_value)
            return Stakes
            print(Players_account)
        if call == 'no':
            play = False
"""
def sum_dicts(players_dict: dict):
    return [sum(players_dict['Players'][i].values()) for i in players_dict['Players']]

def compare():
    
    players = sum_dicts(players_dict)
    winner = players[0]
    for i in players:
        if i  > winner:
            winner = i
"""
    
def find_winner(players_dict: dict):
    podium = []

    for player, points in players_dict.items():
        podium.append((player, points))

    podium.sort(key = lambda x: x[1], reverse = True)

    print(podium)

    return podium
    


    
    



        



        




bank()
betting(Stakes)
raise_bet(Stakes)
Stakes_xd(bet_value)
find_winner(players_dict)
print(Stakes)











