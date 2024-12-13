# Khai báo thư viện
import math
# Khai báo biến
N=int
# Định nghĩa hàm

def xuatChuoiNhiPhan(N): 
   if not isinstance(N,int) or N<=0:
       return -1
   return bin(N)[2: ]

def laPalindrome(N):
    pass


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
