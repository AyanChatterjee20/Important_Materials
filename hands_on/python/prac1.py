# Print a string in reverse and space in between each character

def reverse(val: str, l: int):
    # val = list(val)
    temp = []
    for i in range(l):
        t = val[l - 1 - i]
        temp.append(t)
    val = ''.join(temp)
    print(f"Reverse of given string : {val}")


def add_space(val: str):
    val = list(val)
    val = ' '.join(val)
    print(f"Added space between each char of given string : {val}")


def main():
    try:
        val = input("Please enter the string:")
        l = len(val)
        reverse(val, l)
        add_space(val)
    except Exception as e:
        print(e)


if __name__ == '__main__':
    main()
