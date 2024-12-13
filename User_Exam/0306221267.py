# Khai báo thư viện
import math
# Khai báo biến
# Định nghĩa hàm
def xuatChuoiNhiPhan(N):
    if N<0:
        print("-1")
    else:
        chuoi = (bin(N).split('b'))
        print(chuoi[1])

def laPalindrome(N):
    pass
def laSoNguyenTo(K):
    if K<2:
        return False
    elif K % 1 == 0 and K % K == 0:
        return True
def tongSoNguyenTo(N):
    pass
# Hàm main
def main():
    N = int(input("Nhap vao so N: "))
    str(xuatChuoiNhiPhan(N))
    print(laSoNguyenTo(N))

# Gọi hàm main
if __name__ == "__main__":
    main()