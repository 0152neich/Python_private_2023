from math import gcd

class PhanSo:
    def __init__(self, tu_so, mau_so, **kwargs):
        self.tu_so = tu_so
        self.mau_so = mau_so
        self.rut_gon()

    def rut_gon(self):
        ucln = gcd(self.tu_so, self.mau_so)
        self.tu_so //= ucln
        self.mau_so //= ucln

    @staticmethod
    def tu_hon_so_to_phan_so(tu_hon_so):
        parts = tu_hon_so.split('/')
        phan_nguyen = int(parts[0])
        tu_so = int(parts[1])
        mau_so = int(parts[2])
        return PhanSo(phan_nguyen * mau_so + tu_so, mau_so)
    
    def __str__(self) -> str:
        if self.tu_so == 0:
            return f'a = {self.tu_so}'  # Nếu tử số bằng 0, chỉ hiển thị tử số
        elif self.tu_so < self.mau_so:
            return f'a = {self.tu_so}/{self.mau_so}'  # Nếu tử số nhỏ hơn mẫu số, hiển thị tử số/mẫu số
        else:
            phan_nguyen = self.tu_so // self.mau_so
            tu_so_phan_so = self.tu_so % self.mau_so
            return f'a = {phan_nguyen}/{tu_so_phan_so}/{self.mau_so}'  # Hiển thị dạng hỗn số

class HonSo:
    def __init__(self, phan_nguyen, phan_so, **kwargs):
        self.phan_nguyen = phan_nguyen
        self.phan_so = phan_so

    @staticmethod
    def phan_so_to_hon_so(phan_so):
        phan_nguyen = phan_so.tu_so // phan_so.mau_so
        phan_so.tu_so %= phan_so.mau_so
        return HonSo(phan_nguyen, phan_so)
    
    def __str__(self) -> str:
        return f'b = {self.phan_nguyen * self.phan_so.mau_so + self.phan_so.tu_so}/{self.phan_so.mau_so}'
    
# Nhập đối tượng Math a từ phân số
a_input = input('Nhập phân số: ')
a_tu, a_mau = map(int, a_input.split('/'))
a = PhanSo(a_tu, a_mau)

# Nhập đối tượng Math b từ hỗn số
b_input = input('Nhập hỗn số: ')
b = HonSo.phan_so_to_hon_so(PhanSo.tu_hon_so_to_phan_so(b_input))

# In lại a và b
print(a)
print(b)



