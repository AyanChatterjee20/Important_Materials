# Find the duplicate char and replace it with its ascii value
# and print the key & count as a dictionary


def count_replace(val):
    l = list(val)
    d = {key: l.count(key) for key in l}
    final = {key.replace(key, str(ord(key))): value for key, value in d.items()}
    print(final)


def main():
    try:
        val = input("Enter the string:")
        count_replace(val)
    except Exception as e:
        print(e)


if __name__ == "__main__":
    main()
