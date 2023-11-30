def Input():
    arr = [int(x) for x in input().split()]
    return arr

def Sum(x, a):
    s = 0
    for i in range(x + 1):
        s += a[i]
    return s

n = int(input())
a = Input()
q = int(input())
for _ in range(q):
    x = int(input())
    s = Sum(x, a)
    print(s)
