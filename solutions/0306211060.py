# Khai báo thư viện
import math
# Khai báo biến
# Định nghĩa hàm
def xuatChuoiNhiPhan(N):
    pass
def laPalindrome(N):
    pass
def laSoNguyenTo(K):
    if (K>2 or K == 2 and K % K == 1 and K % 1 == 0):
        return True
    else:
        return False
def tongSoNguyenTo(N):
    if (N>2 or N ==2 ):
        return 
    else:
        return 0
# Hàm main
def main():
    N = int(input("Nhap vao so N: "))
    K = int(input("Nhap vao so K: "))
    Songuyento = laSoNguyenTo(K)
    print(Songuyento)
# Gọi hàm 
if __name__ == "__main__":

    main()