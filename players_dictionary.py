
# global variables
    #players dictionary
    
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
    #players_dic = players_dic + {players_list[i]: i}
    players_dic.update({players_list[i]: i+1})
