a = 5
b = 17
print('a + b =', a + b)
print('a - b = ', a - b)
print('a * b =', a * b)
print('a chia nguyên b là:', a // b)
print('a mũ b là:', a**b)
print('a chia dư b là:', a % b)
if a - b > 0:
    print('a lớn hơn b')
elif a - b < 0:
    print('a nhỏ hơn b')
else:
    print('a bằng b')
print('a AND b là:', a & b)
print('a or b là:', a | b)
print('a XOR b là:', a ^ b)
print('NOT a == b', not(a == b))
print('a dịch phải 5 bit', a >> 5)
print('a dịch trái 6 bit', a << 6)
c = ~a
print(bin(c))