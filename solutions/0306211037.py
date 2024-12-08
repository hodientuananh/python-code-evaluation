# Khai báo thư viện
import math
# Khai báo biến
N = int

# Định nghĩa hàm
def xuatChuoiNhiPhan(N):
    if not isinstance(N,int) or N<=0:
        return -1
    return bin(N)[2:]
    

def laPalindrome(N):
    unit = N % 10
    hundred = (N%100) // 10
    thousand = (N%1000) // 100
    str(chuoiso) = str(unit) + str(hundred) + str(thousand)
    if not isinstance(N,int) or N<=0:
        return -1
    return str(chuoiso)
def laSoNguyenTo(K):
    pass
def tongSoNguyenTo(N):
    pass
# Hàm main
def main():
    N = int(input("Nhap vao so N: "))
    kq = xuatChuoiNhiPhan(N)
    print(kq)
# Gọi hàm main
if __name__ == "__main__":
    main()