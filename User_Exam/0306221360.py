# Khai báo biến

# Định nghĩa hàm
def xuatChuoiNhiPhan(N):
    if N > 0:
        return bin(N)[2:]
    else:
        return "-1"
def laPalindrome(N):
    if N > 0:
        n = str(N)
        if n == n[::-1]:
            return True
        else:
            return False
    else:
        return False
def laSoNguyenTo(K):
    if K < 2:
       return False
    for a in range (2,K):
        if K % a == 0:
            return False
    return True
def tongSoNguyenTo(N):
    tong = 0
    if N < 2:
        return 0
    for a in range (2,N+1):
        if laSoNguyenTo(a) == True:
            tong += a
    return tong
# Hàm main
def main():
    N = int(input("Nhap vao so N: "))
    print(xuatChuoiNhiPhan(N))
    print(laPalindrome(N))
    print(laSoNguyenTo(N))
    print(tongSoNguyenTo(N))
# Gọi hàm main
if __name__ == "__main__":
    main()