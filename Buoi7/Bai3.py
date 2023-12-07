class Matrix:
    def __init__(self, hang, cot, value) -> None:
        self._hang = hang
        self._cot = cot
        self._value = value
    
    def __add__(self, other):
        result_values = [[0 for _ in range(self._cot)] for _ in range(self._hang)]
        
        for i in range(self._hang):
            for j in range(self._cot):
                result_values[i][j] = self.get_value(i, j) + other.get_value(i, j)
                
        return Matrix(self._hang, self._cot, result_values)
    
    def __sub__(self, other):
        result_values = [[0 for _ in range(self._cot)] for _ in range(self._hang)]
        
        for i in range(self._hang):
            for j in range(self._cot):
                result_values[i][j] = self.get_value(i, j) - other.get_value(i, j)
                
        return Matrix(self._hang, self._cot, result_values)
    
    def __mul__(self, other):
        result_values = [[0 for _ in range(other._cot)] for _ in range(self._hang)]
        for i in range(self._hang):
            for j in range(other._cot):
                for k in range(self._cot):
                    result_values[i][j] = self.get_value(i, k) * self.get_value(k, j)
        
        return Matrix(self._hang, self._cot, result_values)

    def __truediv__(self, other):
        # Tìm ma trận nghịch đảo của ma trận thứ hai
        inverse_other = self.inverse(other)

        # Kiểm tra xem ma trận nghịch đảo có tồn tại hay không
        if inverse_other is None:
            raise ValueError("Ma trận thứ hai không khả nghịch, không thể thực hiện phép chia.")

        # Nhân ma trận đầu tiên với ma trận nghịch đảo của ma trận thứ hai
        result_values = [[0 for _ in range(other._cot)] for _ in range(self._hang)]
        for i in range(self._hang):
            for j in range(other._cot):
                for k in range(other._hang):
                    result_values[i][j] += self.get_value(i, k) * inverse_other.get_value(k, j)

        return Matrix(self._hang, other._cot, result_values)

    def inverse(self, matrix):
        determinant = self.calculate_determinant(matrix)
        if determinant == 0:
            return None

        inverse_matrix = [[0 for _ in range(matrix._cot)] for _ in range(matrix._hang)]
        for i in range(matrix._hang):
            for j in range(matrix._cot):
                inverse_matrix[i][j] = matrix.get_value(i, j) / determinant

        return Matrix(matrix._hang, matrix._cot, inverse_matrix)

    def calculate_determinant(self, matrix):
        determinant = 1
        for i in range(matrix._hang):
            determinant *= matrix.get_value(i, i)

        return determinant
    
    def __eq__(self, other):

        for i in range(self._hang):
            for j in range(self._cot):
                if self.get_value(i, j) == other.get_value(i, j):
                    result_values = True
        return False
        
    def get_value(self, i, j):
        return self._value[i][j]

    def __str__(self):
        matrix_str = ""
        for row in self._value:
            matrix_str += " ".join(map(str, row)) + "\n"
        return matrix_str.strip()

# Tạo hai ma trận
Matrix1 = Matrix(3, 3, [[1, 2, 3], [4, 5, 6], [7, 8, 9]])
Matrix2 = Matrix(3, 3, [[3, 2, 1], [6, 5, 4], [9, 8, 7]])

sum = Matrix1 + Matrix2
difference = Matrix1 - Matrix2
product = Matrix1 * Matrix2
quotient = Matrix1 / Matrix2

print('Tổng 2 ma trận:\n', sum, '\n')
print('Hiệu 2 ma trận:\n', difference, '\n')
print('Tích 2 ma trận:\n', product, '\n')
print('Nhân ma trận trái với nghịch đảo ma trận phải:\n', quotient, '\n')
print('2 ma trận bằng nhau' if Matrix1 == Matrix2 else '2 ma trận không bằng nhau')