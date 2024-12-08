def xuatChuoiNhiPhan(N):
    if N < 0:
        return -1
    return bin(N)[2:]

def laPalindrome(N):
    pass

def laSoNguyenTo(K):
    if K < 2:
        return False
    for i in range(2, int(K**0.5 + 1)):
        if K % i == 0:
            return False
    return True
        
def tongSoNguyenTo(N):
    tong = 0
    for i in range(2,N):
        if laSoNguyenTo(i):
            tong += i
    return tong

def main():
    N = int(input("Nhap vao so N: "))
    print(f"Chuoi nhi phan cua N la : {xuatChuoiNhiPhan(N)}")

    K = int(input("Nhap vao so K: "))
    print(f"K la so nguyen to : {laSoNguyenTo(K)}")

    N = int(input("Nhap vao so N: "))
    print(f"Tong so nguyen to < {N} la : {tongSoNguyenTo(N)}")

# Gọi hàm main
if __name__ == "__main__":
    main()