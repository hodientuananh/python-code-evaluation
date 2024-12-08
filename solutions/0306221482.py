# Khai báo thư viện
import math
# Khai báo biến
# Định nghĩa hàm
def xuatChuoiNhiPhan(N):
    if N<=0:
        return -1
    else:
        return bin(N)[2:]
def laPalindrome(N):
    pass
def laSoNguyenTo(K):
    if K<=1:
        return False
    for i in range(2,K):
        if K%i==0:
            return False
    return True
def tongSoNguyenTo(N):
    sum=0
    for i in range(1,N+1):
        if(laSoNguyenTo(i)==True):
            sum +=i
    return sum

# Hàm main
def main():
    N=int(input("Nhap vao so N: "))
    print(xuatChuoiNhiPhan(N))
    print(laSoNguyenTo(N))
    print(tongSoNguyenTo(N))
# Gọi hàm main
if __name__ == "__main__":
    main()