#https://leetcode.com/problems/regular-expression-matching/description/
def isMatch(val, pat):
    if len(pat) > len(val):
        print("False")
    elif pat == '.*':
        print("True")
    elif pat == val:
        print("True")
    else:
        if ('.' in pat):
            pos = pat.index(".")
            if (len(val) > 2):
                val = val[:pos] + val[pos + 1:]
                if pat[:pos] == val:
                    print("True")
                else :
                    print("False")
            elif pat[:pos] == val[:pos]:
                print("True")
            else:
                print("False")
        elif '*' in pat:
            pos = pat.index("*")
            if pat[:pos] == val[:pos]:
                print("True")
            else:
                print("False")
        else:
            print("False")



def main():
    try:
        val = input("Enter the input string: ")
        pat = input("Enter the input string : ")
        isMatch(val, pat)
    except Exception as e:
        print(f"Raise Error: {e}")

if __name__ == "__main__":
    main()