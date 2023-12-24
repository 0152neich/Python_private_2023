import pandas as pd

df = pd.read_csv('Car_sales.csv')
print(df)

rows, cols = df.shape
print(f'Số dòng:{rows}\nSố cột:{cols}')

df['Sales_in_thousands'] = df['Sales_in_thousands'].fillna(value=0)
df['__year_resale_value'] = df['__year_resale_value'].fillna(value=df['__year_resale_value'].mean())
df['Price_in_thousands'] = df['Price_in_thousands'].fillna(value=df['Price_in_thousands'].median())

# In ra màn hình vị trí thiếu dữ liệu và DataFrame kết quả
missing_data = df.isnull().sum()
print(f'Vị trí thiếu dữ liệu:\n{missing_data}')
print(f'DataFrame sau khi điền dữ liệu thiếu:\n{df}')

duplicates = df[df.duplicated()]
print(f'\nSố dòng trùng lặp: {len(duplicates)}')
df = df.drop_duplicates()
print('DataFrame sau khi xóa dòng trùng lặp:\n', df)

df['ID'] = df['Manufacturer'] + '_' + df['Model']
print('\nDataFrame sau khi thêm cột "ID":\n', df)

# Tách DataFrame thành 2 DataFrame: Sale và Car
sale = df[['ID', 'Sales_in_thousands', '__year_resale_value', 'Price_in_thousands']]
car = df[['ID'] + [col for col in df.columns if col not in sale.columns]]

sale.to_csv('sale.csv', index=False)
car.to_csv('car.csv', index=False)