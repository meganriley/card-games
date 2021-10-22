def get_rounds(number):
    return list(range(number, number + 3))


def concatenate_rounds(rounds_1, rounds_2):
    for round in rounds_2:
        rounds_1.append(round)
    return rounds_1
    


def list_contains_round(rounds, number):
    return number in rounds


def card_average(hand):
    return sum(hand)/len(hand)


def approx_average_is_average(hand):
    first_and_last = (hand[0]+hand[-1])/2
    median = hand[int(len(hand)/2)]
    true_avg = sum(hand)/len(hand)

    if first_and_last == true_avg or median == true_avg:
        return True
    else:
        return False


def average_even_is_average_odd(hand):
    even_i = hand[0:hand[-1]:2]
    even_avg = sum(even_i)/len(even_i)
    true_avg = sum(hand)/len(hand)

    if even_avg == true_avg:
        return True
    else:
        return False
    


def maybe_double_last(hand):
    if hand[-1] == 11:
        hand[-1] *= 2
    return hand
