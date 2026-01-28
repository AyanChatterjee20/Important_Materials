# https://leetcode.com/problems/longest-substring-without-repeating-characters/description/?envType=problem-list-v2&envId=string

def find_max_substr(s):
    start = 0
    max_len = 0
    max_substring = ''
    seen = {}

    for end, char in enumerate(s):
        print(f"{end}  {char}")
        if char in seen and seen[char] >= start:
            print(f"{seen[char]}")
            start = seen[char] + 1
        seen[char] = end
        if end - start + 1 > max_len:
            max_len = end - start + 1
            print(f"{start}   {end}")
            max_substring = s[start:end + 1]

    return max_substring, max_len


def main():
    try:
        val = input("Enter the input string : ")
        max_substring, max_len = find_max_substr(val)
        print(f"The highest substring is : {max_substring} with length of {max_len}")
    except Exception as e:
        print("Raised Exception : ", e)


if __name__ == "__main__":
    main()
