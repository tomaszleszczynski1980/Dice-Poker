import Gameplay
import Visuals
import Human_inputs
import Preparations

from os import system
from game_pattern_5 import figures_pattern


def game_start(hand_size=5, dice_size=6):
    Visuals.message('Welcome to dice poker')
    system('clear')
    players_list = Human_inputs.get_players()
    points_dict = Preparations.make_points_dict(figures_pattern)
    players_dict = Preparations.make_players_dict(players_list, points_dict)
    throws = Human_inputs.get_throws()
    Visuals.display_players(players_list)
    Human_inputs.wait_for_key()
    system('clear')

    return players_dict, throws


def game_cycle(players_dict: dict, figures_pattern: dict, number_of_throws=3, number_of_dices=5):
    """one game cycle in which one action of each of all defined players are taken"""

    for name, points in players_dict.items():
        Visuals.message(f'Plays {name}')
        hand = [0 for i in range(number_of_dices)]
        throws = number_of_throws
        choice = None

        while throws:
            hand = Gameplay.hand_throw(hand, choice)
            throws -= 1
            results = Gameplay.check_hand(hand, figures_pattern)
            results = Gameplay.remove_figures_already_got(results, points)
            results.sort(key=lambda x: x[1], reverse=True)

            Visuals.show_points_table(players_dict)
            Visuals.dices_view(hand)
            Visuals.show_avaiable_figures(results)

            if throws > 0:
                choice = Human_inputs.choose_to_reroll()
                if len(choice) == 0:
                    throws = 0
                    add, remove = Human_inputs.add_remove_input(results, points)
                else:
                    pass
            else:
                add, remove = Human_inputs.add_remove_input(results, points)

            system('clear')

        points, message = Gameplay.add_points_strike_figures(results, points, add, remove)
        players_dict[name] = points

        Visuals.show_points_table(players_dict)
        Visuals.message(message)
        Visuals.message(f'{name} round finished')
        Human_inputs.wait_for_key()
        system('clear')

    return players_dict


def main():
    players_dict, throws = game_start()

    for round_number in range(len(figures_pattern)):
        Visuals.message(f'Round number {round_number}')
        players_dict = game_cycle(players_dict, figures_pattern, throws)

    Visuals.show_points_table(players_dict)
    Visuals.show_winner(Gameplay.find_winner(players_dict))

    Human_inputs.wait_for_key()
    system('clear')


# here it goes
main()
