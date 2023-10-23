# CS50 final project, to be finished
import inflect
import sys

from random import randint


# Used for a / an prefix
p = inflect.engine()

CLASSES = ["Barbarian", "Bard", "Cleric", "Druid", "Fighter", "Monk",
           "Paladin", "Ranger", "Rogue", "Sorcerer", "Warlock", "Wizard"]
RACES = ["Dragonborn", "Dwarf", "Elf", "Gnome", "Half-Elf",
         "Halfing", "Half-Orc", "Human", "Tiefling"]
ABILITY_SCORES = ["STR", "DEX", "CON", "INT", "WIS", "CHA"]


class Character:
    def __init__(self, char_class, race, score):
        self.name = name
        self.char_class = char_class
        self.race = race
        self.score = score


def main():
    calculate_scores()
    while True:
        try:
            ask = input("Roll dice? Y/N ").lower().strip()
            if ask == "y" or ask == "yes":
                roll = dice()
                if roll == 20:
                    print(f"Natural {roll}! Critical success!")
                elif roll == 1:
                    print(f"Critical fail!")
                else:
                    # Get ability score modifiers and add to the random roll
                    modifier = modifiers("Choose an ability score modifier: "
                                         "STR | DEX | CON | INT | WIS | "
                                         "CHA", char_score)
                    total_roll = roll + modifier
                    print(f"You rolled {roll}. With a of {modifier}, your "
                          f"total roll is {total_roll}!")
                    continue
            else:
                create = input("Create character? Y/N ").lower().strip()
                if create == "y" or create == "yes":
                    char_gender = char_genders()
                    char_name = input("Name your character: ")
                    char_class = char_classes()
                    char_race = char_races()
                    char_score = calculate_scores(char_race)
                    player_char = Character(char_gender, char_name, char_class, char_race, char_score)
                    print(f"You are {player_char.name}, {p.an(player_char.race)} {player_char.char_class}!\n You're ability scores are: {player_char.score}")
                    continue
                else:
                    sys.exit("Thank you for playing!")
        except ValueError:
            print("Invalid input")
            pass


# def character():
    # Create or load


def char_classes():
    global CLASSES
    while True:
        try:
            char_class = input("Class: ").lower().strip().capitalize()
            if char_class in classes:
                return char_class
            else:
                raise NameError
        except NameError:
            print("Invalid class")
            pass


def char_races():
    global RACES
    while True:
        try:
            char_race = input("Race: ").strip().title()
            if char_race in RACES:
                return char_race
            else:
                raise NameError
        except:
            print("Invalid race")
            pass


def calculate_scores(char_race):
    global RACES
    global ABILITY_SCORES
    # Add race dictionary to ability score dictionary
    score = {key: {} for key in RACES}
    score["Dragonborn"]["STR"] = 2
    score["Dragonborn"]["CHA"] = 1
    score["Dwarf"]["CON"] = 2
    score["Elf"]["DEX"] = 2
    score["Gnome"]["INT"] = 2
    score["Half-Elf"]["CHA"] = 2
    score["Halfing"]["DEX"] = 2
    score["Half-Orc"]["STR"] = 2
    score["Half-Orc"]["CON"] = 1
    for ability in ABILITY_SCORES:
        score["Human"][ability] = 1
    score["Tiefling"]["CHA"] = 2
    score["Tiefling"]["INT"] = 1
    # Allow users to add 1 point to two ability scores
    if char_race == "Half-Elf":
        while True:
            try:
                add_score = input("Add 1 to two ability scores. Type two "
                                  "with space between from STR | DEX | CON |"
                                  " INT | WIS\n").upper().split()
                if len(add_score) == 2 and add_score[0] != add_score[1]:    # Prevents choosing same ability score twice
                    i = 0
                    for _ in range(len(add_score)):
                        match add_score[i]:
                            case "STR":
                                score["Half-Elf"]["STR"] = 1
                                i += 1
                            case "DEX":
                                score["Half-Elf"]["DEX"] = 1
                                i += 1
                            case "CON":
                                score["Half-Elf"]["CON"] = 1
                                i += 1
                            case "INT":
                                score["Half-Elf"]["INT"] = 1
                                i += 1
                            case "WIS":
                                score["Half-Elf"]["WIS"] = 1
                                i += 1
                            case _:
                                raise ValueError
                    break
                else:
                    raise ValueError
            except ValueError:
                pass
    # Random generation of character ability scores
    stats = []
    for _ in range(len(ABILITY_SCORES)): # Loops per ability score
        stat = []
        for _ in range(4): # To roll four times
            stat.append(randint(1, 6)) # Rolls d6
        stat.remove(min(stat)) # Remove smallest number
        stats.append(sum(stat)) # Append the sum of the three die rolls
    # Initialise ability score to add to
    char_score = {"STR": 0, "DEX": 0, "CON": 0, "INT": 0, "WIS": 0, "CHA": 0}
    # User choose ability score to add rolled stats
    i = 0
    for _ in range(len(ABILITY_SCORES)):
        print(stats)
        choose_stat = input(f"For a roll of {stats[i]}, "
                            f"choose to assign to an ability score "
                            f"STR | DEX | CON | INT | WIS | CHA\n")
        char_score[choose_stat] = stats[i]
        i += 1
    # Add race ability scores to character
    race_score = score[char_race]
    for key, value in race_score.items():
        if key in char_score:
            char_score[key] += value
    return char_score


def modifiers(chosen_score, char_score):
    # Get corresponding ability score value that was chosen
    for key, _ in char_score.items():
        if key in chosen_score:
            score_mod = char_score[key]
    # Calculate modifier
    modifier = (score_mod - 10) / 2
    return modifier


# Determine type of roll, randomise a number returned based on chosen die faces
def dice():
    while True:
        try:
            roll_type = input("Advantage: 1 | Disadvantage: 2 | Straight: 3? ")
            roll_type = roll_type.lower().strip()
            if (roll_type == "advantage"
                    or roll_type.strip() == "1"
                    or roll_type == "disadvantage"
                    or roll_type.strip() == "2"):
                die_count = 2
                break
            elif roll_type == "straight" or roll_type.strip() =="3":
                die_count = 1
                break
            else:
                raise ValueError
        except:
            pass

    die_list = ["4", "6", "8", "10", "12", "20"]
    while True:
        try:
            # Check input is valid
            number = input("How many die faces? " )
            if number in die_list:
                number_rolled = []
                for _ in range(die_count):
                    # Store rolled value, rolls number of times per die_count
                    number_rolled.append(randint(1, int(number)))
                # Return number rolled according to roll type
                if roll_type == "advantage" or roll_type == "1":
                    return max(number_rolled)
                elif roll_type == "disadvantage" or roll_type == "2":
                    return min(number_rolled)
                else:
                    return number_rolled[0]
            else:
                raise ValueError
        except ValueError:
            print("Invalid number")
            pass


if __name__ == "__main__":
    main()
