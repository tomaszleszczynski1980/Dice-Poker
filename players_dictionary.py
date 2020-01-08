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

def sum_points(points_dict: dict):
    '''this functions sums points in points dictionary omitting figures that are stroke out (marked with 'X')'''
    return sum([points for points in points_dict.values() if type(points) == int])

# players dictionary

def make_players_dict(players_list: list, points: dict):
    
    players_dict = {}

    for i in range(len(players_list)):
        players_dict.update({players_list[i]: copy(points)})

    return players_dict


def get_players():   

    players_number = int(input('number of players?: '))

    players_list = []
    for number in range(players_number):
        players_list.append(input(f'Type name of {number + 1} player: '))

    return players_list


def display_players(players_list: list):

    print('Players in the game:')
    for player in range(len(players_list)):
        print(f'player number {player + 1}:', players_list[player])


def test_this_module():
    players_list = get_players()

    print('')

    display_players(players_list)
    players = make_players_dict(players_list, points)

    return players
