l = list(map(int, input().split()))

res = []
l1 = []

for num in l:
    if not l1 or num == l1[0]:
        l1.append(num)
    else:
        res.append(l1)
        l1 = [num]

if l1:
    res.append(l1)

print(res)
