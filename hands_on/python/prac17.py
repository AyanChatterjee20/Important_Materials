# Given an list of integers called input and an integer target. Return the index of the two numbers which
# sum up to the target. Do not use the same list element twice.
# In case there is no valid solution, return [-1, -1].
# Return the indexes in increasing order ([1,2] not [2,1])

def check(l, t):
    for i in range(len(l)):
        for j in range(i + 1, len(l)):
            if (l[i] + l[j]) == t:
                return [i, j]
    return [-1, -1]


def main():
    try:
        l = [1, 5, 4, 6, 10]
        t = 10
        o = check(l, t)
        print(f"Output is {o}")
    except Exception as e:
        print("Wrong data")


if __name__ == "__main__":
    main()
