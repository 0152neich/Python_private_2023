class Hiter:
    def __init__(self, id, ten, tuoi, gen) -> None:
        self._id = id
        self._ten = ten
        self._tuoi = tuoi
        self._gen = gen
        
    def __str__(self) -> str:
        return f'Id:{self._id} || Ten:{self._ten} || Tuoi:{self._tuoi} || Gen:{self._gen}'
   
    def nhap():
        id = input('Nhập id:')
        ten = input('Nhập tên:')
        tuoi = input('Nhập tuổi:')
        gen = input('Thế hệ HIT:')
        
        return Hiter(id, ten, tuoi, gen)
    
    @staticmethod
    def danhSach(hiters):
        for hiter in hiters:
            print(hiter)

class Ban:
    def __init__(self, id, ten, tuoi, gen, idBan, tenBan, truongBan: Hiter, thanhVien: list) -> None:
        super().__init__()
        self.__idBan = idBan
        self.__tenBan = tenBan
        self.__truongBan = truongBan
        self.__thanhVien = thanhVien
        
    def nhap():
        idBan = input("Nhập ID Ban: ")
        tenBan = input("Nhập tên Ban: ")
        print("\nNhập thông tin Trưởng Ban:")
        truongBan = Hiter.nhap()
        print("\nNhập thông tin Thành viên:")
        thanhVien = []
        soThanhVien = int(input('Nhập số lượng thành viên:'))
        for i in range(soThanhVien):
            print(f'Nhập thông tin thành viên thứ {i + 1}')
            thanhVien_ban = Hiter.nhap()
            thanhVien.append(thanhVien_ban)
            
        return Ban(None, None, None, None,idBan, tenBan, truongBan, thanhVien)

    def __str__(self) -> str:
        return super().__str__()
    
    def dsHiter(self):
        print(f'\nThông tin ban {self.__tenBan}:')
        print('\nThông tin trưởng ban:')
        print(self.__truongBan)
        print('\nDanh sách thành viên:')
        for i, hiter in enumerate(self.__thanhVien, 1):
            print(f'{i}. {hiter}')
    
    def get_tenBan(self):
        return self.__tenBan
        
    def xoa(self, tenHiter):
        for hiter in self.__thanhVien:
            if hiter._ten == tenHiter:
                self.__thanhVien.remove(hiter)
                print(f"Hiter '{tenHiter}' đã bị xóa khỏi ban '{self.__tenBan}'.")
                return
        print(f"Không tìm thấy Hiter có tên '{tenHiter}' trong ban '{self.__tenBan}'.")

    def add(self, hiter):
        if hiter not in self.__thanhVien:
            self.__thanhVien.append(hiter)
            print(f"Hiter '{hiter._ten}' đã được thêm vào ban '{self.__tenBan}'.")
        else:
            print(f"Hiter '{hiter._ten}' đã có trong ban '{self.__tenBan}'.")

# Nhập thông tin Hiter
n = int(input("Nhập số lượng Hiter: "))
danh_sach_hiter = []
for i in range(n):
    print(f"\nNhập thông tin Hiter thứ {i + 1}:")
    hiter = Hiter.nhap()
    danh_sach_hiter.append(hiter)

# In thông tin Hiter
print("\nThông tin n Hiter:")
Hiter.danhSach(danh_sach_hiter)

# Nhập thông tin Ban
m = int(input('\nNhập số lượng ban:'))
danh_sach_ban = []
for i in range(m):
    print(f'\nNhập thông tin ban thứ {i + 1}:')
    ban = Ban.nhap()
    danh_sach_ban.append(ban)

# In thông tin Ban và Hiter trong từng Ban
for ban in danh_sach_ban:
    ban.dsHiter()

# Xóa và thêm Hiter trong Ban
tenBan_Xoa = input("Nhập tên ban muốn xóa Hiter: ")
for ban in danh_sach_ban:
    if ban.get_tenBan() == tenBan_Xoa:
        tenHiter_Xoa = input("Nhập tên Hiter muốn xóa: ")
        ban.xoa(tenHiter_Xoa)

tenBan_Them = input("Nhập tên ban muốn thêm Hiter: ")
for ban in danh_sach_ban:
    if ban.get_tenBan() == tenBan_Them:
        print(f'\nNhập thông tin Hiter muốn thêm vào ban {tenBan_Them}:')
        hiterThem = Hiter.nhap()
        ban.add(hiterThem)
