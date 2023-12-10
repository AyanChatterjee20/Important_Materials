# Check if the sub-string is in a string or not and split the string , join with a different delimiter
# try with val = "geek for geek" and "geek"


def check_string(val, sub):
    l = val.split()
    if (sub in val) and (sub in l):
        c = [l.count(key) for key in l if key == sub][0]
        print(f"Sub-string is present and {c} times")
    else:
        print("Sub-string is not present")


def split_join(val):
    l = val.split(' ')
    fv = '-'.join(l)
    print(f"Replace the delimiter ' ' with '-' in the given string : {fv}")


def main():
    try:
        val = input("Enter the main string:")
        sub = input("Enter the sub-string:")
        check_string(val, sub)
        split_join(val)
    except Exception as e:
        print(e)


if __name__ == "__main__":
    main()
