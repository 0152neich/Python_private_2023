a = set(map(int,input().split()))
b = list(a)
t = []
m = []
if 11 in a:
    print('số 11 đã có trong set')
else:
    a.add(11)
print(a)
for i in range(len(b)):
    for j in range(i + 1, len(b)):
        if b[i] + b[j] == 11:
            t.append((b[i], b[j]))
            m.append(b[i])
            m.append(b[j])

t = tuple(t)
print(t)
m = tuple(m)
print(sum(m))
