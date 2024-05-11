import random
import math
import statistics

def calculate_modifier(number):
    if number == 10:
        return 0
    else:
        return math.floor((number - 10) / 2)

def roll_d20(modifier):
    roll = random.randint(1, 20)
    result = roll + modifier
    return result

def calculate_probability(modifier, target):
    outcomes = [i + modifier for i in range(1, 21)]
    successes = [i for i in outcomes if i >= target]
    probability = len(successes) / len(outcomes)
    return probability

# Test the function with different numbers
numbers = [2, 8, 11, 15, 21]

for number in numbers:
    modifier = calculate_modifier(number)
    results = [roll_d20(modifier) for _ in range(100)]
    mean = statistics.mean(results)
    print(f"Number: {number}, Modifier: {modifier}, Mean of 100 rolls: {mean}")
    print(f"Probability of beating 12: {calculate_probability(modifier, 12)}")