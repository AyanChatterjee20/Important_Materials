# print * tree
import math as m


def normal_tree(val):
    for i in range(1, val + 1):
        tmp = i * '*'
        print(tmp)


def pyramid_tree(val):
    val = val * 2
    for i in range(1, val, 2):
        tmp = ' ' * m.floor((val - i) / 2) + i * '*' + ' ' * m.floor((val - i) / 2)
        print(tmp)


def main():
    try:
        val = int(input("Enter the height of the tree:"))
        normal_tree(val)
        pyramid_tree(val)
    except Exception as e:
        print(e)


if __name__ == "__main__":
    main()
