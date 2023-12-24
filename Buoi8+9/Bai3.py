import numpy as np

a = np.random.randint(0, 11, size=(3, 20))
print('Mảng ban đầu:\n',a)
print(f'Môn:ĐSTT\nVị trí điểm lớn nhất:{np.argmax(a, axis= 1)[0]}\nVị trí điểm nhỏ nhất:{np.argmin(a, axis=1)[0]}')
print(f'Môn:XSTK\nVị Trí điểm lớn nhất:{np.argmax(a, axis= 1)[1]}\nVị trí điểm nhỏ nhất:{np.argmin(a, axis=1)[1]}')
print(f'Môn:GT\nVị trí điểm lớn nhất:{np.argmax(a, axis= 1)[2]}\nVị trí điểm nhỏ nhất:{np.argmin(a, axis=1)[2]}')

flat_a = a.flatten()
a = a[a!= 0]
print('Mảng sau khi được làm phẳng và xóa đi điểm 0:\n',a)

sort_a = np.sort(a, kind='quicksort')[::-1]
print('Mảng sau khi được sắp xếp giảm dần bằng quicksort:\n', sort_a)

print(sort_a)
k = float(input('Nhập k:'))
print(np.searchsorted(sort_a, k))
