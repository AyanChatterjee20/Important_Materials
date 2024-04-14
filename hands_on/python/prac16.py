vowel = ['a', 'e', 'i', 'o', 'u']
word = "programming"
c = 8
val = list(word)
s = 0
for i in val:
    if i not in vowel:
        s += 1
print(f"Constants : {s}")

name = 'Python is 1'
val = list(name)
sp = val.count(' ')
d = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
ltr = 0
for i in d:
    if i in val:
        ltr += 1
print(f"Space : {sp}")
print(f"Digit : {ltr}")
v = len(val) - sp - ltr
print(f"Letter : {v}")

word_list = ["apple", "banana", "apple", "cherry", "banana", "apple"]
val = {key: word_list.count(key) for key in word_list}
l = [v for _, v in val.items()]
l.sort()
h = l[-1]
val = {key: word_list.count(key) for key in word_list if word_list.count(key) == h}
print(val)
