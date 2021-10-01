#!/usr/bin/env python3

# Created by: Mikayla Barthelette
# Created on: Sept 2021
# This program will square every number up to and including your number


def main():
    # this function squares the numbers
    loop_counter = 0

    # input
    user_input = input("Enter an integer >= 0: ")

    # process & output
    try:
        positive_integer = int(user_input)
        assert positive_integer > 0
        for loop_counter in range(positive_integer + 1):
            squared_number = loop_counter ** 2
            print("{0}² = {1}.".format(loop_counter, squared_number))
    except Exception:
        print("You did not enter a positive integer.")
    finally:
        print("\nDone.")


if __name__ == "__main__":
    main()
