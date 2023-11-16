s = input()
res = 0
i = 0
while i < len(s):
    if s[i].isdigit():
        n = int(s[i])
        check = True
        if i > 0 and s[i - 1] == '-':
            check = False
        j = i + 1
        while j < len(s) and s[j].isdigit():
            n = n * 10 + int(s[j])
            j += 1
            i += 1
        if not check:
            n *= -1
        res += n
    i += 1
print(res)
