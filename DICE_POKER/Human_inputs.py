# this file (module) contains input from human player


def get_players():
    players_number = int(input('number of players: '))

    players_list = []
    for number in range(players_number):
        players_list.append(input(f'Type name of {number + 1} player: '))

    return players_list


def get_rethrows()
    rethrows = int(input('numeber of throws: '))

    return rethrows


def add_remove_input(results: list, points: dict):

    if (len(results) > 0):

        for i in range(len(results)):
            print (str(i + 1) + '.', results[i][0], 'for', results[i][1], 'points', end=', ')

        print('')

        show_points_table(points)

        choice = input('Choose figure to add (number) or name figure from points list to delete: ')

        try:
            choice = int(choice)
            if (choice <= len(results)):
                add = choice
            else:
                add = 1

            remove = ''

        except ValueError:
            if (choice in points.keys()):
                remove = choice
                add = 0

            else:
                remove = ''
                add = 1

    else:
        points_table(points)

        choice = input('Type figure from points list to delete: ')

        remove = choice
        add = 0

    return add, remove
