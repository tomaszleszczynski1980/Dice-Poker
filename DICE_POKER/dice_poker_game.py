import Gameplay
import Visuals
import Human_inputs
import Preparations
import AI

from os import system
from game_pattern_5 import figures_pattern



def game_start(hand_size=5, dice_size=6) -> tuple:
    Visuals.message.list('Welcome to dice poker')
    system('clear')
    players_list = Human_inputs.get_players()
    points_dict = Preparations.make_points_dict(figures_pattern)
    players_dict = Preparations.make_players_dict(players_list, points_dict)
    throws = Human_inputs.get_throws()
    Visuals.display_players(players_list)
    Human_inputs.wait_for_key()
    system('clear')

    return players_dict, throws


def game_cycle(players_dict: dict, figures_pattern: dict,
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

            if name.lower().startswith('comp'):        #computer plays
                if throws > 0:
                    # we don't have function for computer to re-throw
                    # instead that, computer says:

                    Visuals.message.warning(f'{name} says: I am too stupid to choose what to re-roll')
                    throws = 0
                    add, remove = AI.get_best_figure(filtered_results, points, AI.FIGURES_PROBABILITY_MAX_POINTS)

                    '''
                    choice = AI.computer_choice()
                    if len(choice) == 0:
                        throws = 0
                        add, remove = AI.get_best_figure(filtered_results, points, AI.FIGURES_PROBABILITY_MAX_POINTS)
                    else:
                        pass
                    '''

                else:
                    add, remove = AI.get_best_figure(filtered_results, points, AI.FIGURES_PROBABILITY_MAX_POINTS)

                if add:
                    message = 'add {0} for {1} points'.format(filtered_results[add - 1][0],filtered_results[add - 1][1])
                else:
                    message = 'strike {0} from my points list'.format(remove)

                Visuals.message.warning(f'So i decided to {message}')
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

    for round_number in range(len(figures_pattern)):
        Visuals.message.headlist(f'Round number {round_number + 1}')
        players_dict = game_cycle(players_dict, figures_pattern, throws)

    Visuals.show_points_table(players_dict)
    Visuals.show_winner(Gameplay.find_winner(players_dict))

    Human_inputs.wait_for_key()
    system('clear')


if __name__ == '__main__':
    main()
