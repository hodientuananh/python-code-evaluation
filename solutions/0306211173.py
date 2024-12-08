import math

def xuatChuoiNhiPhan(N):
    pass
def laPalindrome(N):
    pass
def laSoNguyenTo(N):
    if N < 2:
        return False
    for x in range (2,int(N**0.5)+1):
        if N % x == 0:
            return False
    return True
        
def tongSoNguyenTo(N):
    tsnt = 0
    if N == 1:
        return 0
    for tong in range (2, N-1):
        if N % tong==0:
            tsnt += tong
    return tsnt


def main():
    N = int(input("Nhap vao so N: "))
    if laSoNguyenTo(N) == True:
        print(N,'la so nguyen to')
    else:
        print(N,'khong phai la so nguyen to')
    
    print('tong so nguyen to la',tongSoNguyenTo(N))

if __name__ == "__main__":
    main()  