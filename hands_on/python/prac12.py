# Python – Extract Unique values dictionary values
# Python program to find the sum of all items in a dictionary


def create_dict(val):
    l = list(val)
    print(l)
    d = {key: ord(key) for key in l}
    return d


def sum_items(val):
    d = create_dict(val)
    sum = 0
    for key, val in d.items():
        sum += val
    print(f"Final Sum is {sum}")


def unique_val(val):
    d = create_dict(val)
    print(d)


def main():
    try:
        val = input("Enter the string:")
        sum_items(val)
        unique_val(val)
    except Exception as e:
        print(e)


if __name__ == "__main__":
    main()
