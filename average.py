#!/usr/bin/env python3

# Created by: Haokai Li
# Created on: Oct 2021
# This Program calculate average
import random


def main():
    # This function calculate average
    my_numbers = []
    loop_number_first = 0
    loop_number_second = 0
    total_number = 0

    # process
    for loop_number_first in range(0, 10):
        calculate_number = random.randint(0, 100)
        my_numbers.append(calculate_number)

    # output
    print("10 random numbers between 1 and 100:")
    print("")

    # process
    for loop_number_second in range(0, len(my_numbers)):
        total_number = total_number + my_numbers[loop_number_second]
        # output
        print("The random number is {0}".format(my_numbers[loop_number_second]))

    # process
    average_number = total_number / len(my_numbers)

    # output
    print("")
    print("Answer: {0}".format(average_number))


if __name__ == "__main__":
    main()
