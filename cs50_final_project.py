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
CHAR_SCORE = {"STR": 10, "DEX": 10, "CON": 10, "INT": 10, "WIS": 10, "CHA": 10}


def main():
    # Default modifier of 0
    char_score = CHAR_SCORE
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
                    modifier = modifiers(
                        input("Choose an ability score modifier "
                              "(STR | DEX | CON | INT | WIS | CHA): "
                              "").upper().strip()
                        , char_score)
                    total_roll = roll + modifier
                    print(f"You rolled {roll}. With a modifier of "
                          f"{int(modifier)}, "
                          f"your "
                          f"total roll is {int(total_roll)}!")
                    continue
            elif ask == "n" or ask == "no":
                use_character = (input("Would you like to create or load a "
                                       "character? ").lower().strip())
                if use_character == "create":
                    character = create_character()
                    print(f"You are {character[0]}, "
                          f"{p.an(character[2])} {character[1]}!"
                          f"\n You're ability scores are: {character[3]}")
                    character_save(character)
                    continue
                elif use_character == "load":
                    with open("dnd_characters.txt", "r") as f:
                        lines = f.readlines()
                        count = 0
                        for line in lines:
                            count += 1
                            print(count + " " + line.strip("\n"))
                        character_choice = input("Enter character "
                                                 "number: ")
                        character_load = lines[character_choice]

                    pass
                elif use_character == "n" or use_character == "no":
                    sys.exit("Thank you for playing!")
                else:
                    raise ValueError
        except ValueError:
            print("Invalid input")


def character_save(details):
    # Save character in local file
    with open("dnd_characters.txt", "a") as f:
        f.write(" ".join(str(item) for item in details))
        f.write("\n")


def create_character():
    name = input("Name your character: ")
    _class = char_classes()
    race = char_races()
    score = calculate_scores(race)
    return name, _class, race, score


def char_classes():
    global CLASSES
    while True:
        try:
            char_class = input("Class: ").lower().strip().capitalize()
            if char_class in CLASSES:
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
                # Prevents choosing same ability score twice
                if len(add_score) == 2 and add_score[0] != add_score[1]:
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
    # Loops per ability score
    for _ in range(len(ABILITY_SCORES)):
        stat = []
        # To roll four times
        for _ in range(4):
            # Rolls d6
            stat.append(randint(1, 6))
        # Remove smallest number
        stat.remove(min(stat))
        # Append the sum of the three die rolls
        stats.append(sum(stat))
    # Initialise ability score to add to
    char_score = CHAR_SCORE
    # User choose ability score to add rolled stats
    i = 0
    for _ in range(len(ABILITY_SCORES)):
        print(stats)
        choose_stat = (input(f"For a roll of {stats[i]}, "
                             f"choose to assign to an ability score "
                             f"STR | DEX | CON | INT | WIS | CHA\n").upper().
                       strip())
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
            elif roll_type == "straight" or roll_type.strip() == "3":
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
            number = input("How many die faces? ")
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
