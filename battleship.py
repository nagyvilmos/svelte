"""
Tumblehome
"""
import argparse

instructions = [
    "You are a humble French constructor of battleships. Your challenge is to produce just one ",
    "(1) competent vessel. Arranged against you are the lads of the Jeune École, who will just ",
    "not stop having ideas, and the Noisy Neighbours, who have one big idea of their own..."
]

scores = [0,0,0]
cIx = 0 # construction
nIx = 1 # nonsense
dIx = 2 # dreadnaught

ending = [
    [
        "Your marvelous new battleship is launched successfully and is the wonder",
        "of the world! Not least amongst certain navel commentators, who are wondering ""Why?""."
    ],
    [
        "The Jeune École have had so many damn ideas that construction is halted so",
        "that everyone can have a jolly good argument - for years - about how to complete it.",
        "You run away to the circus, where at least the clowns are professionally trained."
    ],
    [
        "The Noisy Neighbours launch a turbine powered, all big-gun battleship.",
        "Bloody show-offs. Your masterpiece is obsolete before it leaves the stocks."
    ]
]

parser = argparse.ArgumentParser()
parser.add_argument("-a", "--autorun", action="store_true",
                    help="auto run with random inputs")
args = parser.parse_args()




def run_game():
    return nIx

for line in instructions:
    print(line)
print()

result = run_game()

for line in ending[result]:
    print(line)
