# Khai báo thư viện
import math
# Khai báo biến
# Định nghĩa hàm
def xuatChuoiNhiPhan(N):
    if N < 0:
        return "-1"
    return bin(N)[2:]

def laPalindrome(N):
    if N < 0:
        return False
    return str(N)==str(N)[::-1]

def laSoNguyenTo(K):
    if K <= 1:
        return False
    for i in range (2,K):
        if K % i == 0:
            return False
        return True

def tongSoNguyenTo(N):
    tong = 0
    if N <= 1:
        return "0"
    for i in range(2,N+1):
        if laSoNguyenTo(i)==True:
            tong + i
        return tong

# Hàm main
def main():
    N = int(input("Nhap vao so N: "))
    K = int(input("Nhap vao so K: "))
    print(xuatChuoiNhiPhan(N))
    print(laPalindrome(N))
    print(laSoNguyenTo(K))
    print(tongSoNguyenTo(N))
# Gọi hàm main
if __name__ == "__main__":
    main()