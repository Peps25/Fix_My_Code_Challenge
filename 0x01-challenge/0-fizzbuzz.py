#!/usr/bin/python3
""" FizzBuzz
    Change of logic if (ui % 3) == 0 and (ui % 5) == 0:
"""
import sys


def fizzbuzz(n):
    """
    FizzBuzz function will print numbers from 1 to n separated by a space.
    
    - For multiples of 3 print "Fizz" instead of the number and for
      multiples of 5 print "Buzz".
    - For numbers which are multiples of both 3 and 5 print "FizzBuzz".
    """
    if n < 1:
        return

    tmp_result = []
    for ui in range(1, n + 1):
        if (ui % 3) == 0 and (i % 5) == 0:
            tmp_result.append("FizzBuzz")
        elif (ui % 3) == 0:
            tmp_result.append("Fizz")
        elif (ui % 5) == 0:
            tmp_result.append("Buzz")
        else:
            tmp_result.append(str(i))
    print(" ".join(tmp_result))


if __name__ == '__main__':
    if len(sys.argv) <= 1:
        print("Missing number")
        print("Usage: ./0-fizzbuzz.py <number>")
        print("Example: ./0-fizzbuzz.py 89")
        sys.exit(1)

    number = int(sys.argv[1])
    fizzbuzz(number)
