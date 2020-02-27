"""
(C) Copyright 2020
A command-line controlled coffee maker.
"""

RECIPES_FOLDER = "recipes"

def load_recipe(coffee):
    """
    Load all the available coffee recipes from the folder 'recipes/'

    File format:
        first line: coffee name
        next lines: resource=percentage
    """
    file_name = RECIPES_FOLDER + "/" + coffee + ".txt"
    used_ingredients = {}

    with open(file_name, "r") as file_desc:
        line = file_desc.readline()

        for _ in range(3):
            line = file_desc.readline()
            tokens = line.split('=')
            used_ingredients[tokens[0]] = int(tokens[1])

    return used_ingredients
