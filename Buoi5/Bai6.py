d = {'01': 8, '02': 7.5, '03': 3, '04': 2.5, '05': 10}
l = [value for value in d.values() if 2.5 <= value <= 3.5]
print('Số sinh viên có điểm tổng kết trong đoạn [2.5, 3.5] là:', len(l))

d['06'] = 1
k = [key for key, value in d.items() if value <= 2]

for i in k:
    del d[i]

print('Danh sách sau khi xóa các sinh viên có điểm tổng kết nhỏ hơn 2 là:',d)