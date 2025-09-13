from art import logo
import random

from game_data import data

#print(logo)




 #get a random entry from game data
def get_random_entry():
    item = random.choice(data)
    return item

A = get_random_entry()
B = get_random_entry()

def display_choices(A, B):
    print(f"Compare A: {A['name']}, a {A['description']}, from {A['country']}")
    print("vs")
    print(f"Against B: {B['name']}, a {B['description']}, from {B['country']}")





display_choices(A, B)
