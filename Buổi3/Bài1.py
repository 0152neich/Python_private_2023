import math
a = int(input())
b = int(input())
c = int(input())
d = int(input())
e = int(input())
f = int(input())
m = math.sqrt((c - a)**2 + (d - b)**2)
n = math.sqrt((e - c)**2 + (f - d)**2)
k = math.sqrt((a - e)**2 + (b - f)**2)
print('TAM GIÁC') if (m + n > k and n + k > m and k + m > n) else print('KHÔNG PHẢI TAM GIÁC')