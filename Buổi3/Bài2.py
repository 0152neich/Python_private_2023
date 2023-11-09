n = int(input())
m = int(input())
for _ in range(n):
    x = int(input())
    x = str(x)
    print(x[:len(x)-m] + x[len(x)-m:][::-1])