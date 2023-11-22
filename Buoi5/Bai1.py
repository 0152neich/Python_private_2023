a = set(map(int,input().split()))
b = set(map(int,input().split()))
if (a & b):
    print('Danh sách sinh viên đăng kí tại cả 2 bàn là: ')
    print(a & b)
else:
    print('Không có sinh viên nào đăng kí cả 2 bàn')
print('Danh sách tổng hợp sinh viên đăng kí cả 2 bàn là: ')
print(a | b)
print('Danh sách sinh viên đăng kí tại bàn 1 mà không đăng kí tại bàn 2 là: ')
print(a - b)
print('Danh sách sinh viên đăng kí duy nhất 1 bàn là: ')
print(a ^ b)