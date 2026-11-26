#!/usr/bin/env python3
# Created By: Kaylee R
# Date: 24, 11, 2026
# This program uses a for loop
# to print numbers from 1000 to 2000
# 5 numbers per line with spaces in between.


def main():
    # set up the for loop
    for counter in range(10, 21):
        # use if statement to make sure it prints 5 num per line
        if counter == 10:
            print(counter, end=" ")
        elif counter % 5 == 0:
            print("")
            print(counter, end=" ")
        else:
            print(counter, end=" ")


if __name__ == "__main__":
    main()
