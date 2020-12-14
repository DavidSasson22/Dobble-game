import random
import time

DECK = [
    ['Ansible', 'AstroPy', 'Attrs', 'BeeWare'],
    ['BeeWare', 'Bottle', 'BuildBot', 'Celery'],
    ['Attrs', 'Bottle', 'CherryPy', 'Chopsticks'],
    ['Ansible', 'Celery', 'Chopsticks', 'Click'],
    ['AstroPy', 'Coala', 'BuildBot', 'Chopsticks'],
    ['AstroPy', 'Cookiecutter', 'CherryPy', 'Celery'],
    ['Attrs', 'Coala', 'Cython', 'Celery'],
    ['BeeWare', 'Cookiecutter', 'Cython', 'Chopsticks'],
    ['AstroPy', 'Bottle', 'Cython', 'Click'],
    ['Attrs', 'Cookiecutter', 'BuildBot', 'Click'],
    ['Ansible', 'CherryPy', 'BuildBot', 'Cython'],
    ['BeeWare', 'Coala', 'CherryPy', 'Click'],
    ['Ansible', 'Cookiecutter', 'Coala', 'Bottle']
      ]


def cards_intersect(card1, card2):
    in_both = (set(card1) & set(card2))
    return list(in_both)


def remove_card(deck, test_card):
    test_card.sort()
    for card in deck:
        card.sort()
        if card == test_card:
            deck.remove(card)
            return True
    print("Error! card is not in the deck")
    return False


def add_card(deck, test_card):
    if len(test_card) != len(deck[0]):
        print("Error! Card is of wrong length")
        return False
    else:
        for card in deck:
            if len(cards_intersect(card, test_card)) != 1:
                print("Error! number of matches for new card is not one")
                return False
    deck.append(test_card)
    return True


def is_valid(deck):
    i = 0
    while i < len(deck):
        tested_card = deck[0]
        del deck[0]
        if add_card(deck, tested_card):
            i += 1
        else:
            return False
    return True


def draw_random_cards(deck):
    hand = random.sample(deck, 2)
    return hand


def print_symbols_counts(deck):
    symbol_dictionary = {}
    symbol_list = []
    for card in deck:
        for symbol in card:
            symbol_list.append(symbol)
        symbol_list.sort()
    for symbol in symbol_list:
        symbol_dictionary[symbol] = symbol_list.count(symbol)
    for key in symbol_dictionary:
        print("{} {}".format(key, symbol_dictionary[key]))


def play_dobble(DECK):
    operation = input("Select operation: (P)lay, (A)dd card, (R)emove card, or (C)ount:\n")
    if operation.upper() == "A":
        additional_card_symbols = input("Enter your card:\n ")
        additional_card = additional_card_symbols.split(", ")
        add_card(DECK, additional_card)

    elif operation.upper() == "R":
        removal_card_symbols = input("Enter your card:\n ")
        removal_card = removal_card_symbols.split(", ")
        remove_card(DECK, removal_card)

    elif operation.upper() == "C":
        print_symbols_counts(DECK)

    elif operation.upper() == "P":
        rounds_time = []
        correct = 0
        wrong = 0
        while len(DECK) > 2:
            game_cards = draw_random_cards(DECK)
            print("Identify joint symbol: ")
            print("{}\n{}".format(", ".join(game_cards[0]), ", ".join(game_cards[1])))
            a = time.time()
            answer = input()
            speed = time.time() - a
            correct_answer = cards_intersect(game_cards[0], game_cards[1])
            if answer == correct_answer[0]:
                correct += 1
                rounds_time.append(speed)
                print("Very Nice! Found the correct card in {:.2f} sec".format(speed))
            else:
                wrong += 1
                rounds_time.append(speed)
                print("Wrong!")
            for card in game_cards:
                remove_card(DECK, card)
        sum = 0
        for i in range(0, len(rounds_time)):
            sum += rounds_time[i]
        average = sum/len(rounds_time)
        print("Finished Game. Correct: {} Wrong: {} Average time: {:.2f}".format(correct, wrong, average))
    input("press any key to exit")


if __name__ == '__main__':
    play_dobble(DECK)


