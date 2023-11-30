import numpy as np
# import matplotlib.pyplot as plt

# Diện tích căn nhà
x = np.array([[50, 75, 80, 60, 70, 90, 100, 65, 85, 105]]).T
# Giá thực tế
y = np.array([[600, 860, 930, 700, 800, 1040, 1150, 750, 970, 1200]]).T

# Building Xbar
one = np.ones((x.shape[0], 1))
Xbar = np.concatenate((one, x), axis=1)

# Tìm w, b
A = np.dot(Xbar.T, Xbar)
b = np.dot(Xbar.T, y)
W = np.dot(np.linalg.pinv(A), b)
b = W[0][0]
w= W[1][0]
print('w = {} b = {}'.format(w, b))
print('Dự đoán giá nhà có diện tích 40 m2:',40*w + b)


# Preparing the fitting line 
# x0 = np.linspace(40, 110, 2)
# y0 = b + w * x0

# Vẽ đồ thị dự đoán
# plt.plot(x.T, y.T, 'ro')     
# plt.plot(x0, y0)
# plt.axis([35, 120, 450, 1300])
# plt.xlabel('S (m2)')
# plt.ylabel('T (100 * USD)')
# plt.show()
