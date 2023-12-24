import numpy as np

# Tạo mảng 1-D n phần tử trong [1-14]
n = int(input('Nhập số phần tử:'))
a = np.random.randint(1, 14, n, dtype=int)
print('Mảng 1-D với n phần tử trong [1-14]:\n', a)
print(f'Số chiều:{a.ndim}\nHình dạng mảng:{a.shape}\nlen:{len(a)}\nKích thước mỗi phần tử:{a.itemsize}\nKiểu dữ liệu:{a.dtype}')

# Tạo mảng 1-D với 100 số chẵn đầu tiên
b = np.arange(0, 200, 2)
print('Mảng 1-D với 100 số chẵn đầu tiên:\n',b)
print(f'Số chiều:{b.ndim}\nHình dạng mảng:{b.shape}\nlen:{len(b)}\nKích thước mỗi phần tử:{b.itemsize}\nKiểu dữ liệu:{b.dtype}')

#Tạo mảng nxn với 100 phần tử 0
c = np.zeros((10, 10))
print('Mảng nxn với 100 phần tử 0:\n',c)
print(f'Số chiều:{c.ndim}\nHình dạng mảng:{c.shape}\nlen:{len(a)}\nKích thước mỗi phần tử:{a.itemsize}\nKiểu dữ liệu:{a.dtype}')

#Tạo ma trận đơn vị nxn
d = np.eye(n)
print(f'Ma trận đơn vị kích thước {n}x{n}:\n',d)
print(f'Số chiều:{d.ndim}\nHình dạng mảng:{d.shape}\nlen:{len(a)}\nKích thước mỗi phần tử:{a.itemsize}\nKiểu dữ liệu:{a.dtype}')

# Tạo ma trận đường chéo
e = np.diag(a)
print('Ma trận đường chéo với các giá trị trên đường chéo là ma trận a:\n', e)
print(f'Số chiều:{e.ndim}\nHình dạng mảng:{e.shape}\nlen:{len(a)}\nKích thước mỗi phần tử:{a.itemsize}\nKiểu dữ liệu:{a.dtype}')
