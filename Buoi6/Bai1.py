def MyMutiple(*args):
    s = 1
    for i in args:
        s *= i
    return s

t = tuple(map(float, input().split()))
print(MyMutiple(*t))