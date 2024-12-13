import math

def xuatChuoiNhiPhan(N):
    pass
def laPalindrome(N):
    ban_goc =str(N)
    daonguoc_so =ban_goc[::-1]
    if ban_goc ==daonguoc_so:
        return True
    else:
        return False
def laSoNguyenTo(K):
    if K<=1:
        return False
    if K==2:
        return True
    if K%2==0:
        return False
    for i in range (3,int( K ** 0.5)+ 1, 2):
        if K%i==0:
            return False
    return True
def tongSoNguyenTo(N):
    TONG=0
    for i in range (2, N+1):
        if laSoNguyenTo(i):
            TONG += i
    return TONG    
def main():
    N = int(input("Nhap vao so N: "))
    print(laSoNguyenTo(N))
    print(tongSoNguyenTo(N))
    print(xuatChuoiNhiPhan(N))
    print(laPalindrome(N))
if __name__ == "__main__":
    main()