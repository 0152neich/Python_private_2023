l = list(map(str, input().split()))
n = int(input())
res = []

for i in range(n):
    l1 = []
    for j in range(len(l)):
        if j % n == i:
            l1.append(l[j])
    res.append(l1)
    
print(res)