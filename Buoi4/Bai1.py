s = input()
cnt = 0
if int(s[3:5]) != 2:
    a = 31 if int(s[3:5]) in [1, 3, 5, 7, 8, 10, 12] else 30
    cnt += a - int(s[:2]) + 1
    for i in range(int(s[3:5]) + 1, 13):
        if i == 2:
            b = 29 if (int(s[6:]) % 4 == 0 and int(s[6:]) % 100 != 0) or (int(s[6:]) % 400 == 0) else 28
            cnt += b
        else:
            c = 31 if i in [1, 3, 5, 7, 8, 10, 12] else 30
            cnt += c
else:
    a = 29 if (int(s[6:]) % 4 == 0 and int(s[6:]) % 100 != 0) or (int(s[6:]) % 400 == 0) else 28
    cnt += a - int(s[:2]) + 1
    for i in range(int(s[3:5]) + 1, 13):
        c = 31 if i in [1, 3, 5, 7, 8, 10, 12] else 30
        cnt += c
print(cnt)