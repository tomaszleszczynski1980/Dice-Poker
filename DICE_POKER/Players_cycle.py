# stary main


def main(points: dict, rounds: int):

    hand = [0, 0, 0, 0, 0]

    for loop in range(rounds):

        hand = dice_throw(5)

        print(hand)
        print('')

        dices_view(hand)

        res = check_hand(hand, points)

        print(res)

        reroll = input_to_reroll()

        if (len(reroll) > 0 and len(reroll) < 6):

            hand = another_throw(hand, reroll)

            print(hand)
            print('')

            dices_view(hand)

            res = check_hand(hand, points)

            print(res)

        elif (len(reroll) > 0 and len(reroll) >= 6):

            reroll = reroll[0:5]

            hand = another_throw(hand, reroll)

            print(hand)
            print('')

            dices_view(hand)

            res = check_hand(hand, points)

            print(res)

        elif (len(reroll) == 0):
            pass

        addrem = add_remove_input(res, points)

        add = addrem[0]
        remove = addrem[1]

        points = adding_points_striking_figures(res, points, add, remove)

        print('')

        points_table(points)

        print('')
        stop = input('Press enter to next move, q to quit:')

        if stop == 'q':
            break

    print ('Finished! You gain in total: ', sum_points(points), 'points')

main(points, 11)