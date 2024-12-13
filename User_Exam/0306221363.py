# Khai báo thư viện
import math
# Khai báo biến
# Định nghĩa hàm
def xuatChuoiNhiPhan(N):
    chuoi=""
    if N==0 or N<0 :
        return "-1"
    else :
        while N!=0:
            if N%2 == 0:
                chuoi=chuoi + "0"
            else :
                chuoi=chuoi + "1"
            N=int(N/2)
        return chuoi
def laPalindrome(N):
    S=0
    Tam=N
    while N!=0:
        donvi=N%10
        N=int(N/10)
        S=S*10+int(donvi)
    if Tam==S :
        return True
    else :
        return False
def laSoNguyenTo(K):
    if K<2 :
        return False
    for i in range(2,K):
        if(K%i==0):
            return False
    return True
def tongSoNguyenTo(N):
    S=0
    for i in range(1,N+1):
        if laSoNguyenTo(i):
            S=S+i
    return S

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
