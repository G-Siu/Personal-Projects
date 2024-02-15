# Author : Gary Siu
# Date : 5th Feb 2024
# Description : Calculate Difference Between Two Dates
from datetime import date


def main():
    print("Calculate difference between two dates.")
    # Get user date inputs
    date_input1, date1, date_input2, date2 = input_dates()
    # Pass dates in get_difference() and return the difference
    calculate_difference = get_difference(date1, date2)
    # Print result
    print("Difference between", date_input1, "and", date_input2, "is",
          calculate_difference.days, "days")


# Get date inputs from user
def input_dates():
    while True:
        # Get date input
        date_input1 = input("Input first date DD-MM-YYYY: ")
        # Split input by "-"
        date1 = date_input1.split("-")
        # Check date is within date format limits
        if (1 <= int(date1[0]) <= 31 and 1 <= int(date1[1]) <= 12 and 1 <=
                int(date1[2]) < 9999):
            break
    while True:
        date_input2 = input("Input second date DD-MM-YYYY: ")
        date2 = date_input2.split("-")
        if (1 <= int(date2[0]) <= 31 and 1 <= int(date2[1]) <= 12 and 1 <=
                int(date2[2]) < 9999):
            break
    return date_input1, date1, date_input2, date2


# Calculate difference between dates and return difference in days
def get_difference(date1, date2):
    try:
        # Difference between date2 and date1
        return (date(int(date2[2]), int(date2[1]), int(date2[0]))
                - date(int(date1[2]), int(date1[1]), int(date1[0])))
    # If date value is out of range, catch the error
    except ValueError:
        print("Date is out of range\n")
        main()


main()
