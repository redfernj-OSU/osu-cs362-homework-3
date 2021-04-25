#!/usr/bin/python3

"""
CS 362 Homework 1 - Q4 Programming Portion
Jacob Redfern

To Run: Run in the Command Line using python version 3
    python jacob_redfern_hw1.py

Take a user inputed year and state if it is a leap year.

CS 362 Homework 3 - Q3 Programming Portion

Implement error handing to the leap year program.

"""

def leap_check(year):
    """Check if the inputed year is a leap year"""
    if year%4 == 0 and year%100 != 0:
        leap = True

    elif year%4 == 0 and year%400 == 0:
        leap = True

    else:
        leap = False

    return leap

def main():
    """Main function, does the bulk of the calculation"""
    year = input("Enter Year: ")

    # Error Handleing:

    try:
        int_year = int(year)

        if int_year <= 0:
            print("The number must be positive.")
            return
            
    except ValueError:
        print("You must enter an integer.")
        return

    # Calculations:

    if leap_check(int_year) is True:
        print(int_year, "is a leap year")

    elif leap_check(int_year) is False:
        print(int_year, "is not a leap year")

if __name__ == '__main__':
    main()
