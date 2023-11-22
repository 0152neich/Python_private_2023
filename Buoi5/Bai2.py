n = int(input())
a = set(map(int,input().split()))
m = int(input())
k = 0
res = set()
for i in a:
    if k + i <= m:
        res.add(i)
        k += i
print(res)