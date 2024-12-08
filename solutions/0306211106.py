# Khai báo thư viện
import math
# Khai báo biến
# Định nghĩa hàm
#Hàm xuatChuoiNhiPhan(N) có input là số N bất kỳ, output là chuỗi string biểu diễn chuỗi
#nhị phân.
#Hàm laPalindrome(N) có input là số N bất kỳ, output là True/ False
#Hàm laSoNguyenTo(K) có input là số K bất kỳ, output là True nếu số đó là nguyên tố, False
#nếu ngược lại
#Hàm tongSoNguyenTo(N) có input là một số N bất kỳ, output là tổng của các số nguyên tố
#trong đoạn [2; N].
def xuatChuoiNhiPhan(N):
    if N <= 0:
        return"-1"
    binary_string = ""
    while N > 0:
        binary_string = str(N % 2) + binary_string
        N //=2
        return binary_string
def laPalindrome(N):
    reversed_N = 0
    original_N = N
    while N > 0:
        reversed_N = reversed_N*10 + N %10
        N // 10
    return original_N == reversed_N

def laSoNguyenTo(K):
    if K <=1:
        return False
    if K <= 3:
        return True
    if  K % 2 ==0 or K % 3 == 0:
        return False
    i =5
    while i*i <=K:
        if K %i==0 or K % (i+2) ==0:
            return False
    i +=6
    return True
def tongSoNguyenTo(N):
    if N < 2:
        return 0
    total = 0
    for i in range(2, N+1):
        if laSoNguyenTo((i)):
            total +=i
            return total
# Hàm main
def main():
    N = int(input("Nhap vao so N: "))
    K = int(input("Nhap vao mot so nguyen to K: "))
    print(xuatChuoiNhiPhan (N))
    print(laPalindrome(N))
    print(laSoNguyenTo(K))
    print(tongSoNguyenTo(N))
# Gọi hàm main
if __name__ == "__main__":
    main()