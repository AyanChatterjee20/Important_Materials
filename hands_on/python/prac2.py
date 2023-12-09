# palindrome number and prime number check in that interval
import math as m
import sys


def palindrome_check(val):
    val = str(val)
    l = len(val)
    if val[:m.floor(l / 2)] == val[m.ceil(l / 2):][::-1]:
        print(f"Nearest palindrome number of given number : {val}")
    else:
        palindrome_check(int(val) + 1)


def prime_check(val):
    l = []
    for val1 in range(2, val + 1):
        for i in range(2, m.floor(val1 / 2)):
            if val1 % i == 0:
                break
        else:
            l.append(val1)
    print(f"List of prime numbers in the given interval : {l}")


def main():
    try:
        val = int(input("Enter the number :"))
        palindrome_check(val)
        prime_check(val)
    except Exception as e:
        print(e)


if __name__ == '__main__':
    main()
