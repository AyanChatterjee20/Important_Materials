ip = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
op = [[1, 4, 9], [16, 25, 36], [49, 64, 81]]

# d={key:ip.count(key) for key in ip}
# print(d)


# op = [[i * i] for val in ip for i in val]
# print(op)
op = []
for val in ip:
    l = []
    for i in val:
        l.append(i * i)
    op.append(l)

ip_1 = [i for val in ip for i in val]
op_1 = [i for val in op for i in val]

# print(ip_1)
# print(op_1)

l = []

for i in ip_1:
    if op_1.count(i) > 0:
        l.append(i)

print(l)
