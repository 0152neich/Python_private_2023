from random import choice

n = int(input('Nhập số sinh viên: '))
ds = {}

for i in range(n):
    l = choice(['CNTT', 'KHMT', 'KTPM', 'HTTT'])
    m = 2022600001 + i

    acc = 'Account' + str(i + 1)

    student_data = {
        'Username': str(m),
        'Password': l + str(m)
    }

    ds[acc] = student_data

print(ds)
