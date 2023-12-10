# word count and char count of a given string


def word_count(val):
    l = val.split(' ')
    d = {key: l.count(key) for key in l}
    print(f"Word count of the string '{val}' is {d} ")


def char_count(val):
    l = list(val)
    d = {key: l.count(key) for key in l}
    print(f"Char count of the string '{val}' is {d} ")


def main():
    try:
        val = input("Enter the main string:")
        word_count(val)
        char_count(val)
    except Exception as e:
        print(e)


if __name__ == "__main__":
    main()
