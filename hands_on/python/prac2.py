# palindrome number and prime number check
import math as m


def palindrome_check(val):
    val = str(val)
    l = len(val)
    if val[:m.floor(l / 2)] == val[m.ceil(l / 2):][::-1]:
        print(f"Nearest palindrome number of given number : {val}")
    else:
        palindrome_check(int(val) + 1)


def prime_check(val):
    pass


def main():
    try:
        val = int(input("Enter the number :"))
        palindrome_check(val)
        pri = prime_check(val)
        print(f"Nearest palindrome number of given number : ")
    except Exception as e:
        print(e)


if __name__ == '__main__':
    main()
