from art import logo
import random

from game_data import data




 #get a random entry from game data
def get_random_entry():
    item = random.choice(data)
    return item

A = get_random_entry()
B = get_random_entry()
score =0


def display_choices(A,B):
    print(logo)
    print(A["follower_count"], B["follower_count"])
    print(f"Compare A: {A['name']}, a {A['description']}, from {A['country']}")
    print("vs")
    print(f"Against B: {B['name']}, a {B['description']}, from {B['country']}")
    print(f"Your score is {score}")



def check_answer(A, B, player_guess):
    if int(A["follower_count"]) > int(B["follower_count"]):
        champion = A
        champion_letter = "A"
    else:
        champion = B
        champion_letter = "B"


    if player_guess == champion_letter:
        is_correct = True
    else:
        is_correct = False


    return is_correct, champion





while True:
    display_choices(A,B)
    player_guess = input("Which one? “A” or “B”: ").upper()

    is_correct, winner = check_answer(A, B, player_guess)

    if is_correct:
        score += 1
        A = winner  # carry forward the winner
        B = get_random_entry()

    else:
        print(f"Sorry, that’s wrong . Final score: {score}")





















