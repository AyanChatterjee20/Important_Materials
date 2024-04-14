# N number of buildings are standing consecutively. After the last building, there is a playground.
# One have the name and the height of the building in sequence.
# Find from which buildings, one can see the playgrounds and the other from which not.

# d={'a':100,'b':60,'c':70,'d':50}

def find_build(d):
    l_k = d.keys()
    l_v = d.values()

    op = [i for i in l_k if check(d[i], l_v)]
    op_1 = [i for i in l_k if i not in op]
    print(f"List of buildings from which we can see the playground : {op}")
    print(f"List of buildings from which we can't see the playground : {op_1}")


def check(k, l_v):
    # print("Called")
    flag = 0
    l_v = list(l_v)
    # print(l_v)
    for i in l_v:
        if flag == 0:
            if k == i:
                flag = 1
                continue
        elif flag == 1:
            if k <= i:
                print(f"{k} {i}")
                return 0
    print("Here")
    return 1


def main():
    try:
        n = int(input("Enter the number of buildings :"))
        d = {}
        for i in range(n):
            name = input(f"Enter the {i + 1}th name of the building :")
            height = input(f"Enter the {i + 1}th height of the building :")
            d[name] = height
        # print(d)
        find_build(d)
    except Exception as e:
        print(e)


if __name__ == "__main__":
    main()
