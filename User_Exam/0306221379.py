#Khai báo thư viện
import math
# Khai báo biến
N=0
# Định nghĩa hàm
def xuatChuoiNhiPhan(N):
    if N>1: 
        return bin(N)[2:]
    else:
        return "-1"

def laPalindrome(N):
    if N>0:
        a=str(N)
        if a==a[::-1]:
            return True
        else :
            return False
    else: 
        return False
    
def laSoNguyenTo(K):
    pass
def tongSoNguyenTo(N):
    tong=0
    if N<2:
        return 0
    for i in range (2,N+1):
        if laSoNguyenTo(i):
            tong=tong+i
        return tong
    
# Hàm main
def main():
    N = int(input("Nhap vao so N: "))

    #K = int(input("Nhap vao so K: "))
    print(xuatChuoiNhiPhan(N))
    print(laPalindrome(N))
    print(tongSoNguyenTo(N))
# Gọi hàm main
if __name__ == "__main__":
    main()