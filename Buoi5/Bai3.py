a = input().split()
cnt = list(a.count(x) for x in set(a))
MAX = 0
for i in cnt:
    if i > MAX:
        MAX = i
t = [x for x in set(a) if a.count(x) == MAX]

t1 = [(word, MAX) for word in t]
print(tuple(t1))