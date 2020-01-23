import Gameplay
import Visuals
import Human_inputs
import Preparations
import AI

import json

from os import system
from game_pattern_5 import figures_pattern

from PATH import RESULTS_FILE


def game_start(hand_size=5, dice_size=6) -> tuple:
    """Function prepares game."""

    system('clear')
    Visuals.message.headlist('Welcome to dice poker')
    Human_inputs.wait_for_key()
    players_list = Human_inputs.get_players()
    points_dict = Preparations.make_points_dict(figures_pattern)
    players_dict = Preparations.make_players_dict(players_list, points_dict)
    throws = Human_inputs.get_throws()
    Visuals.display_players(players_list)
    Human_inputs.wait_for_key()
    system('clear')

    return players_dict, throws


def game_cycle(players_dict: dict, figures_pattern: dict,
               rounds_number: int, rounds_left: int,
               number_of_throws=3, number_of_dices=5) -> dict:
    """one game cycle in which one action of each of all defined players are taken"""

    for name, points in players_dict.items():
        hand = [0 for dice in range(number_of_dices)]
        throws = number_of_throws
        choice = None

        while throws:
            Visuals.message.list(f'Plays {name}')
            hand = Gameplay.hand_throw(hand, choice)
            throws -= 1
            results = Gameplay.check_hand(hand, figures_pattern)
            filtered_results = Gameplay.remove_figures_already_got(results, points)
            filtered_results.sort(key=lambda x: x[1], reverse=True)

            Visuals.show_points_table(players_dict)
            Visuals.dices_view(hand)
            Visuals.show_avaiable_figures(filtered_results)

            add = 0
            remove = ''

            if name.lower().startswith('comp'):        #computer plays
                if throws > 0:
                    choice = AI.throw_or_not_and_what(hand, filtered_results)
                    if len(choice) == 0:
                        throws = 0
                        add, remove = AI.get_best_figure(filtered_results, points,
                                                     rounds_number, rounds_left,
                                                     AI.FIGURES_PROBABILITY_MAX_POINTS)
                    else:
                        print(f'{name} will re-roll dices: {choice}')
                        pass
                else:
                    add, remove = AI.get_best_figure(filtered_results, points,
                                                     rounds_number, rounds_left,
                                                     AI.FIGURES_PROBABILITY_MAX_POINTS)

                if add:
                    print(f'{name} adds {filtered_results[add - 1][0]} for {filtered_results[add - 1][1]} points')
                elif remove:
                    print(f'{name} strikes {remove}')

                Human_inputs.wait_for_key()
                system('clear')

            else:                                      #if not computer plays, plays human, obvious :)
                if throws > 0:
                    choice = Human_inputs.choose_to_reroll()
                    if len(choice) == 0:
                        throws = 0
                        add, remove = Human_inputs.add_remove_input(filtered_results, points)
                    else:
                        pass
                else:
                    add, remove = Human_inputs.add_remove_input(filtered_results, points)

                system('clear')

        points, message = Gameplay.add_points_strike_figures(filtered_results, points, add, remove)
        players_dict[name] = points

        Visuals.show_points_table(players_dict)
        Visuals.message.list(message)
        Visuals.message.prompt(f'{name} round finished')
        Human_inputs.wait_for_key()
        system('clear')

    return players_dict


def main():
    players_dict, throws = game_start()
    rounds_number = len(figures_pattern)

    for round_number in range(rounds_number):
        rounds_left = rounds_number - round_number
        Visuals.message.headlist(f'Round number {round_number + 1}')
        players_dict = game_cycle(players_dict, figures_pattern,
                                  rounds_number, rounds_left, throws)

    Visuals.show_points_table(players_dict)
    Visuals.show_winner(Gameplay.find_winner(players_dict))

    with open(RESULTS_FILE, 'a', encoding="UTF-8") as file:
        json.dump(players_dict, file, ensure_ascii=False)

    Human_inputs.wait_for_key()
    system('clear')


if __name__ == '__main__':
    main()
