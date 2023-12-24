import pandas as pd

# Đọc 2 file đã lưu
sale = pd.read_csv('sale.csv')
car = pd.read_csv('car.csv')

print('Tổng số lượng bán ô tô trên thị trường:', sale['Sales_in_thousands'].sum())

print('Giá trị trung bình của ô tô là:', sale['Price_in_thousands'].mean())

# Xác định 10 ID có giá trị bán lại cao nhất và in ra thông tin xe từ DataFrame Car của 10 xe đó.
top_10 = sale.sort_values(by='Price_in_thousands', ascending=False).head(10).merge(car, on='ID')
print('10 ID có giá trị bán lại cao nhất\n', top_10)

# Đếm số lượng phương tiện mỗi loại (Passenger, Car)
vehicle_counts = car['Vehicle_type'].value_counts()
print('Số lượng phương tiện mỗi loại:\n')
print(vehicle_counts)

# Xác định mode của hãng xe
manufacturer_mode = car['Manufacturer'].mode()
print(f'Mode của hãng xe:\n {manufacturer_mode}')

# Sắp xếp DataFrame Sale giảm dần theo mức độ ưu tiên số lượng bán, giá bán, giá bán lại dự kiến và in kết quả ra màn hình.
sorted_sale = sale.sort_values(by=['Sales_in_thousands', 'Price_in_thousands', '__year_resale_value'], ascending=False)
print(f'DataFrame Sale giảm dần theo mức độ ưu tiên số lượng bán, giá bán, giá bán lại dự kiến:\n{sorted_sale}')

# Gộp 2 DataFrame lại theo thuộc tính “ID” và in kết quả ra màn hình
merged = pd.merge(car, sale, on='ID', how='inner')
print(f'DataFrame sau khi gộp theo thuộc tính "ID":\n{merged}')
