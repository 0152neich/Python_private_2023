def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

class PS():
    def __init__(self, tuSo, mauSo) -> None:
        self.tuSo = tuSo
        self.mauSo = mauSo
        
    def __mul__(self, other):
        tuSo = self.tuSo * other.tuSo
        mauSo = self.mauSo * other.mauSo
        gcd_ = gcd(tuSo, mauSo)
        return PS(tuSo // gcd_, mauSo // gcd_)

s = PS(1, 1) 
for _ in range(int(input())):
    a, b = map(int, input().split())
    s *= PS(a, b)
print(s.tuSo, s.mauSo)

