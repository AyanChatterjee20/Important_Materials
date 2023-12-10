# Check if the string Symmetrical and palindrome
# try with val = amaama or khokho

def palindrome(val):
    l = int(len(val) / 2)
    if val[:l] == val[-l:][::-1]:
        print(f"Given string {val} is palindrome")
    else:
        print(f"Given string {val} is not palindrome")


def symmetrical(val):
    l = int(len(val) / 2)
    if val[:l] == val[-l:]:
        print(f"Given string {val} is symmetrical")
    else:
        print(f"Given string {val} is not symmetrical")


def main():
    try:
        val = input("Enter the string: ")
        symmetrical(val)
        palindrome(val)
    except Exception as e:
        print(e)


if __name__ == "__main__":
    main()
