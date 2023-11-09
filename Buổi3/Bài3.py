i = int(input())

for j in range(i):
    s = input()
    a = int(input())
    b = int(input())
    x = ''
    if a + b >= 190:
        x = 'Xuất sắc'
    elif a + b >= 150:
        x = 'Giỏi'
    elif a + b >= 100:
        x = 'Khá'
    else:
        x = 'Kém'
    print(j + 1, s, a + b, x)