# palindrome number and prime number check
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
    for i in range(2, m.floor(val / 2)):
        if val % i == 0:
            print("Given number is not prime.")
            sys.exit(0)
    print("Given number is prime.")


def main():
    try:
        val = int(input("Enter the number :"))
        palindrome_check(val)
        prime_check(val)
    except Exception as e:
        print(e)


if __name__ == '__main__':
    main()
