# Find second most repetitive element from a given list
# Sort dictionary by keys and by values

def find_nth(val, d):
    # print(d)
    l = []
    for key, val in d.items():
        l.append(val)
    l.sort()
    # print(sum(l))
    temp = l[-2]
    final = [key for key, val in d.items() if val == temp]
    print(f"Second most repetitive element is : {final[0]}")


def sort_key(d):
    l = list(d.keys())
    l.sort(reverse=True)
    d1 = {key: d[key] for key in l}
    print(d1)


def sort_val(d):
    l = list(d.values())
    l = sorted(l)
    d1 = {key: val1 for val1 in l for key, val2 in d.items() if val1 == val2}
    print(d1)


def main():
    try:
        val = ["aaa", "bbb", "ccc", "aaa", "aaa", "eee", "ccc", "ccc", "aaa", "eee"]
        d = {key: val.count(key) for key in val}
        sort_key(d)
        sort_val(d)
        find_nth(val, d)
    except Exception as e:
        print(e)


if __name__ == "__main__":
    main()
