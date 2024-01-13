val = 'INDIA'

l = list(val)
d = {key: l.count(key) for key in l}

print(d)
