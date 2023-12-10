# Check if the sub-string is in a string or not
# try with val = "geek for geek" and "geek"

def check_string(val, sub):
    l = val.split()
    if (sub in val) and (sub in l):
        print("Sub-string is present")
    else:
        print("Sub-string is not present")


def main():
    try:
        val = input("Enter the main string:")
        sub = input("Enter the sub-string:")
        check_string(val, sub)
    except Exception as e:
        print(e)


if __name__ == "__main__":
    main()
