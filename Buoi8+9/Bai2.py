import numpy as np

n = int(input("Nhập kích thước của vector: "))

a_input = input(f"Nhập {n} phần tử của vector a: ")
a = np.array([int(x) for x in a_input.split()])

b_input = input(f"Nhập {n} phần tử của vector b: ")
b = np.array([int(x) for x in b_input.split()])

print(f'Max(a):{np.max(a)}\nMin(a):{np.min(a)}\nGTTB(a):{np.mean(a)}\nĐộ lệch chuẩn(a):{np.std(a)}\nGTTV(a):{np.median(a)}')
print(f'Max(b):{np.max(b)}\nMin(b):{np.min(b)}\nGTTB(b):{np.mean(b)}\nĐộ lệch chuẩn(b):{np.std(b)}\nGTTV(b):{np.median(b)}')

#Khởi tạo ma trận c
c = np.stack((a, b))
print(c)

#Khởi tạo ma trận d
d = np.random.normal(np.mean(b), np.std(b), size=(n, n))
print(d)

d1 = np.linalg.pinv(d)
d2 = d.T
print(f'Tổng:\n{d2 + d1}\nHiệu:\n{d2 - d1}\nTích:\n{d2@d1}\n')

e = np.reshape(c, (c.shape[0], c.shape[1], 1))
print(e)
