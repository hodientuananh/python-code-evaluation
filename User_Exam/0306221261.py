# Khai báo thư viện
import math
# Khai báo biến

# Định nghĩa hàm
def xuatChuoiNhiPhan(N):
    if N <= 0:
        return -1
    else:
        return bin(N)[2:]

# def laPalindrome(N):
# pass
def laSoNguyenTo(K):
    if K <=2:
        return (" Nhap lai so khac: ")
    elif K % K == 0 and K % 1 == 0:
        return True
    else:
        return False

def tongSoNguyenTo(N):
    tongnt=0
    for i in range (2,N):
        if laSoNguyenTo(K)
pass
# # Hàm main
def main():
    N = int(input("Nhap vao so N: "))
    print(f"Chuoi nhi phan la:{xuatChuoiNhiPhan(N)}")

    K = int(input("Nhap vao so K: "))
    print(laSoNguyenTo(K))
# # Gọi hàm main
if __name__ == "__main__":
main()
