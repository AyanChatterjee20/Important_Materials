# check array monotonic increasing or decreasing
import sys


def monotonic(l):
    tmp = l[0]
    flag = 0
    for i in range(1, len(l)):
        if l[i] >= tmp:
            tmp = l[i]
            flag = 1
        elif l[i] < tmp:
            flag = 0
            break
    if flag == 1:
        print(f"Given list is monotonically increasing : {l}")
        sys.exit(0)
    for i in range(1, len(l)):
        if l[i] <= tmp:
            tmp = l[i]
            flag = 1
        elif l[i] > tmp:
            flag = 0
            break
    if flag == 1:
        print(f"Given list is monotonically decreasing : {l}")
        sys.exit(0)
    print(f"Given list is not monotonically : {l}")


def main():
    try:
        val = int(input("Enter the size of the array: "))
        l = []
        for i in range(val):
            tmp = int(input("Enter the value: "))
            l.append(tmp)
        monotonic(l)
    except Exception as e:
        print(e)


if __name__ == "__main__":
    main()
