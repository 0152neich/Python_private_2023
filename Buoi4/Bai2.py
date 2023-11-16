n = int(input())
l = list(map(int, input().split()))
l1 = []
cnt = 0

for i in l:
    if i % 2 != 0:
        cnt += 1
        l1.append(i)

print(cnt)
for i in sorted(l1):
    print(i, end=' ')