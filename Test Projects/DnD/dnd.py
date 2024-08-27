# import random
#
#
# # Ability Score Generation
# def roll_ability_score():
#     rolls = [random.randint(1, 6) for _ in range(4)]
#     rolls.sort()
#     return sum(rolls[1:])
#
#
# # DnD 5e Ability Scores
# ABILITY_SCORES = {
#     "Strength": roll_ability_score(),  # str
#     "Dexterity": roll_ability_score(),  # dex
#     "Constitution": roll_ability_score(),  # con
#     "Intelligence": roll_ability_score(),  # int
#     "Wisdom": roll_ability_score(),  # wis
#     "Charisma": roll_ability_score(),  # cha
# }
#
#
# # Display Ability Scores
# def display_ability_scores():
#     print("\nAbility Scores:")
#     for ability, score in ABILITY_SCORES.items():
#         print(f"{ability:10}: {score}")
#
#
# # Calculate Ability Modifiers
# ABILITY_MODIFIERS = {k: int((v - 10) / 2) for k, v in ABILITY_SCORES.items()}
#
# # DnD Classes
# CLASSES = [
#     "Fighter",
#     "Wizard",
#     "Rogue",
#     "Cleric",
# ]
#
# # DnD Races
# RACES = [
#     "Human",
#     "Elf",
#     "Dwarf",
#     "Gnome",
# ]
#
#
# def choose_from(options, prompt):
#     print(prompt)
#     for i, option in enumerate(options, start=1):
#         print(f"{i}. {option}")
#     choice = int(input("Enter your choice: "))
#     while choice < 1 or choice > len(options):
#         print("Invalid choice. Please try again.")
#         choice = int(input("Enter your choice: "))
#     return options[choice - 1]
#
#
# # Character Creation
# def create_character():
#     character = {}
#
#     character["Name"] = input("Enter your character's name: ")
#     character["Race"] = choose_from(RACES, "Choose your race:")
#     character["Class"] = choose_from(CLASSES, "Choose your class:")
#
#     return character
#
#
# # Display Character Details
# def display_character(character):
#     print("\nCharacter Details:")
#     for key, value in character.items():
#         print(f"{key:10}: {value}")
#     display_ability_scores()
#     print("\nAbility Modifiers:")
#     for ability, modifier in ABILITY_MODIFIERS.items():
#         print(f"{ability:10}: {modifier}")
#
#         # Main Menu
#
#
# def main_menu():
#     print("DnD 5th Edition Character Creator")
#     print("=" * 30)
#     print("1. Create a Character")
#     print("2. Display Character")
#     print("3. Exit")
#     choice = int(input("Enter your choice: "))
#
#     while choice < 1 or choice > 3:
#         print("Invalid choice. Please try again.")
#         choice = int(input("Enter your choice: "))
#
#     if choice == 1:
#         global CHARACTER
#         CHARACTER = create_character()
#     elif choice == 2:
#         if 'CHARACTER' in globals():
#             display_character(CHARACTER)
#         else:
#             print("No character created yet. Please create one first.")
#     else:
#         print("Goodbye!")
#         return choice
#
#
# if __name__ == "__main__":
#     while True:
#         if main_menu() == 3:
#             break


import json
import os
import random


# Ability Score Generation
def roll_ability_score():
    rolls = [random.randint(1, 6) for _ in range(4)]
    rolls.sort()
    return sum(rolls[1:])


# DnD 5e Ability Scores
ABILITY_SCORES = {
    "Strength": roll_ability_score(),  # str
    "Dexterity": roll_ability_score(),  # dex
    "Constitution": roll_ability_score(),  # con
    "Intelligence": roll_ability_score(),  # int
    "Wisdom": roll_ability_score(),  # wis
    "Charisma": roll_ability_score(),  # cha
}


# Display Ability Scores
def display_ability_scores():
    print("\nAbility Scores:")
    for ability, score in ABILITY_SCORES.items():
        print(f"{ability:10}: {score}")


# Calculate Ability Modifiers
ABILITY_MODIFIERS = {k: int((v - 10) / 2) for k, v in ABILITY_SCORES.items()}

# DnD Classes
CLASSES = ["Fighter", "Wizard", "Rogue", "Cleric", ]

# DnD Races
RACES = ["Human", "Elf", "Dwarf", "Gnome", ]


def choose_from(options, prompt):
    print(prompt)
    for i, option in enumerate(options, start=1):
        print(f"{i}. {option}")
    choice = int(input("Enter your choice: "))
    while choice < 1 or choice > len(options):
        print("Invalid choice. Please try again.")
        choice = int(input("Enter your choice: "))
    return options[choice - 1]


# Character Creation
def create_character():
    character = {}
    try:
        character["Name"] = input("Enter your character's name: ")
        if not character["Name"]:
            raise ValueError("Character name cannot be empty.")

        character["Race"] = choose_from(RACES, "Choose your race:")
        character["Class"] = choose_from(CLASSES, "Choose your class:")
        return character
    except ValueError as ve:
        print(f"Error: {ve}")
        return None


# Display Character Details
def display_character(character):
    if character:
        print("\nCharacter Details:")
        for key, value in character.items():
            print(f"{key:10}: {value}")
        display_ability_scores()
        print("\nAbility Modifiers:")
        for ability, modifier in ABILITY_MODIFIERS.items():
            print(f"{ability:10}: {modifier}")
    else:
        print("\nNo character found.")


def save_character(character, file_name):
    with open(file_name, 'w') as file:
        json.dump(character, file, indent=2)
        print(f"Character saved to {file_name}")


def load_character(file_name):
    try:
        with open(file_name, 'r') as file:
            character = json.load(file)
            print(f"Character loaded from {file_name}")
            return character
    except FileNotFoundError:
        print(f"Error: File {file_name} not found.")
        return None
    except json.JSONDecodeError:
        print(f"Error: Invalid JSON data in the file {file_name}.")
        return None


# Character IO Operations
def io_menu():
    print("\nCharacter IO Menu:")
    print("1. Save Character")
    print("2. Load Character")
    print("3. Back to Main Menu")
    choice = int(input("Enter your choice: "))
    while choice < 1 or choice > 3:
        print("Invalid choice. Please try again.")
        choice = int(input("Enter your choice: "))
    return choice


def save_load_character():
    if 'CHARACTER' in globals():
        choice = io_menu()
        if choice == 1:
            file_name = input(
                "Enter file name to save (with .json extension): ")
            if file_name.endswith(".json"):
                save_character(CHARACTER, file_name)
            else:
                print("File name should end with .json extension.")
        elif choice == 2:
            file_name = input(
                "Enter file name to load (with .json extension): ")
            if file_name.endswith(".json"):
                loaded_character = load_character(file_name)
                if loaded_character:
                    CHARACTER = loaded_character
            else:
                print("File name should end with .json extension.")
    else:
        print("No character created yet. Please create one first.")

        # Main Menu


def main_menu():
    print("DnD 5th Edition Character Creator")
    print("=" * 30)
    print("1. Create a Character")
    print("2. Display Character")
    print("3. Character IO")
    print("4. Exit")
    choice = int(input("Enter your choice: "))
    while choice < 1 or choice > 4:
        print("Invalid choice. Please try again.")
        choice = int(input("Enter your choice: "))
    return choice


if __name__ == "__main__":
    while True:
        choice = main_menu()
        if choice == 1:
            CHARACTER = create_character()
        elif choice == 2:
            display_character(CHARACTER)
        elif choice == 3:
            save_load_character()
        else:  # choice == 4:
            print("Goodbye!")
            break



# import json
# import os
# import random
#
#
# # Ability Score Generation
# def roll_ability_score():
#     rolls = [random.randint(1, 6) for _ in range(4)]
#     rolls.sort()
#     return sum(rolls[1:])
#
#
# # DnD 5e Ability Scores
# ABILITY_SCORES = {
#     "Strength": roll_ability_score(),  # str
#     "Dexterity": roll_ability_score(),  # dex
#     "Constitution": roll_ability_score(),  # con
#     "Intelligence": roll_ability_score(),  # int
#     "Wisdom": roll_ability_score(),  # wis
#     "Charisma": roll_ability_score(),  # cha
# }
#
#
# # Display Ability Scores
# def display_ability_scores():
#     print("\nAbility Scores:")
#     for ability, score in ABILITY_SCORES.items():
#         print(f"{ability:10}: {score}")
#
#
# # Calculate Ability Modifiers
# ABILITY_MODIFIERS = {k: int((v - 10) / 2) for k, v in ABILITY_SCORES.items()}
#
# # DnD Classes
# CLASSES = ["Fighter", "Wizard", "Rogue", "Cleric", ]
#
# # DnD Races
# RACES = ["Human", "Elf", "Dwarf", "Gnome", ]
#
#
# # Error Handling function for character creation
# def get_valid_input(options, prompt):
#     while True:
#         try:
#             choice = int(input(prompt))
#             if choice < 1 or choice > len(options):
#                 print("Invalid choice. Please try again.")
#             else:
#                 return options[choice - 1]
#         except ValueError:
#             print("Invalid input. Please enter a number.")
#
#
# def choose_from(options, prompt):
#     print(prompt)
#     for i, option in enumerate(options, start=1):
#         print(f"{i}. {option}")
#     return get_valid_input(options, "Enter your choice: ")
#
#
# # Character Creation
# def create_character():
#     character = {}
#     try:
#         character["Name"] = input("Enter your character's name: ") or None
#         if not character["Name"]:
#             raise ValueError("Name cannot be empty.")
#         character["Race"] = choose_from(RACES, "Choose your race:")
#         character["Class"] = choose_from(CLASSES, "Choose your class:")
#         return character
#     except ValueError as ve:
#         print(f"Error: {str(ve)}")
#         return None
#
#
# # Display Character Details
# def display_character(character):
#     if character:
#         print("\nCharacter Details:")
#         for key, value in character.items():
#             print(f"{key:10}: {value}")
#         display_ability_scores()
#         print("\nAbility Modifiers:")
#         for ability, modifier in ABILITY_MODIFIERS.items():
#             print(f"{ability:10}: {modifier}")
#     else:
#         print("\nNo Character Found.")
#
#
# # Save Character to JSON file
# def save_character(character):
#     if character:
#         file_name = character["Name"] + ".json"
#         file_path = os.path.join(os.getcwd(), "characters", file_name)
#         # create characters folder if not exist
#         os.makedirs(os.path.dirname(file_path), exist_ok=True)
#         with open(file_path, 'w') as f:
#             json.dump(character, f, indent=4)
#         print(f"Character saved to '{file_path}'.")
#     else:
#         print("No character to save.")
#
#
# # Load Character from JSON file
# def load_character():
#     char_file = choose_from(os.listdir("characters"),
#                             "Select a character to load (Enter the file name): ")
#     file_path = os.path.join(os.getcwd(), "characters", char_file)
#     with open(file_path, 'r') as f:
#         try:
#             return json.load(f)
#         except json.decoder.JSONDecodeError:
#             print(
#                 f"Error loading character from '{file_path}'. Invalid JSON data.")
#             return None
#
#
# # Character Creation Menu
# def character_creation_menu():
#     print("=" * 30)
#     print("Character Creation Menu")
#     print("=" * 30)
#     print("1. Create New Character")
#     print("2. Load Character")
#     print("3. Back to Main Menu")
#     choice = get_valid_input([1, 2, 3], "Enter your choice: ")
#
#     if choice == 1:
#         return create_character()
#     elif choice == 2:
#         return load_character()
#     else:
#         return None
#
#
# # Main Menu
# def main_menu():
#     print("DnD 5th Edition Character Creator")
#     print("=" * 30)
#     print("1. Create/Load Character")
#     print("2. Display Character")
#     print("3. Exit")
#     choice = get_valid_input([1, 2, 3], "Enter your choice: ")
#
#     if choice == 1:
#         return character_creation_menu()
#     elif choice == 2:
#         if 'CHARACTER' in globals():
#             display_character(CHARACTER)
#         else:
#             print("No character created yet. Please create or load one first.")
#     else:
#         print("Goodbye!")
#         return choice
#
#
# if __name__ == "__main__":
#     # Create a "characters" folder to store character files
#     os.makedirs(os.path.join(os.getcwd(), "characters"), exist_ok=True)
#
#     while True:
#         if main_menu() == 3:
#             break