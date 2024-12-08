# Khai báo thư viện
import math;
# Khai báo biến
N = 0
# Định nghĩa hàm
def xuatChuoiNhiPhan(N):
    if N > 1:
        return bin(N)[2:]
    else:
        return "-1"
def laPalindrome(N):
    s = str(N)
    return s == s[::1]
def laSoNguyenTo(K):
    if K < 2:
        return False
    for i in range(2, int(math.sqrt(K)) + 1):
        if K % i == 0:
            return False
    return True
def tongSoNguyenTo(N):
    tong = 0
    for i in range(2, N + 1):
     if laSoNguyenTo(i):
        tong +=1
    return tong
# Hàm main
def main():
    N = int(input("Nhap vao so N: "))
    K = int(input("Nhap vao so K: "))
    print(xuatChuoiNhiPhan(N))
    print(laPalindrome(N))
    print(laSoNguyenTo(K))
    tong = tongSoNguyenTo(N)
    print(tongSoNguyenTo(N))
    
# Gọi hàm main
if __name__ == "__main__":
    main()