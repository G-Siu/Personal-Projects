import cs50_final_project as project
import pytest


def test_char_classes(monkeypatch):
    # Provide inputs
    class_one = "Barbarian"
    class_two = "wizard"
    class_three = " bard"
    class_four = "nonsense-word"
    class_five = "123"

    # Create iterator object
    answers = iter([class_one, class_two, class_three, class_four, class_five])

    monkeypatch.setattr("builtins.input", lambda _: next(answers))

    char_class_one = project.char_classes()
    char_class_two = project.char_classes()
    char_class_three = project.char_classes()
    assert char_class_one == "Barbarian"
    assert char_class_two == "Wizard"
    assert char_class_three == "Bard"
    with pytest.raises(Exception) as e_info:
        char_class_four = project.char_classes()
    with pytest.raises(Exception) as e_info:
        char_class_five = project.char_classes()


def test_char_races(monkeypatch):
    # Provide inputs
    race_one = "Elf"
    race_two = " dragonborn"
    race_three = "nonsense-word"
    race_four = "123"

    # Create iterator object
    answers = iter([race_one, race_two, race_three, race_four])

    monkeypatch.setattr("builtins.input", lambda _: next(answers))

    char_race_one = project.char_races()
    char_race_two = project.char_races()
    assert char_race_one == "Elf"
    assert char_race_two == "Dragonborn"
    # with pytest.raises(Exception) as e_info:
    #     char_race_three = project.char_races()
    # with pytest.raises(Exception) as e_info:
    #     char_race_four = project.char_races()


# def test_modifiers(monkeypatch):
#     # Provide inputs
