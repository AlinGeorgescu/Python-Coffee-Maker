"""
(C) Copyright 2020
A command-line controlled coffee maker.
"""

import sys

import load_recipes

# Example result/interactions:

# I'm a smart coffee maker
# Enter command:
# list
# americano, cappuccino, espresso
# Enter command:
# status
# water: 100%
# coffee: 100%
# milk: 100%
# Enter command:
# make
# Which coffee?
# espresso
# Here's your espresso!
# Enter command:
# refill
# Which resource? Type 'all' for refilling everything
# water
# water: 100%
# coffee: 90%
# milk: 100%
# Enter command:
# exit

# Commands
EXIT = "exit"
LIST_COFFEES = "list"
MAKE_COFFEE = "make"
HELP = "help"
REFILL = "refill"
RESOURCE_STATUS = "status"
COMMANDS = [EXIT, LIST_COFFEES, MAKE_COFFEE, REFILL, RESOURCE_STATUS, HELP]

# Coffee examples
ESPRESSO = "espresso"
AMERICANO = "americano"
CAPPUCCINO = "cappuccino"

# Resources examples
WATER = "water"
COFFEE = "coffee"
MILK = "milk"
ALL = "all"

# Coffee maker's resources - the values represent the fill percents
RESOURCES = {WATER: 100, COFFEE: 100, MILK: 100}

def make_coffee():
    """
    Function to make a coffee
    """
    print("Which coffee?")
    line = sys.stdin.readline().rstrip("\n")

    if line == ESPRESSO or line == AMERICANO or line == CAPPUCCINO:
        used_ingredients = load_recipes.load_recipe(line)
        RESOURCES[WATER] -= used_ingredients[WATER]
        RESOURCES[COFFEE] -= used_ingredients[COFFEE]
        RESOURCES[MILK] -= used_ingredients[MILK]

        if RESOURCES[WATER] < 0 or RESOURCES[COFFEE] < 0 or RESOURCES[MILK] < 0:
            RESOURCES[WATER] += used_ingredients[WATER]
            RESOURCES[COFFEE] += used_ingredients[COFFEE]
            RESOURCES[MILK] += used_ingredients[MILK]
            print("Not enough ingredients, please refill!")
        else:
            print("Here is your " + line)

    else:
        print("Unknown coffee, make aborted!")

def refill():
    """
    Refill function
    """
    print("Which resource? Type 'all' for refilling everything")
    line = sys.stdin.readline().rstrip("\n")

    if line == ALL:
        RESOURCES[WATER], RESOURCES[COFFEE], RESOURCES[MILK] = 100, 100, 100
    elif line == WATER:
        RESOURCES[WATER] = 100
    elif line == COFFEE:
        RESOURCES[COFFEE] = 100
    elif line == MILK:
        RESOURCES[MILK] = 100
    else:
        print("Unknown resource, refill aborted!")

    for ingredient, amount in RESOURCES.items():
        print("%s: %d%%" % (ingredient, amount))

def main():
    """
    Main fucntion - parsing and executing commands
    """
    print("I'm a smart coffee maker")
    while True:
        print("Enter command:")
        command = sys.stdin.readline().rstrip("\n")

        if command == EXIT:
            sys.exit(0)
        elif command == RESOURCE_STATUS:
            for ingredient, amount in RESOURCES.items():
                print("%s: %d%%" % (ingredient, amount))
        elif command == REFILL:
            refill()
        elif command == LIST_COFFEES:
            print(ESPRESSO + " " + AMERICANO + " " + CAPPUCCINO)

        elif command == MAKE_COFFEE:
            make_coffee()
        else:
            print("Unknown command!")

if __name__ == "__main__":
    main()
