#!/usr/bin/env python


def is_even(i):
    x = int(i) % 2
    return x == 0

number = input("give me a number: <number>")
print(is_even(number))
