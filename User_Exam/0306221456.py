# Khai báo thư viện
import math
# Khai báo biến
# Định nghĩa hàm

def xuatChuoiNhiPhan(N):
    if N < 1:
        return "-1"
    CNP =" "
    while N > 0:
        CNP =str(N % 2) + CNP
        N //=2
    return CNP
pass

def laPalindrome(N):
    if N < 0:
        return False
    
    Pal = str (N)
    return Pal==Pal[::-1]


pass

def laSoNguyenTo(K):
    if K <= 1:
        return False
    if K<=3:
        return True
    if K%2==0 or K%3==0:
        return False
    i = 5
    while i * i <= K:
        if K % i == 0 or K % (i + 2)==0:
         return False
        i+=6
    return True 

pass

def tongSoNguyenTo(N):
    if N<2:
        return 0;
    tong = 0
    for N in range (2,N+1):
        if laSoNguyenTo(N):
            tong+=N;
    return tong




pass

# Hàm main
def main():
    N = int(input("Nhap vao so N: "))
    print('Xuat chuoi nhi phan :')
    print(xuatChuoiNhiPhan(N))
    print('LA PAL:')
    print(laPalindrome(N))
    print('laSoNguyenTo:')
    print(laSoNguyenTo(N))
    print('Tong so Nguyen to tu 2-N :')
    print(tongSoNguyenTo(N))

# Gọi hàm main
if __name__ == "__main__":
    main()