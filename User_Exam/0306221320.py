# # Ho va ten: Nguyen Tran Tien Dat
# # MSSV: 0306221320
# # Lop: CD TH 22MMTA
# # Mon hoc: Python
# # Kiem tra lan 1

# Khai báo thư viện
import math

# Khai báo biến

# Định nghĩa hàm

def xuatChuoiNhiPhan(N):
    if isinstance(N, int) and N > 0:
        return bin(N)[2:]
    else:
        return "-1"
pass

def laPalindrome(N):
    if isinstance(N, int) and N > 0:
        return str(N) == str(N)[::-1]
    else:
        return False
pass

def laSoNguyenTo(K):
    if K < 2:
        return False
    for i in range(2, K):
        if K % i == 0:
            return False
    else:
        return True
pass

def tongSoNguyenTo(N):
    tongsnt = 0
    for N in range (2, N + 1):
        if laSoNguyenTo(N):
            tongsnt = tongsnt+N
    return tongsnt
pass

# Hàm main
def main():
    N = int(input("Nhap vao so N: "))
    print (xuatChuoiNhiPhan(N))
    print (laPalindrome(N))
    print (laSoNguyenTo(N))
    print (tongSoNguyenTo(N))

# Gọi hàm main
if __name__ == "__main__":
    main()