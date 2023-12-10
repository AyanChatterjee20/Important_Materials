# All permutations of a given string and create a complete string with ' ' seperator.
# replace a certain sub-string with given sub string : "Original"
from itertools import permutations


def per_replace(val):
    pr = permutations(val)
    fs = [''.join(prem) for prem in pr]
    line = ' '.join(fs)
    final = line.replace(val, "Original")
    print(final)


def main():
    try:
        val = input("Enter the string:")
        per_replace(val)
    except Exception as e:
        print(e)


if __name__ == "__main__":
    main()
