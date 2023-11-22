a = [input() for _ in range (int(input()))]
b = tuple(a)
print(b)
cnt = 0
for i in b:
    if i.isnumeric():
        cnt += 1
print(cnt)