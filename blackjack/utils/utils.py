import os
import random
cards_not_in_deck = ["red_joker.svg"]

def get_random_card(number_of_cards = 1) -> tuple:
    """
    Returns a list of random cards.
    """
    cards_path = []
    cards_name = []
    directory = os.path.join(
            os.path.dirname(os.path.realpath(__file__)), 
            "../resources/assets/cards/"
        )
    for i in range(number_of_cards):
        choice = random.choice([x for x in os.listdir(directory) if x not in cards_not_in_deck])
        cards_not_in_deck.append(choice)
        path = os.path.join(directory, choice)
        if(number_of_cards == 1):
            return path, choice
        cards_path.append(path)
        cards_name.append(choice)
    return (cards_path, cards_name)

def calculate_points(cards):
    """
    Returns the sum of the points of the cards.
    """
    aces = 0
    points = 0
    for card in cards:
        if(str(card[0]).isdigit()):
            points += int(card[0])
        elif(str(card[0]) == "a"):
            aces +=1
            points += 11
        elif(str(card[0]).isalpha()):
            points += 10
    while(points>21 and aces>0):
        points -= 10
        aces -= 1
    return points