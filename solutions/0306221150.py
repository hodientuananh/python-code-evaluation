# Khai báo thư viện
import math
# Khai báo biến
# Định nghĩa hàm
def xuatChuoiNhiPhan(N):
    if N%2==0:
        return N
    pass
def laPalindrome(N):
    pass
def laSoNguyenTo(K):
    d=0
    for x in range(1,K):
        if K%x==0:
            d=d+1
        return "True" if d==2 else "False"
         
    pass
def tongSoNguyenTo(N):
    t = 0
    if N < 2:
        return 0
    for x in range(2,N):
        if laSoNguyenTo(N)==True:
            t =t+x
        else:
            continue
    return t
    pass
# Hàm main
def main():
    N = int(input("Nhap vao so N: "))
    print(xuatChuoiNhiPhan(N))
    print(laSoNguyenTo(N))
    print("Tong cua cac so nguyen to la:",tongSoNguyenTo(N))
# Gọi hàm main
if __name__ == "__main__":
    main()