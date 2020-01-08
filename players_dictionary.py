from copy import copy

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


#players dictionary

def make_players_dict(players_list: list, points: dict):
    
    players_dict = {}

    for i in range(len(players_list)):
        players_dic.update({players_list[i]: copy(points)})

    return players_dict


def get_players():   

    players_number = int(input('number of players?: '))

    players_list = []
    for x in range(players_number):
        players_list.append (input(f'podaj imie {x+1} gracza: '))

    return players_list


def display_players(players_list: list):

    print('Players in the game:')
    for i in range(len(players_list)):
        print(f'player number {i+1}:', players_list[i])


def test_this_module():
    players_list = get_players()

    print ('')

    display_players(players_list)

    players = make_players_dic(players_list, points)

    print (players)
