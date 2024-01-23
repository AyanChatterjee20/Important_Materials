# Find repetitive element in a given list
# Print square of each number in the same format in a given list
# Find the common element in the above input & output list

ip_f = [1, 1, 2, 3, 7, 2, 9]
ip = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

d = {key: ip.count(key) for key in ip_f}
print(d)

op = []
for val in ip:
    l = []
    for i in val:
        l.append(i * i)
    op.append(l)
print(op)

ip_1 = [i for val in ip for i in val]
op_1 = [i for val in op for i in val]

l = [i for i in ip_1 if op_1.count(i) > 0]

print(l)
