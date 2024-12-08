# Khai báo thư viện
# Khai báo biến
# Định nghĩa hàm
def xuatChuoiNhiPhan(N):
    if N < 0:
        print("N khong phai so nguyen duong")
        return -1
    return bin(N)[2:]
def laPalindrome(N):
    pass
def laSoNguyenTo(K):
    if (K < 2):
        return False
    for i in range (2,int(K**0.5 + 1)):
        if K % i == 0:
            return False
    return True
def tongSoNguyenTo(N):
    Tong=0
    if N < 2:
        return 0
    for i in range(2,N-1):
        if(laSoNguyenTo(i)):
            Tong+=i
    return Tong
            
# Hàm main
def main():
    N = int(input("Nhap vao so N: "))
    print(f"Nhi phan cua {N} la: {xuatChuoiNhiPhan(N)}")

    K = float(input("Nhap mot so K: "))
    print(laSoNguyenTo(K))

    N = int(input("Nhap vao so N: "))
    print(f"Tong so nguyen to la {tongSoNguyenTo(N)}")
# Gọi hàm main
if __name__ == "__main__":
    main()