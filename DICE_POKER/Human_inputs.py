''' Module contains input functions from human player'''

def wait_for_key(quit='q'):
    '''waits for enter/return key.

    in fact any input
    inputting quit value, exits program.
    '''

    key = input('press enter/return key')
    if key == quit:
        exit()


def get_players(players_limit = 5):
    '''Gets number of human players, and their names.

    returns list of players names
    if ValueError or wrong numbers of players calls self again.
    '''

    try:
        players_number = int(input('Enter number of players: '))
    except ValueError:
        print('number must be integer')
        return get_players()

    if 0 < players_number <= players_limit:
        players_list = []
        for number in range(players_number):
            players_list.append(input(f'Enter name of {number + 1} player: '))

    elif players_number > players_limit:
        print(f'too many players. Specify maximum {players_number}')
        return get_players()

    else:
        print('at least one player is needed')
        return get_players()

    return players_list


def get_throws():
    '''Asks human player for number of maximum dice throws in each round'''

    try:
        throws = int(input('Enter number of dice throws: '))
    except ValueError:
        print('number must be integer')
        return get_throws()

    if throws <= 0:
        print('you need at least 1 throw')
        return get_throws()

    return throws


def choose_to_reroll():
    '''Asks human player which dices to re-roll

    if empty string is given or 0 or wrong number
    returns empty roll list that means re-roll nothing.
    '''

    choice = input('Which dices to re-roll (sep with commas, empty = nothing to re-roll): ')
    if choice == '' or choice[0] == ' ' or choice[0] == '0':
        roll = []
    else:
        try:
            roll = [(int(n) - 1) for n in choice.split(',')]
        except ValueError:
            roll = []

    return roll


def add_remove_input(results: list, points: dict):
    '''Asks human player which figure to write down or strike out.

    from points dict (table)
    returns tuple of add, remove
    where add is a figure to add from results list
    remove figure to remove
    '''

    if len(results) > 0:
        choice = input('Choose figure to add (number) or name figure from points list to delete: ')

        try:
            choice = int(choice)
            if choice <= len(results):
                add = choice
            else:
                add = 1

            remove = ''

        except ValueError:
            if choice in points.keys():
                remove = choice
                add = 0

            else:
                remove = ''
                add = 1

    else:
        choice = input('Type figure name from points table to delete: ')
        remove = choice
        add = 0

    return add, remove
