# Sort given array and sum all the numbers of an array
# Find nth largest element of a given array
import sys
from functools import reduce


def nth_largest(l):
    n = int(input("Enter the nth value to find the largets in the given array: "))
    l.sort()
    v = l[-n]
    print(f"Sorted array is {l} and the nth highest is {v}")


def _sum(l):
    val = reduce(lambda a, b: a + b, l)
    print(f"Sum of the numbers of array is : {val}")


def _sort(l):
    val = len(l)
    for i in range(val):
        if l[i] > 0:
            l.append(l[i])
            l[i] = ''
        else:
            pass
    l = [i for i in l if i != '']
    print(f"Left side negative numbers and right side positive numbers : {l}")


def main():
    try:
        val = int(input("Enter the size of the array: "))
        l = []
        for i in range(val):
            tmp = int(input("Enter the value: "))
            l.append(tmp)
        nth_largest(l)
        _sum(l)
        _sort(l)
    except Exception as e:
        print(e)


if __name__ == "__main__":
    main()
